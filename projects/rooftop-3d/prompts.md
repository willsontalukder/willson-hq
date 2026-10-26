# Rooftop 3D · prompts

Layout: main rooftop 45 ft × 25 ft (1,125 sq ft) + 16 ft × 7.5 ft (120 sq ft) = 1,245 sq ft.
Read from the plan (approximate, measured from the drawing at 45 × 25 ft):

| Zone | Where | Approx. size |
|---|---|---|
| Open floor | left edge strip and bottom strip | ~10 ft wide (left), ~6 ft deep (bottom) |
| Service block | top-left: staircase room, entrance space, closet, vanity sink, bathroom | ~17 × 5 ft |
| Pool | below the service block, oval, with 2 round planters at its top-left corner | pool ~9 × 11.5 ft inside a ~10 × 15 ft deck |
| Service strip | right of the pool: wooden steps, outdoor sink counter, BBQ grill | ~2 ft wide |
| Awning | vertical shaded walkway right of the strip, rounded bottom corner | ~5 × 19 ft |
| Lounge | top-right: two round tables with 6 chairs each | ~18 × 11 ft |
| Garden | bottom-right, L-shaped lawn | ~6.5 ft wide + ~13 × 6 ft |

The extra 16 × 7.5 ft area isn't drawn on the plan; the prompts assume it is the staircase/entrance block.

## 1 · Isometric 3D render (upload the plan with this prompt)
```
Use the uploaded floor plan exactly as the layout. Create a photorealistic 3D isometric render, seen from above at a 45-degree angle, of a modern residential rooftop in Dhaka, Bangladesh, 45 ft by 25 ft, surrounded by a 3.5 ft white parapet wall with a slim glass railing on top.
Top-left: a small white concrete service block with the staircase room, an entrance door, a closet, an outdoor vanity sink and a bathroom.
Below it: an oval swimming pool with turquoise water and a grey stone coping, set in a warm teak wood deck, with two round concrete planters holding small palms at its top-left corner.
Right of the pool: a narrow service strip with a few wooden steps, an outdoor stone sink counter and a built-in charcoal BBQ grill.
Next to it: a long shaded walkway under a beige fabric awning on slim black steel posts, with a rounded corner at the bottom.
Top-right: an open lounge area with light grey porcelain tiles and two round white tables, each with six rattan chairs.
Bottom-right: an L-shaped green lawn garden with low shrubs and flowering plants along the edges.
Everything else: light grey anti-slip floor tiles.
Soft late-afternoon sunlight, realistic shadows, Dhaka city buildings softly blurred in the background, architectural visualization quality, clean and minimal, no people, no text, no labels.
```

## 2 · Eye-level view: lounge looking toward the pool
```
Photorealistic architectural render of a modern rooftop in Dhaka at golden hour, eye-level view standing in the lounge area. In the foreground two round white tables with six rattan chairs each on light grey porcelain tiles. In the middle ground a beige fabric awning on slim black steel posts shades a walkway, and beyond it an oval turquoise swimming pool with a teak wood deck and potted palms. To the right a green lawn garden with flowering shrubs. White parapet with glass railing, warm string lights starting to glow, Dhaka skyline in soft haze. Realistic materials, natural light, no people, no text.
```

## 3 · Night view: pool and BBQ
```
Photorealistic night render of a modern Dhaka rooftop: an oval swimming pool glowing with underwater lights, teak wood deck, a built-in BBQ grill and stone sink counter beside it under a beige fabric awning lit by warm LED strips, round lounge tables with rattan chairs under festoon string lights, a small green lawn garden with uplighting on the plants, white parapet with glass railing, city lights of Dhaka in the background. Cinematic, cosy, realistic, no people, no text.
```

## 4 · Drone flythrough video (Google Flow / Veo)
```
Smooth cinematic drone shot slowly orbiting a modern rooftop in Dhaka at golden hour: an oval turquoise swimming pool with a teak wood deck and potted palms, a small white service block with staircase and bathroom, a built-in BBQ grill and stone sink under a beige fabric awning on black steel posts, a lounge with two round white tables and rattan chairs, and an L-shaped green lawn garden, all surrounded by a white parapet with a glass railing. Dhaka skyline in warm haze behind. Soft ambient city sound and birds. Realistic, 16:9, no people, no on-screen text.
```

## Notes
- AI image tools make a nice visual but won't keep exact measurements. For an accurate, editable 3D model with real dimensions, build it in SketchUp Free or Blender from the table above, then use prompt 1 to restyle a screenshot of it.
- If the AI moves zones around, reply: "Keep the layout exactly like the uploaded plan: service block and pool on the left, awning walkway in the middle, lounge top-right, garden bottom-right."

## Architect model files (model/)
- `rooftop-plan.dxf`: 2D plan in feet with layers (AutoCAD, SketchUp, Revit import)
- `rooftop.dae`: 3D massing model (SketchUp: File → Import → COLLADA), metres
- `rooftop.obj`: 3D model, metres (SketchUp 2021+, Blender, Rhino)
- `rooftop.glb`: 3D model for web/phone viewers, metres
- Rebuild with `python3 build_model.py` (needs trimesh, ezdxf, scipy, pycollada).
