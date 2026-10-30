# Day 4 · Skin tones and the skin-tone line (30 Oct)

## Lesson (10 min)
1. **Why skin matters most:** viewers forgive a slightly wrong wall colour, never a wrong face. A green, grey or orange face looks "off" even to people who know nothing about colour.
2. **The skin-tone line:** on the **Vectorscope YUV**, the thin line between yellow and red (about the 11 o'clock direction). Every human skin colour, light or dark, sits **on or near this line**. Darker skin is the same direction, just lower in brightness and often a little further from the centre.
3. **How to read it for one face only:** a full frame mixes the wall, the clothes and the face. Isolate the face:
   - Add a **crop** effect or a **mask** (Lumetri doesn't need it; use the Crop effect temporarily) so only the face shows, **or**
   - in Lumetri **HSL Secondary**, use the eyedropper on the skin and tick **"Color/Gray"** to see only the selected skin.
4. **What the trace tells you:**
   - Trace **left of the line** (towards yellow/green): face too yellow/green. Fix with **Tint** towards magenta, or Temperature a touch cooler.
   - Trace **right of the line** (towards red/magenta): face too red/pink. Tint towards green.
   - Trace **long** (far from centre): too saturated, looks orange. Lower Saturation or Vibrance.
   - Trace **tiny** in the centre: skin looks grey or sick. Add a little Saturation.
5. **Bangladeshi skin under mixed light:** tube lights push skin green; tungsten and candle push it orange. The line is your neutral judge either way.

## Task (30–40 min)
1. Use the same 3 Banns clips (church, outdoors, restaurant). Duplicate the Day 3 sequence.
2. On each clip, temporarily crop to one face and look at the vectorscope. Write down: on the line, left, or right? Long or short?
3. Correct each face onto the line using only **Temperature, Tint and Saturation** in Basic Correction. Remove the crop and check the whole frame still looks natural.
4. Pick the clip where two people with different skin tones are in the same shot. Make sure **both** sit near the line, not just one.
5. Export a before/after still per clip (Shift+E).

**If Premiere is still crashing:** do the same task in DaVinci Resolve (free): Color page → Scopes → Vectorscope, and turn on **"Show Skin Tone Indicator"** in the scope's options. The idea is identical.

## Check yourself
- [ ] Every face sits on or very near the skin-tone line
- [ ] No face looks orange (too long) or grey (too short)
- [ ] Two different people in one shot both look natural
- [ ] Whites from Day 3 are still white after your changes

**Send the 3 before/after stills in chat.** Tomorrow is Day 5: contrast and saturation without clipping.
