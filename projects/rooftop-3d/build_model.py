"""Build a massing 3D model and a 2D DXF plan of the rooftop from the hand layout.

Units: feet in the DXF; metres in GLB/OBJ/DAE (1 ft = 0.3048 m).
Plan coordinates: x = east (0..45 ft), y = north (0..25 ft), z = up.
Sizes are read off the drawing's proportions and must be checked on site.
"""
import math
import numpy as np
import trimesh
import trimesh.exchange.dae
import ezdxf

FT = 0.3048
W, D = 45.0, 25.0

# pixel → feet, from the layout drawing (border at x 28–880 px, y 28–500 px)
def fx(px): return round((px - 28) * W / 852, 2)
def fy(py): return round((500 - py) * D / 472, 2)

COL = {
    "floor": [205, 205, 200, 255], "parapet": [240, 240, 236, 255], "rooms": [235, 232, 222, 255],
    "deck": [176, 122, 74, 255], "water": [64, 170, 205, 200], "coping": [150, 150, 145, 255],
    "planter": [120, 120, 115, 255], "plant": [70, 140, 70, 255], "counter": [110, 110, 108, 255],
    "bbq": [40, 40, 40, 255], "steps": [160, 110, 70, 255], "awning": [222, 205, 170, 255],
    "post": [30, 30, 30, 255], "lounge": [215, 215, 212, 255], "table": [250, 250, 250, 255],
    "chair": [190, 150, 100, 255], "garden": [100, 165, 80, 255],
}

parts = []  # (layer, mesh)

def box(layer, x0, x1, y0, y1, z0, z1):
    m = trimesh.creation.box(extents=[abs(x1 - x0), abs(y1 - y0), abs(z1 - z0)])
    m.apply_translation([(x0 + x1) / 2, (y0 + y1) / 2, (z0 + z1) / 2])
    parts.append((layer, m))

def cyl(layer, cx, cy, r, z0, z1, sx=1.0, sy=1.0, sections=48):
    m = trimesh.creation.cylinder(radius=r, height=z1 - z0, sections=sections)
    m.apply_scale([sx, sy, 1])
    m.apply_translation([cx, cy, (z0 + z1) / 2])
    parts.append((layer, m))

# floor slab and parapet (3.5 ft high, 0.5 ft thick)
box("floor", 0, W, 0, D, -0.5, 0)
t, h = 0.5, 3.5
box("parapet", 0, W, 0, t, 0, h); box("parapet", 0, W, D - t, D, 0, h)
box("parapet", 0, t, 0, D, 0, h); box("parapet", W - t, W, 0, D, 0, h)

# service block (massing, 8 ft high)
rooms = {
    "Staircase area": (222, 405, 28, 78), "Entrance space": (405, 472, 28, 78),
    "Closet": (222, 325, 78, 112), "Bathroom": (405, 472, 78, 125),
}
for name, (a, b, c, d) in rooms.items():
    box("rooms", fx(a), fx(b), fy(d), fy(c), 0, 8)
box("counter", fx(325), fx(405), fy(112), fy(78), 0, 3)  # vanity sink

# pool zone: deck, oval pool, coping, planters
box("deck", fx(222), fx(405), fy(395), fy(112), 0, 0.3)
pcx, pcy, prx, pry = fx(315), fy(280), 87 * W / 852, 110 * D / 472
cyl("coping", pcx, pcy, 1.0, 0.3, 0.45, sx=prx + 0.5, sy=pry + 0.5, sections=64)
cyl("water", pcx, pcy, 1.0, 0.3, 0.5, sx=prx, sy=pry, sections=64)
for px, py in [(265, 125), (237, 155)]:
    cyl("planter", fx(px), fy(py), 0.8, 0.3, 2.0)
    cyl("plant", fx(px), fy(py), 0.7, 2.0, 4.0)

# service strip: steps, outdoor sink counter, BBQ
sx0, sx1 = fx(410), fx(445)
y_top, y_bot = fy(125), fy(205)
n = 5
for i in range(n):
    ya = y_bot + (y_top - y_bot) * i / n
    box("steps", sx0, sx1, ya, y_top, 0, 0.6 * (i + 1) / n * 2)
box("counter", sx0, sx1, fy(285), fy(210), 0, 3)
box("bbq", fx(410), fx(435), fy(365), fy(305), 0, 3)

# awning walkway: canopy at 9 ft on posts
ax0, ax1, ay0, ay1 = fx(445), fx(545), fy(395), fy(28)
box("awning", ax0, ax1, ay0, ay1, 9.0, 9.2)
for y in np.linspace(ay0 + 0.3, ay1 - 0.3, 4):
    box("post", ax1 - 0.35, ax1 - 0.05, y - 0.15, y + 0.15, 0, 9.0)

