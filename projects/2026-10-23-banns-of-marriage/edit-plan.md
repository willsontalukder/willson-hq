# Edit Plan · Banns of Marriage · Edit 24 Oct to 6 Nov 2026

Owner: Bartholomew (edit and colour) · Editor: Frank, solo · DaVinci Resolve on the ASUS TUF laptop

Deliverables: **3–5 min highlight film** (target 4:00–4:20) and a **full ceremony film** (real time, about 40–55 min),
plus a **9:16 Instagram teaser** and a **small WhatsApp file** of the highlight film.

Source footage, as planned in `shot-list.md` and `audio-plan.md`:
- Sony A7C, **4K UHD 25p**, XAVC S 100 Mbps, 8-bit 4:2:0 long-GOP, **HLG3 gamma, Pro colour mode**
- **1080p 100p** XAVC S HD for slow motion, conformed to 25p (4x slower)
- DJI Mic Mini 2 into the camera's mic input (the camera audio track), plus a **phone backup recording** near the lectern and at the head table
- Possibly a phone locked-off wide of the ceremony (25 fps), if Frank managed to set one up

**Assumptions (Frank, correct any of these):**
- **Laptop:** model unknown. This plan assumes a **mid-range ASUS TUF with an NVIDIA RTX laptop GPU (RTX 4050/4060 class, 6–8 GB VRAM), 16 GB RAM, a 512 GB–1 TB NVMe SSD**, running Windows. With 8 GB RAM or a GTX card, use quarter-resolution proxies and expect slower renders.
- **Resolve version:** this plan assumes the **free version** of Resolve 19 or 20. Where DaVinci Resolve Studio would help (GPU decoding of H.264, noise reduction, film grain, Super Scale, transcription), the plan says so.
- **Storage:** the event will be about 2–3 hours of footage, roughly 100–140 GB. Keep the original media on an **external SSD** and the cache and proxies on the internal NVMe.
- **Couple's names and the church name are still unknown.** Titles stay as placeholders until Frank provides them.

---

## 1. Project setup in Resolve

### 1.1 Laptop prep (do once, about 10 minutes)
1. Plug the laptop into mains power for every edit session. On battery, the RTX GPU throttles hard.
2. Windows: Settings > System > Power > **Best performance**. In Armoury Crate, set the **Performance** or **Turbo** mode and, if available, the **GPU mode to Ultimate/dGPU only** (or Standard, never Eco).
3. Install the latest **NVIDIA Studio driver**. Windows Settings > Display > Graphics > add `Resolve.exe` > **High performance**.
4. Resolve > Preferences > Memory and GPU: GPU processing mode **CUDA**, GPU selection **NVIDIA (manual)**. Leave Resolve's memory at its default (about 75% of RAM).
5. Close the browser and any sync apps (OneDrive, Google Drive) while editing.

