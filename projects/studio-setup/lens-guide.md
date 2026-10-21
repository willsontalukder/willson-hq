# Lens Guide: 24mm vs 85mm on the Sony A7C

*For Frank, from James (DoP). Task T03. One page; keep it in the bag.*

**Assumptions.** Lens brands and max apertures aren't recorded, so this assumes **f/1.8-class primes**
(typical minimum focus: about 0.2-0.25 m for the 24mm, about 0.8 m for the 85mm). Check the barrels and
fix the numbers if yours differ. Studio notes say there are **no ND filters, tripod, gimbal or lights**, so
everything below works handheld with available light. Distances assume video (16:9, full sensor width).
**Check before relying on it:** whether 4K 30p crops the sensor on your firmware (on the A7 III, which uses the
same sensor, it does, by about 1.2x). If it does, shoot 4K 24/25p when you need the full field of view.

## The rule in one line
**24mm = put the viewer *in* the place. 85mm = make the viewer *look at* one thing.**

## Framing and distance cheat-sheet (camera to subject)

| Frame | 24mm | 85mm | Note |
|---|---|---|---|
| Tight close-up (face) | 0.4 m | 1.5 m | 24mm this close distorts faces: avoid for people |
| Close-up (head + shoulders) | 0.6 m | 2.1 m | 85mm is the flattering choice |
| Medium (waist up) | 1.1 m | 3.8 m | 24mm medium = walk-and-talk / vlog distance |
| Full body | 2.4 m | 8.5 m | 85mm full body needs a long room or outdoors |
| Small group / room | 3-4 m (covers about 4.5-6 m width) | not practical indoors | |
| Detail (rings, hands, food) | 0.25-0.3 m | 0.8 m (min focus), crop in post | Shoot 4K, crop to 1080 for about 2x "macro" |

Quick math: frame width is about **distance x 1.5** on the 24mm and **distance x 0.42** on the 85mm.

## Depth of field and compression
- **85mm @ f/1.8, 2 m:** about **6 cm** in focus. Eye-AF is mandatory; one step forward ruins it. Use f/2.8 for
  interviews (about 10 cm), and f/4 or more for two people side by side.
- **85mm @ f/1.8, 3 m:** about 13 cm. Backgrounds melt; signs and clutter vanish.
- **24mm @ f/1.8, 2 m:** about 0.7 m in focus. Background is soft but still readable (it shows *where* you are).
- **24mm zone focus:** at f/5.6, focus at **3.5 m** and everything from about 1.7 m to infinity is acceptably sharp;
  at f/8, focus at **2.5 m** and everything from about 1.2 m to infinity is. Use it for run-and-gun and crowds.
- **Compression:** the 85mm pulls the background *closer and bigger* (a sunset or skyline looms behind the subject).
  The 24mm pushes it *away* and exaggerates depth and motion; anything near the lens looks big and fast.
- **Perspective comes from distance, not the lens.** Stand back for faces (85mm). Get close for energy (24mm).

## Handheld stability
- **Stills:** shutter at least 1/focal length, then add margin for subject movement. 24mm: 1/50 is safe (IBIS can
  get 1/8 on still scenes). 85mm: **1/160 or faster** (1/250 for people moving); IBIS fixes your shake, not theirs.
  Set the IBIS focal length if the lens has no electronic contacts.
- **Video:** shutter stays at about 2x frame rate (1/50 at 24/25p, 1/60 at 30p, 1/250 at 120p). So on the 85mm you
  can't buy stability with shutter. **Brace:** elbows tucked, strap tension, lean on a wall or doorframe, sit or kneel,
  breathe out on the take, keep shots to 5-8 s. Turn SteadyShot **Active** on for the 85mm if your firmware has it
  (slight crop), but **avoid walking with the 85mm**: it amplifies every step.
- **24mm** hides shake: walk heel-to-toe with knees soft and the camera at chest height; a 20-30 cm "slider" by
  shifting your body weight looks smooth.
- **Post:** Catalyst Browse / Gyroflow-style gyro stabilization from A7C metadata is an option. Check support before
  counting on it.

## Low light
- Both lenses at f/1.8 give the same exposure. The **24mm is easier** because the shutter can drop and DoF is
  forgiving at f/1.8.