# lounge: tile pad, two round tables with six chairs
box("lounge", fx(545), W - t, fy(228), D - t, 0, 0.05)
for px in (665, 765):
    tx, ty = fx(px), fy(110)
    cyl("table", tx, ty, 1.6, 2.3, 2.45)
    cyl("table", tx, ty, 0.15, 0, 2.3)
    for k in range(6):
        ang = 2 * math.pi * k / 6
        cx, cy = tx + 2.7 * math.cos(ang), ty + 2.7 * math.sin(ang)
        box("chair", cx - 0.75, cx + 0.75, cy - 0.75, cy + 0.75, 0, 1.5)

# garden: L-shaped lawn bed, 0.5 ft high
box("garden", fx(755), W - t, fy(395), fy(228), 0, 0.5)
box("garden", fx(635), W - t, t, fy(395), 0, 0.5)

# ---- export 3D (metres) ----
scene = trimesh.Scene()
for i, (layer, m) in enumerate(parts):
    mm = m.copy()
    mm.apply_scale(FT)
    mm.visual.face_colors = COL[layer]
    scene.add_geometry(mm, node_name=f"{layer}_{i:02d}", geom_name=f"{layer}_{i:02d}")
out = "model/"
scene.export(out + "rooftop.obj")
with open(out + "rooftop.dae", "wb") as f:
    f.write(trimesh.exchange.dae.export_collada(list(scene.geometry.values())))
zup_to_yup = trimesh.transformations.rotation_matrix(-math.pi / 2, [1, 0, 0])
gscene = scene.copy(); gscene.apply_transform(zup_to_yup)
gscene.export(out + "rooftop.glb")

# ---- export 2D plan (feet) ----
doc = ezdxf.new("R2010", setup=True); doc.units = ezdxf.units.FT
msp = doc.modelspace()
for name, c in [("PARAPET", 7), ("ROOMS", 1), ("POOL", 5), ("SERVICE", 3), ("AWNING", 30), ("LOUNGE", 8), ("GARDEN", 3), ("TEXT", 7), ("DIMS", 2)]:
    doc.layers.add(name, color=c)
def rect(layer, x0, x1, y0, y1):
    msp.add_lwpolyline([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], close=True, dxfattribs={"layer": layer})
def label(text, x, y, hgt=0.6):
    msp.add_text(text, height=hgt, dxfattribs={"layer": "TEXT"}).set_placement((x, y), align=ezdxf.enums.TextEntityAlignment.MIDDLE_CENTER)
rect("PARAPET", 0, W, 0, D); rect("PARAPET", t, W - t, t, D - t)
for name, (a, b, c, d) in rooms.items():
    rect("ROOMS", fx(a), fx(b), fy(d), fy(c)); label(name, (fx(a) + fx(b)) / 2, (fy(c) + fy(d)) / 2, 0.45)
rect("SERVICE", fx(325), fx(405), fy(112), fy(78)); label("Sink", (fx(325) + fx(405)) / 2, (fy(78) + fy(112)) / 2, 0.45)
rect("POOL", fx(222), fx(405), fy(395), fy(112))
msp.add_ellipse((pcx, pcy), major_axis=(0, pry), ratio=prx / pry, dxfattribs={"layer": "POOL"}); label("Pool", pcx, pcy)
for px, py in [(265, 125), (237, 155)]:
    msp.add_circle((fx(px), fy(py)), 0.8, dxfattribs={"layer": "POOL"})
rect("SERVICE", sx0, sx1, y_bot, y_top); label("Steps", (sx0 + sx1) / 2, (y_bot + y_top) / 2, 0.35)
rect("SERVICE", sx0, sx1, fy(285), fy(210)); label("Sink", (sx0 + sx1) / 2, (fy(285) + fy(210)) / 2, 0.35)
rect("SERVICE", fx(410), fx(435), fy(365), fy(305)); label("BBQ", (fx(410) + fx(435)) / 2, (fy(365) + fy(305)) / 2, 0.35)
rect("AWNING", ax0, ax1, ay0, ay1); label("Awning shaded area", (ax0 + ax1) / 2, (ay0 + ay1) / 2, 0.5)
label("Lounge area", fx(700), fy(170))
for px in (665, 765):
    msp.add_circle((fx(px), fy(110)), 1.6, dxfattribs={"layer": "LOUNGE"})
msp.add_lwpolyline([(fx(755), fy(228)), (W - t, fy(228)), (W - t, t), (fx(635), t), (fx(635), fy(395)), (fx(755), fy(395))], close=True, dxfattribs={"layer": "GARDEN"})
label("Garden", (fx(755) + W) / 2, fy(310))
msp.add_linear_dim(base=(0, -2.5), p1=(0, 0), p2=(W, 0), dxfattribs={"layer": "DIMS"}).render()
msp.add_linear_dim(base=(-2.5, 0), p1=(0, 0), p2=(0, D), angle=90, dxfattribs={"layer": "DIMS"}).render()
label("ROOFTOP PLAN · 45 ft x 25 ft · sizes approximate, verify on site", W / 2, -5, 0.7)
doc.saveas(out + "rooftop-plan.dxf")

print(len(parts), "parts; bounds (ft):", [round(v, 1) for v in np.array(scene.bounds).flatten() / FT])