### 1.2 Folder structure on the external SSD
```
2026-10-23_banns/
  01_camera/        A7C card copies, untouched (PRIVATE/M4ROOT/CLIP/...)
  02_audio/         camera WAV exports (if any), phone recordings, room tone
  03_phone-video/   phone locked-off wide (if shot)
  04_music/         licensed tracks + licence PDFs
  05_graphics/      titles, logo
  06_exports/       highlight, ceremony, teaser, whatsapp
  07_project/       Resolve .drp backups
```
Keep the card structure intact inside `01_camera` (copy the whole card folder) so the XML metadata, including gyro data, stays with the clips.
Cache and proxies go on the internal NVMe in `D:\ResolveCache\banns\` (or `C:\` if there is only one drive).

### 1.3 New project and settings (File > Project Settings)
Create the project **`2026-10-23 Banns of Marriage`**. Set these **before importing anything**, because the timeline frame rate cannot be changed after media is added.

**Master Settings**
- Timeline resolution: **3840 x 2160 Ultra HD**
- Pixel aspect ratio: Square
- Timeline frame rate: **25**
- Playback frame rate: **25**
- Video monitoring: leave as is (no external monitor)
- Optimized media and render cache:
  - Proxy media resolution: **Choose automatically** (on a slow laptop: Quarter)
  - Proxy media format: **DNxHR LB** (about 16 GB per hour at 1080p, decodes easily on CPU)
  - Optimized media format: DNxHR LB (only used if you choose optimized media instead of proxies)
  - Render cache format: **DNxHR LB**
  - **Enable background caching after 5 seconds**: on
- Working folders: Proxy generation location and Cache files location > `D:\ResolveCache\banns\`

**Image Scaling**
- Input scaling: **Scale full frame with crop** (this lets the 1080p slow motion fill the UHD frame; it is a 2x upscale, so use those shots briefly and avoid crops on them)
- Mismatched resolution files: Scale full frame with crop

**Color Management** (see 1.5): Color science **DaVinci YRGB**, Timeline color space **Rec.709 Gamma 2.4**, Output color space **Rec.709 Gamma 2.4**.

**Fairlight**: timeline sample rate 48 kHz. Enable **Loudness** metering, target **-14 LUFS** (YouTube standard), true peak -1 dBTP.

**General Options**: Conform options > Assist using reel names from > Source clip file pathname. Auto save **every 5 minutes**, 10 versions.

**Save it as a template:** at the top right of Project Settings, click the three-dot menu > **Save Current Settings as Preset**, name it `WFT 4K25 HLG Laptop`. On future projects, load it and click **Save** before importing. (Optionally also set it as the user default.)

### 1.4 Import, proxies and performance
1. **Media page**: in the Media Storage panel, browse to `01_camera`. Drag the card folders into the Media Pool. Resolve reads XAVC S directly; do not import from the camera with Sony software first.
2. **Bins:**
   - `01 Church 4K`, `02 Church SM 100p`, `03 Lunch 4K`, `04 Lunch SM 100p`
   - `05 Audio – phone`, `06 Audio – room tone`, `07 Phone wide`, `08 Music`, `09 Graphics`
   - `10 Timelines` (selects, stringouts, edits)
   - Smart bins help: Smart Bin > `Frame rate = 100` collects every slow-motion clip automatically.
3. **Conform the slow motion** before cutting with it: select every 100p clip > right-click > **Clip Attributes** > Video > Video Frame Rate **25** > OK. Each clip now plays 4x slower. Its audio becomes useless, so mute it in the edit.
4. **Generate proxies**: select all camera clips (4K and 100p) > right-click > **Generate Proxy Media**. Expect about 1–2 hours for 2–3 hours of footage; run it overnight on Sat 24 Oct.
5. Playback menu > **Proxy Handling > Prefer Proxies**. Turn it off (**Prefer Camera Originals**) for colour work and before every export. Resolve renders from the originals by default (Deliver > Advanced > "Use proxy media" stays unticked).
6. Playback menu > **Render Cache > Smart**. Heavy grades and titles cache in the background.
7. Playback menu > **Timeline Proxy Resolution > Half** while editing. This is a second, cheap speed boost.
8. **Resolve Studio only:** Preferences > Decode Options > enable **Use NVIDIA (or GPU) for H.264/HEVC decoding**. Long-GOP XAVC S then plays without proxies on most RTX laptops, but proxies are still kinder to the fan and the battery.
9. **Why proxies, not optimized media:** proxies are separate files you can delete or regenerate, they relink automatically, and you can move them with the project. Optimized media works too, but it lives in the cache and is harder to manage.

### 1.5 Colour management for HLG3 (node-based, DaVinci YRGB)
The footage is **HLG3 gamma with Pro colour mode**. Pro colour is close to Rec.709 primaries; it is *not* BT.2020. So the input transform is **Rec.709 primaries with HLG gamma**, then everything is graded in a wide working space and converted to Rec.709 Gamma 2.4 at the end. This gives predictable highlight roll-off and easy shot matching.

> **Check first:** open one clip and read the metadata, or check the camera's picture profile. If **Color Mode was left on BT.2020** (the HLG3 default), set the input colour space to **Rec.2020** instead of Rec.709 below. Everything else stays the same.

**Clip-level nodes** (apply via a **Group**: select all camera clips on the Color page > right-click > Add into a New Group > name it `A7C HLG3`):

*Group Pre-Clip* (one node, shared by every clip):
- Node 1, **Color Space Transform**:
  - Input color space: **Rec.709** (or Rec.2020; see the box above) · Input gamma: **Rec.2100 HLG**
  - Output color space: **DaVinci Wide Gamut** · Output gamma: **DaVinci Intermediate**
  - Tone mapping: None · Gamut mapping: None

*Clip level* (per shot, in DaVinci Wide Gamut / Intermediate, so Offset and the HDR wheels behave correctly):
- Node 2 `EXP`: exposure with **Offset** (or the HDR palette's Exposure); target faces at about 60–70 IRE on the waveform after the output transform
- Node 3 `WB`: white balance with the **HDR palette > Temp/Tint**, or Offset R/G/B; balance on a white shirt, the altar cloth or the eye whites
- Node 4 `CONTRAST`: contrast and pivot (pivot about 0.336 for DaVinci Intermediate) and saturation
- Node 5 `FIX`: (optional) power window on faces, de-flicker, or Qualifier for a colour cast

*Group Post-Clip*: Node 6 `MATCH`: small venue-wide trims (church vs restaurant)

*Timeline level* (Color page > node mode **Timeline**):
- Node 7 `LOOK`: the creative grade, applied once to the whole timeline (see 1.6)
- Node 8 **Color Space Transform** (output):
  - Input DaVinci Wide Gamut / DaVinci Intermediate
  - Output color space **Rec.709** · Output gamma **Gamma 2.4**
  - Tone mapping: **DaVinci** (Adaptation 9; enable **Custom max input**, 1000 nits) · Gamut mapping: **Saturation Compression**

Save the whole node setup as a **PowerGrade** (Gallery > PowerGrades > right-click > Add) named `A7C HLG3 > DWG > 709` and reuse it on every Sony HLG job.

**Why not Resolve Color Management (RCM)?** It works, but in RCM the input list labels "Rec.2100 HLG" as Rec.2020 primaries, which is wrong for Pro colour mode. The explicit CST nodes avoid that trap and are easy to see and debug.

**Phone wide footage** (if shot): it is Rec.709 SDR, often HDR/HLG on newer iPhones. Check its metadata. For SDR, set its own group with a CST from Rec.709 / Gamma 2.4 into DWG / DaVinci Intermediate. For iPhone HLG, use Rec.2020 / Rec.2100 HLG as the input.

### 1.6 Colour order and the 8-bit banding watch
1. **Correct first, then grade.** Balance every shot (exposure, white balance, contrast) so faces match across the church and the restaurant. Only then add the look.
2. **Matching:** start from the vows hero shot (85mm on the couple). Grab a still (right-click the viewer > Grab Still), then use **split-screen wipe** to match the other shots to it. Skin tone should sit on the **vectorscope skin line**.
3. **Mixed light in the church** (window daylight and tungsten): correct for faces, not windows. If one side of a face is blue, use a soft power window on faces and warm only that side slightly.
4. **The look** (suggested; Frank's call): warm and soft. Lift the shadows slightly, cream highlights, saturation 90–95% in the greens and blues, faces natural. No teal and orange; it is a church and a family lunch.
5. **Banding risk (8-bit, 4:2:0):** watch the white walls, ceilings, window glow, smooth backdrops and skies.
   - Keep corrections gentle. Avoid heavy Qualifier keys on walls and avoid big saturation boosts in flat areas.
   - Check with **Scopes > Waveform** and zoom the viewer to 200% on gradients.
   - If banding shows, back off contrast, reduce the curve slope in that range, or add a soft fine noise layer. **Film Grain** and **Noise Reduction** are Studio-only; in the free version keep the grade light and export at a higher bitrate (banding gets worse when the encoder starves).
   - High-ISO (3200–6400) shots will be noisy. In the free version, avoid lifting their shadows. In Studio, use Temporal NR (Frames 2, Better, Luma/Chroma 8–12) on those shots only.
6. **Flicker:** if any LED flickers despite the 1/50 shutter, Studio has the **Deflicker** OFX. In the free version, cut away from it or crop it out.
7. **Shake:** the A7C writes gyro data. **Gyroflow** (free) can stabilize from it, but results with IBIS on are mixed. Try it only on hero shots that wobble; otherwise use Resolve's **Stabilizer** (Color page > Tracker > Stabilizer, mode Similarity, Smooth 0.3–0.5, Zoom on).

---

## 2. Day-by-day schedule (Sat 24 Oct to Fri 6 Nov)

About 4–6 hours of edit time per working day. Friday is the weekend in Bangladesh; **Fri 30 Oct** is a rest day, and **Fri 6 Nov** is delivery only.

| Day | Date | Work | Done when |
|---|---|---|---|
| 1 | **Sat 24 Oct** | **Backup and ingest.** Confirm two copies exist (laptop/external SSD + a second drive). Create the project from the template, import, sort bins, conform the 100p clips, generate proxies overnight. Copy the phone audio. Note: matthias owns the backup check. | 2 verified copies; proxies rendering; all clips in bins |
| 2 | **Sun 25 Oct** | **Watch everything and select.** Play through all footage once. Mark **favourites** (F key: Flag) and add **markers** at the best lines (vows, rings, the banns reading, speech laughs). Build a `SELECTS` timeline of the best 15–20 minutes. Transcribe or write down the key spoken lines with timecodes. Shortlist 3–5 licensed music tracks with james-the-less. | Selects timeline + list of key lines + music shortlist |
| 3 | **Mon 26 Oct** | **Full ceremony: sync and assembly.** Auto-sync the camera and phone audio (section 4). Lay the whole ceremony in order on one timeline with continuous audio. | Ceremony assembly, in sync end to end |
| 4 | **Tue 27 Oct** | **Full ceremony: cover the gaps and trim.** Cover camera stops, jump cuts and focus misses with b-roll and reactions. Trim the dead time before the start and after the end. Add chapter markers. | Ceremony fine cut v1 (picture locked unless QC finds problems) |
| 5 | **Wed 28 Oct** | **Highlight: the "radio edit".** Build the audio story first: the best vow lines, the banns, one or two speech lines, then lay the music under them. Lock the music track and its edit points (cut the music to length). | Highlight audio spine + music locked |
| 6 | **Thu 29 Oct** | **Highlight: picture cut v1.** Put pictures on the audio spine beat by beat (section 3). Cut to the music; use slow motion for the arrival, exit, cake and food. | Highlight v1, about 4:30–5:00 |
| – | Fri 30 Oct | **Rest.** Optional: watch highlight v1 once on a phone, with fresh eyes, and write notes. Don't edit. | Notes list |
| 7 | **Sat 31 Oct** | **Highlight v2: rhythm and cutting down.** Apply the notes. Cut anything that doesn't serve the story; aim for 4:00–4:20. Cut the **Instagram 9:16 teaser** (30–45 s) from the highlight. | Highlight picture lock + teaser cut |
| 8 | **Sun 1 Nov** | **Colour.** Switch to camera originals. Apply the PowerGrade; correct and match all shots in both films (the films share clips, so grade once in the highlight and copy grades across with **Shift+=** / ColorTrace, or use the same groups). Apply the look. Check for banding. | Both films graded |
| 9 | **Mon 2 Nov** | **Sound mix** (with james-the-less). Dialogue clean-up, music ducking, room tone under the cuts, loudness to -14 LUFS. Ceremony: smooth the level between officiant, readers and vows. | Both mixes at target loudness |
| 10 | **Tue 3 Nov** | **Titles and the first exports.** Opening title and end card (couple's names, date, church: **need these from Frank**). Export v1 of every deliverable (section 5). **Hand to thomas for QC.** | v1 files + QC request |
| 11 | **Wed 4 Nov** | **QC fixes.** Fix thomas's notes (sync slips, spelling, loudness, black frames, flashes). Frank watches both films in full. | QC passed; Frank's notes in |
| 12 | **Thu 5 Nov** | **Final exports and archive.** Final renders; play every file through once; upload privately (unlisted/private) **only after Frank approves**. Back up the project (.drp), exports, music licences and graded media to two drives. | Final files + archive done |
| 13 | **Fri 6 Nov** | **Delivery**: Frank sends the links and the WhatsApp file to the couple (his approval and his send). Post the teaser only if Frank and the couple agree. | Delivered |

**Buffer:** Wed 4 Nov has slack. If colour or audio runs long, push the exports to Wed and keep Thu as the safety day.
**If Frank's time is short:** deliver the highlight film on Fri 6 Nov and the full ceremony a few days later. The highlight matters most to the couple.

---

## 3. Highlight film structure (target 4:00–4:20)

**Story:** two families come together; the vows are the heart, the lunch is the celebration. **The couple's own words carry the film:** vows first, then the speeches. Music supports them and never fights them.

| # | Beat | Time (approx.) | Pictures | Sound |
|---|---|---|---|---|
| 1 | **Cold open** | 0:00–0:15 | Black, then one detail (rings, the couple's hands) | **One vow line** in the clear, no music, or the softest room tone. Hook the viewer with their voice. |
| 2 | **Place and morning** | 0:15–0:45 | Church exterior and sign (shot 1), interior wide (2), details: Bible, flowers, programme (3). **Title card** at about 0:30 (names, date) | Music in (gentle intro), low |
| 3 | **Gathering and arrival** | 0:45–1:15 | Guests arriving, family, the couple walking in (**SM**, shot 4) | Music builds. A short real sound (bells, organ, door) if available. |
| 4 | **The ceremony** | 1:15–2:20 | Officiant reading the banns (5), readers (6), **vows** close-ups alternating bride and groom (7), **rings** (8), two-shot (9), family reactions (10, **SM** tears/smiles), congregation (11) | **Vow audio carries this section.** Music ducks to a bed (about -20 to -24 dB under the voice) or drops out for the key line. Let the best line land, then 1–2 s of silence or a held breath. |
| 5 | **Release** | 2:20–2:45 | Signing/blessing (12), **exit SM** (13), guests greeting, group photo laughs (14) | Music swells: the first big lift. Cut on the beat. |
| 6 | **To the lunch** | 2:45–3:05 | Lift and entrance (15), room wide, table details (16), food (**SM**, 17) | Music continues; the energy is lighter |
| 7 | **The celebration** | 3:05–3:45 | **Speech** (19): one funny line, one sincere line. Reactions (20: couple laughing). Cake and the cut (18, **SM**). Toasts (22, **SM**) | **Speech audio carries this section**, music ducked under it. Let laughter breathe. |
| 8 | **Close** | 3:45–4:15 | Candid couple at the table (21), group photo (23), couple leaving (**SM**, 24) | Music resolves. A final short vow line or blessing as the last words, then the music ending. |
| 9 | **End card** | 4:15–4:25 | Names · Banns of Marriage · 23 October 2026 · a small "Filmed by Frank Willson Talukder" | Music tail out |

**Cutting rules for this film**
- **Select takes:** the best performance first (emotion and clear words), then focus, then steadiness. A slightly soft shot with a real tear beats a sharp, empty one.
- **Rhythm:** wide shots 3–5 s, close-ups 2–3 s, slow motion 3–6 s (it reads slower). Cut on the music's beat in beats 2, 5 and 8; cut on speech pauses and reactions in beats 4 and 7.
- **Hold the moments:** do not cut away during a vow line; cut on the breath after it.
- **Cut everything that doesn't serve the story:** repeated detail shots, guests with no connection to the couple, shaky walking shots, anything you have to explain.
- **Speed ramps:** none. Real-time and conformed slow motion only; it suits the occasion.
- **Audio from 100p clips is dropped.** Use room tone or the music under slow motion; add natural sound (applause, laughter) from the 25p clips if needed.

**Music: licensed only**
- Choose **one track** (or two with a clear change at the lunch, beat 6). A tempo of about 70–95 BPM suits the ceremony; a lighter, warmer second track for the lunch.
- Licensed sources: **Artlist, Musicbed, Epidemic Sound, Soundstripe**, or the **YouTube Audio Library** (free; check each track's attribution terms). james-the-less picks and checks the licence. Make sure the licence covers **YouTube, Instagram and private sharing** and, for a subscription library, that the channel is **whitelisted for Content ID** before upload.
- Save the licence PDF or certificate in `04_music/` next to the track.
- **Never commercial pop/film songs**, even short clips: they get blocked or muted on YouTube and Instagram.
- **Hymns and music in the church:** traditional hymns are public domain, so a live recording is fine. A modern worship song, or a recorded track played over the PA, may trigger Content ID. Keep that music short and low, or cover it with the licensed track.

---

## 4. Full ceremony film

**Goal:** a complete, watchable record of the ceremony for the couple and the family, from the entrance to the exit, with clean continuous sound. Real time, minus dead time. Expect about 40–55 minutes.

### 4.1 Audio sources and priority
| Source | Best for | Notes |
|---|---|---|
| DJI Mic Mini 2 on the groom (camera track) | **Vows**, the couple's responses | The cleanest sound for the core moment; only exists while the camera records |
| DJI TX2 on the officiant/lectern (if there were 2 TX) | Banns, readings, sermon | Mixed into the same camera track, or the second channel if recorded split |
| **Phone near the lectern** | Everything, **continuously** from 09:50 | **The spine.** It covers every camera stop. |
| Camera on-board mic | Room, singing, applause | Only if the receiver dropped out; check the track layout |

### 4.2 Sync, step by step
1. **Check the camera track layout:** in the Media Pool, right-click a clip > Clip Attributes > Audio. See whether the receiver recorded stereo (TX1 left, TX2 right) or mono-mix. Set the channel format accordingly (two mono channels if split).
2. **Build the spine:** new timeline `CEREMONY FULL`. Put the **phone recording on A2**, starting at 00:00. It runs continuously, so it defines the timeline.
3. **Auto-sync the camera clips to it:** select the phone file and all the church camera clips in the Media Pool > right-click > **Auto Sync Audio > Based on Waveform and Append Tracks**. The camera clips now carry the phone audio as an extra track.
4. **Place the clips:** drag the synced camera clips onto V1/A1 at the right point on the phone spine. Line up the waveforms by eye (zoom in on the clap or a hard consonant). The claps at each camera restart make this quick.
5. **Drift check:** the phone and camera clocks drift slightly over long takes (often 1–2 frames per 10–20 minutes). Check sync at the **start and end of every long camera clip**. If it drifts, cut the phone audio at a pause every 10 minutes and nudge it back into sync (alt/option + comma/period moves a clip 1 frame). Use a 2-frame crossfade at each cut.
6. **Lock** the tracks once synced (padlock icon) before cutting picture.
7. **Sample rate:** the phone may record at 44.1 kHz or in compressed formats. Resolve converts it; if it sounds wrong, convert the phone file to 48 kHz WAV first.

### 4.3 Picture: single camera, so cover the cuts with b-roll
- **Main angle:** the 85mm static shots of the officiant and the couple, and the 24mm wide from the back (shot 2).
- **Camera stops** (battery or card swaps, lens changes): the phone audio continues. Cover the gap with, in order of preference:
  1. The **phone locked-off wide** (if shot), synced the same way. This is the ideal safety angle.
  2. **B-roll from the same moment:** congregation (11), family reactions (10), details (3), the interior wide (2).
  3. **Exterior/detail shots** shot before or after (1, 3) with a slow, gentle push-in (Inspector > Zoom keyframes, 100% to 105%).
  4. Last resort: a slow **dissolve to black** and back, only for long gaps in non-key moments.
- **Jump cuts** (where you trimmed inside a static shot): put a 2–4 s reaction or detail shot over the cut; the audio continues underneath. Use reactions from the same section, so the light and positions match.
- **Focus misses and shaky moments:** cover them the same way. Don't cover the vows or the rings unless there is truly nothing else. A slightly soft real moment is better than b-roll.
- **Never** cover the vows or ring exchange with unrelated b-roll. If the camera missed them, use the phone wide or hold on the couple's two-shot.
- **Dead time:** trim the waiting before the entrance and long pauses (people moving to the lectern) with the audio crossfaded (5–10 frames) and covered with b-roll. Keep the liturgy intact; don't shorten readings, prayers or the banns.
- **Slow motion:** not used in the ceremony film, except in a short opening and closing (the entrance and the exit).
- **Structure:** a 20–30 s opening (exterior, details, title), the ceremony in real time, then a 30–60 s closing (exit, greetings, group photo) under licensed music, then the end card.

### 4.4 Ceremony sound mix
- Pick the best source line by line: the **groom's lav for vows**, the lectern TX or the phone for the officiant and readers. Crossfade between sources over 5–10 frames; never play two sources together at full level (it causes phasing/echo).
- Fairlight: high-pass at 80–100 Hz on dialogue, a gentle compressor (ratio 2:1 to 3:1), and **Voice Isolation** in Studio if there is fan/AC noise (Fairlight FX Noise Reduction in the free version, used lightly).
- Lay the **room tone** recording under every audio cut so silence doesn't drop out.
- Target **-16 to -14 LUFS integrated**, true peak no higher than **-1 dBTP**. Let singing and applause be naturally loud, but limit them.

### 4.5 Chapters
Add markers and, for the YouTube description, write chapter times: `00:00 Opening`, `Entrance`, `Readings`, `The Banns`, `Vows`, `Rings`, `Blessing`, `Exit`. YouTube needs the first chapter at 00:00 and at least three chapters of 10 s or more.

---

## 5. Export specs (Deliver page)

**For every export:**
- **Playback > Proxy Handling > Prefer Camera Originals** (and the render uses originals: Deliver > Advanced > "Use proxy media" unticked).
- Audio is rendered from the Fairlight mix at **-14 LUFS integrated, -1 dBTP**, measured with the Fairlight loudness meter on the full timeline.
- Colour tags: **Rec.709 / Gamma 2.4 (Rec.709)**, data levels **Auto/Video**. (On a Mac, QuickTime shows a slightly washed-out picture with these tags; that is normal and YouTube is fine.)
- Encoder: choose **NVIDIA** if it appears in the encoder list; otherwise **Native**. Quality: **Restrict to** the bitrate shown. Use **Multi-pass encode** if offered.
- Play each finished file all the way through once before it goes anywhere, then send it to thomas for QC.

### 5.1 Highlight film: YouTube / private link master
| Setting | Value |
|---|---|
| Format / codec | **MP4 / H.264** (High profile) |
| Resolution | **3840 x 2160** |
| Frame rate | **25** |
| Bitrate | **50 Mbps** (YouTube recommends 35–45 Mbps for 4K SDR at 24–30 fps; the extra headroom protects against banding) |
| Keyframes | Automatic |
| Audio | **AAC, 320 kbps, 48 kHz, stereo**; -14 LUFS, -1 dBTP |
| File size | About 1.6 GB for 4:20 |
| Upload | YouTube **Unlisted** (or Vimeo with a password), after Frank approves. YouTube shows the 4K version a while after HD finishes processing. |
| File name | `2026-10-23_Banns_Highlight_4K_v1.mp4` |

**Archive master** (keep, not for sharing): QuickTime, **DNxHR HQX**, 3840 x 2160, 25p, Linear PCM 24-bit 48 kHz. About 20–25 GB for 4:20. If the drive is tight, skip this and archive the project, media and music instead.

### 5.2 Full ceremony film: YouTube / private link
| Setting | Value |
|---|---|
| Format / codec | MP4 / H.264 (High profile) |
| Resolution | **1920 x 1080** (default chosen: about 9 GB per hour instead of about 22 GB at 4K, so it uploads overnight on a typical Dhaka connection; use 4K at 45 Mbps if the upload speed allows) |
| Frame rate | 25 |
| Bitrate | **20 Mbps** |
| Audio | AAC, 320 kbps, 48 kHz, stereo; -16 to -14 LUFS, -1 dBTP |
| Upload | YouTube **Unlisted**, after Frank approves; add the chapter list to the description |
| File name | `2026-10-23_Banns_Ceremony_1080p_v1.mp4` |

### 5.3 Instagram Reels / TikTok 9:16 teaser (30–45 s)
1. Duplicate the highlight timeline > rename `TEASER 9x16`. Timeline Settings (right-click the timeline > Timelines > Timeline Settings): untick "Use project settings", set **1080 x 1920**, 25 fps, Mismatched resolution: **Scale full frame with crop**.
2. Recut it short: cold-open vow line > arrival SM > vows > exit SM > cake/laugh > names card. Cut to the music; aim for 30–45 s (Reels and TikTok both allow longer, but shorter keeps people watching).
3. **Reframe** every shot: in the Inspector, adjust Position X (Resolve Studio: **Smart Reframe** does it automatically). Prefer **4K shots**: they give an almost-native 1215 x 2160 crop. The 1080p slow motion only gives a 607 x 1080 crop, upscaled about 1.8x, so it goes soft; use it briefly or skip it.
4. **Safe zones:** keep text and faces out of the **top 250 px and bottom 400 px** (the app's buttons and captions sit there) and about 60 px from each side. Burn-in captions for the vow line: many people watch on mute.

| Setting | Value |
|---|---|
| Format / codec | MP4 / H.264 (High profile) |
| Resolution | **1080 x 1920 (9:16)** |
| Frame rate | 25 |
| Bitrate | **16 Mbps** (Instagram and TikTok recompress; a clean source helps) |
| Audio | AAC, 320 kbps, 48 kHz, stereo; **-14 LUFS**, -1 dBTP |
| Length | 30–45 s |
| Music | The **same licensed track**, if the licence covers Instagram and TikTok. Otherwise use Instagram's in-app music: export without music and add it in the app. |
| Posting | Only if **Frank and the couple agree**; jude handles the caption. Not before the couple has seen the highlight film. |
| File name | `2026-10-23_Banns_Teaser_9x16_v1.mp4` |

### 5.4 WhatsApp-friendly highlight
For family who will watch on their phones and forward it.

| Setting | Value |
|---|---|
| Format / codec | MP4 / **H.264 Main** profile (plays on old phones) |
| Resolution | **1920 x 1080** |
| Frame rate | 25 |
| Bitrate | **3 Mbps** (Restrict to) |
| Audio | **AAC, 128 kbps**, 48 kHz, stereo; -14 LUFS |
| File size | **About 100 MB** for 4:20 |
| File name | `2026-10-23_Banns_Highlight_WhatsApp.mp4` |

- Sent as a **video** in WhatsApp (tap **HD** before sending), it gets recompressed but still looks fine on a phone.
- To send it **without recompression**, attach it as a **Document** instead: the recipient gets this exact file.
- If the family mostly uses mobile data, also make a **720p (1280 x 720), 1.5 Mbps** version: about 50 MB.
- **Do not WhatsApp the full ceremony.** Send the private YouTube link instead.

### 5.5 Deliver-page presets
Save each of 5.1–5.4 as a render preset (Deliver > Render Settings > three-dot menu > **Save as New Preset**): `WFT YT 4K25`, `WFT YT 1080p25`, `WFT Reel 9x16`, `WFT WhatsApp 1080`. Add all four to the Render Queue on Tue 3 Nov and render overnight.

---

## 6. Open items for Frank
- The **couple's names** and the **church name** (needed for titles by Tue 3 Nov).
- **Laptop model**, RAM and GPU (to confirm the proxy settings), and whether Resolve is **free or Studio**.
- The **colour mode** used on the day (Pro or BT.2020). Check one clip; it changes one setting in 1.5.
- Whether the **phone locked-off wide** was shot, and whether there were **1 or 2 transmitters**.
- **Music choice**: approve one track from james-the-less's shortlist (needed by Wed 28 Oct).
- Permission from the couple to post the teaser publicly (default: private only).

## 7. Suggested board tasks (for the team lead)
- `matthias`: verify the two backups and set up the Resolve template on the laptop (Sat 24 Oct, High)
- `james-the-less`: shortlist and license the music; help with the mix (shortlist by Sun 25 Oct, mix Mon 2 Nov)
- `bartholomew`: edit and colour per this plan (Sat 24 Oct – Thu 5 Nov)
- `thomas`: QC every deliverable (Tue 3 – Wed 4 Nov)
- `jude`: teaser caption and posting plan, only if the couple agrees (by Thu 5 Nov)