- 85mm at f/1.8 in the dark means razor-thin focus plus shake. Stop to **f/2.2-2.8** and raise ISO instead.
- A7C ISO comfort zone for video: **100-6400 clean, up to 12800 acceptable**. Expose properly; underexposed
  8-bit footage turns blotchy when you lift it in the edit. Shoot with the look baked in: **Picture Profile Off,
  Creative Style Standard (Contrast -1, Saturation 0, Sharpness -1)**, which works from ISO 100 and needs no
  grading. Log and HLG profiles record flat footage meant for grading, so Frank doesn't use them. Set custom WB
  per location, since colour can't be fixed much later (menu location of Creative Style: check on camera).
- Find light first: face toward a window, a shopfront or a phone screen; put practicals (lamps, string lights)
  in the background of 85mm shots so they turn into bokeh.

## No-ND warning (outdoors in daylight)
At 1/50 with ISO 100 in sun, f/1.8 is several stops overexposed. Without ND, either **stop down to f/8-f/11**
(you lose the 85mm's blur), shoot in **open shade / backlight**, or **bend the shutter** (1/200 or more gives a
crisp, slightly staccato look). Buying a variable ND in each lens's filter size is the single best upgrade for both
lenses (flag for matthew).

## Use by job type, plus the "one-lens day" pick

| Job | 24mm for | 85mm for | One-lens day |
|---|---|---|---|
| **Weddings / events** | Venue establishers, getting ready in tight rooms, dance floor in the crowd, group shots | Vows and speeches from the back (no intrusion), reactions, rings and details, first look | **85mm** for ceremony and speeches (you can't get close); swap to 24mm for the reception. If truly one: 85mm |
| **Documentary / interviews** | Subject in their environment, B-roll of the space, verité following | The interview A-cam (2-2.5 m, f/2.8), hands, eyes, details | **85mm** if it's interview-led; **24mm** if it's observational / following |
| **Portraits** | Environmental portrait (person small in a big place) | Classic head-and-shoulders and half-body, compressed backgrounds | **85mm** |
| **Products / food** | Flat-lay overheads, table-scape, product in context or hands-in-frame | Hero detail, texture, steam, pour, background melted to color | **85mm** for single products / plates; **24mm** for a full table or overhead |
| **Travel / B-roll** | Streets, landscapes, interiors, timelapses, POV movement | Compressed street layers, faces in crowds, distant landmarks stacked behind people | **24mm** (85mm is the second lens if you can carry it) |
| **Handheld walk-and-talk / vlog** | Everything: arm's-length vlog or 1-1.5 m walking backwards ahead of the subject | Static "cutaway" moments only; never walking | **24mm** |

## Six shot recipes

1. **Venue establisher (wedding/event)**: 24mm, f/5.6, 4-6 m from the entrance, set at chest height. Slow push in
   (3 small steps) or a 2 s tilt up from the floral details to the room. 4K 25p, 1/50.
2. **Vows from the aisle side (wedding)**: 85mm, f/2.2, 6-8 m from the couple (full-to-medium framing), braced on a
   pew end or seated. Static, eye-AF on the speaker. Rack focus to the partner's reaction on a cue.
3. **Sit-down interview A-cam (documentary)**: 85mm, f/2.8, 2-2.3 m, subject 2 m or more off the background, window
   at 45 degrees to the face. Static, braced or on a stack of books / bag, Eye-AF on (AF-C). Frame head-and-shoulders,
   eyes on the upper third.
4. **Product hero with a slow reveal (product/food)**: 85mm, f/2.0, 0.8-1 m, steam or a pour backlit by a window.
   Shoot 1080p 120p at 1/250 and slide the camera about 10 cm sideways on a table edge. Slow it down in post.
5. **Travel street layer (B-roll)**: 85mm, f/4, 15-30 m down a busy street, people crossing at different depths.
   Static, braced on a railing, 4K 25p. Compression stacks signs and crowds into one dense wall.
6. **Walk-and-talk (vlog/doc)**: 24mm, f/4 (zone-ish; Face/Eye AF-C on), 1-1.5 m in front of the subject, walking
   backwards with a spotter or along a clear path. Knees soft, SteadyShot Active, 4K 25p 1/50, DJI Mic Mini 2 on
   the subject.

## Bag rule
Leave the house with **both**. Mount the **24mm when arriving** (you're establishing and moving) and switch to the
**85mm once the subject starts talking**. Swap lenses with the camera facing down, out of wind and dust; the A7C's
single slot and exposed sensor make every swap a small risk, so plan swaps at natural breaks.
