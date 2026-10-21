# Edit Plan · Banns of Marriage · Edit 24 Oct to 6 Nov 2026

Owner: Bartholomew (edit) · Editor: Frank, solo · **Adobe Premiere Pro** on the ASUS TUF laptop

Deliverables: **3–5 min highlight film** (target 4:00–4:20) and a **full ceremony film** (real time, about 40–55 min),
plus a **9:16 Instagram teaser** and a **small WhatsApp file** of the highlight film.

Source footage, as planned in `shot-list.md` and `audio-plan.md`:
- Sony A7C, **4K UHD 25p**, XAVC S 100 Mbps, 8-bit 4:2:0 long-GOP, **Picture Profile Off, Creative Style Standard (Contrast -1, Saturation 0, Sharpness -1)**: a baked-in, ready-to-use Rec.709 look. **No grading is needed or planned.**
- **1080p 100p** XAVC S HD for slow motion, interpreted as 25 fps (4x slower)
- DJI Mic Mini 2 into the camera's mic input (the camera audio track), plus a **phone backup recording** near the lectern and at the head table
- Possibly a phone locked-off wide of the ceremony (25 fps), if Frank managed to set one up

**Assumptions (Frank, correct any of these):**
- **Laptop:** model unknown. This plan assumes a **mid-range ASUS TUF with an NVIDIA RTX laptop GPU (RTX 4050/4060 class, 6–8 GB VRAM), 16 GB RAM and a 512 GB–1 TB NVMe SSD**, running Windows 11. With 8 GB RAM or a GTX card, use the smallest proxy preset, keep playback at 1/4 resolution, and expect slower exports.
- **Premiere version:** a current Creative Cloud release (Premiere Pro 2025 or 2026). Speech to Text, Enhance Speech, Auto Reframe and Loudness Normalization on export are all included; no extra plug-ins are needed.
- **Storage:** the event will be about 2–3 hours of footage, roughly 100–140 GB. Keep the original media on an **external SSD**, and the media cache and proxies on the internal NVMe.
- **Couple's names and the church name are still unknown.** Titles stay as placeholders until Frank provides them.

---

## 1. Project setup in Premiere Pro

### 1.1 Laptop prep (do once, about 10 minutes)
1. Plug the laptop into mains power for every edit session. On battery, the RTX GPU throttles hard.
2. Windows: Settings > System > Power > **Best performance**. In Armoury Crate, set **Performance** or **Turbo** mode and, if offered, **GPU mode Ultimate/dGPU only** (or Standard, never Eco).
3. Install the latest **NVIDIA Studio driver**. Windows Settings > Display > Graphics > add `Adobe Premiere Pro.exe` and `Adobe Media Encoder.exe` > **High performance**.
4. Premiere > Edit > Preferences > **Media**: tick **Enable hardware accelerated decoding (requires restart)**, with H.264/AVC and HEVC decoding ticked. On an RTX laptop this lets long-GOP XAVC S play far more smoothly. Restart Premiere.
5. Preferences > **Media Cache**: set the location to `D:\PremiereCache\` on the internal NVMe (or `C:\` if there is only one drive). Tick **Automatically delete cache files older than 90 days**.
6. Preferences > **Memory**: RAM reserved for other applications about 4 GB (leaves about 12 GB for Adobe apps on a 16 GB laptop). Optimize rendering for **Performance**.
7. Close the browser and sync apps (OneDrive, Google Drive) while editing.

### 1.2 Folder structure on the external SSD
```
2026-10-23_banns/
  01_camera/        A7C card copies, untouched (PRIVATE/M4ROOT/CLIP/...)
  02_audio/         phone recordings, room tone
  03_phone-video/   phone locked-off wide (if shot)
  04_music/         licensed tracks + licence PDFs
  05_graphics/      titles, logo
  06_exports/       highlight, ceremony, teaser, whatsapp
  07_project/       .prproj file and Auto-Save folder
  08_proxies/       Premiere proxies (or on the internal NVMe if there is room)
```
Keep the card structure intact inside `01_camera` (copy the whole card folder) so the XML metadata stays with the clips.

### 1.3 New project (File > New > Project)
1. Name: **`2026-10-23 Banns of Marriage`**, location `07_project/`.
2. File > **Project Settings > General**: Renderer **Mercury Playback Engine GPU Acceleration (CUDA)**. Capture format and display formats: leave the defaults (Timecode, Audio Samples).
3. Project Settings > **Scratch Disks**: Captured video and audio, Video Previews, Audio Previews, Project Auto Save all **Same as Project**. (Video previews on the external SSD are fine; put them on the internal NVMe if the SSD is slow.)
4. Preferences > **Auto Save**: every **5 minutes**, maximum **20** versions, tick **Save backup project to Creative Cloud** if Frank's plan has the storage.
5. Leave **Ingest** off for now; proxies are made in 1.5 so you can choose exactly which clips get them.

### 1.4 Sequence settings: 4K UHD 25p
Make one sequence preset and reuse it for every timeline on this job.
1. File > New > **Sequence** > **Settings** tab:
   - Editing Mode: **Custom**
   - Timebase: **25.00 frames/second**
   - Frame Size: **3840 x 2160**, Pixel Aspect Ratio **Square Pixels (1.0)**
   - Fields: **No Fields (Progressive Scan)**
   - Display Format: 25 fps Timecode
   - Working Colour Space: **Rec. 709** (the footage is standard Rec.709; leave any HDR or tone-mapping options off)
   - Audio Sample Rate: **48000 Hz**, Display Format: Audio Samples
   - Video Previews: Preview File Format **I-Frame Only MPEG** (or QuickTime with the **GoPro CineForm** codec, which handles 4K better), width 3840, height 2160. Untick Maximum Bit Depth while editing.
2. **Tracks** tab: Audio, Mix **Stereo**, 6 tracks (A1 camera, A2 phone, A3 room tone, A4 music, A5 SFX, A6 spare).
3. Click **Save Preset**, name it **`WFT 4K25 UHD`**, then OK.
4. Shortcut check: drag one 4K 25p clip onto the New Item icon in the Project panel. Premiere makes a matching sequence; compare it with the preset (it should say 3840 x 2160, 25.00 fps).

**Project template:** once the bins (1.5) and sequence preset exist, but before importing media, use File > Save As to save an empty copy named `WFT_Template_4K25.prproj` in a `Templates` folder. On every new job, duplicate it in Windows Explorer and rename it.

### 1.5 Import, bins, proxies and slow motion
1. **Import** with the **Media Browser** (Window > Media Browser), not Windows Explorer: browse to `01_camera`. The Media Browser reads the Sony card structure and shows clean clips. Select all > right-click > **Import**.
2. **Bins** (Ctrl+B):
   - `01 Church 4K`, `02 Church SM 100p`, `03 Lunch 4K`, `04 Lunch SM 100p`
   - `05 Audio – phone`, `06 Audio – room tone`, `07 Phone wide`, `08 Music`, `09 Graphics`
   - `10 Sequences` (selects, stringouts, edits)
   - Tip: in List view, add the **Media Duration** and **Frame Rate** columns (panel menu > Metadata Display). Sort by Frame Rate to find every 100p clip at once.
3. **Slow motion: Interpret Footage before cutting.** Select every 100p clip (in bins 02 and 04) > right-click > **Modify > Interpret Footage** > Frame Rate: **Assume this frame rate: 25 fps** > OK. Each clip now plays 4x slower with every frame used (smooth, no frame blending). Its audio becomes unusable, so mute or unlink it in the edit.
4. **1080p in a 4K sequence:** the 100p clips are 1920 x 1080. When you first drop one into the sequence, choose **Keep existing settings**. Then select all 1080p clips in the timeline > right-click > **Set to Frame Size** (this scales them to 200% without baking in a low resolution). It is a 2x upscale, so use those shots briefly and avoid extra punch-ins on them. Turn **Scale to Frame Size** off for every 4K clip.
5. **Create proxies:** select all camera clips (4K and 100p) > right-click > **Proxy > Create Proxies**:
   - Format: **QuickTime**, Preset: **ProRes Low Resolution Proxy** (Premiere encodes ProRes on Windows), or **H.264 Low Resolution Proxy** if disk space is tight
   - Destination: `08_proxies/` (Next to Original Media also works, but keeps the card copies less tidy)
   - Premiere hands the job to **Media Encoder**, which starts it automatically. Expect about 1–2 hours for 2–3 hours of footage; run it overnight on Sat 24 Oct.
6. **Toggle Proxies button:** in the Program Monitor, click the **+** (Button Editor) and drag **Toggle Proxies** onto the button bar. Blue = proxies on. Keep it **on while editing**; turn it **off for the light correction pass** (day 8) and to check focus.
7. Program Monitor **Playback Resolution: 1/2** (1/4 if playback still stutters). Paused Resolution: Full.
8. **Render previews:** for heavy sections (titles over video, Warp Stabilizer, Lumetri stacks), set in/out points and use Sequence > **Render In to Out** (Enter). The red bar above the timeline turns green.
9. **Exports always use the originals.** In the Export settings, **Use Proxies** stays unticked (the default). Never tick **Use Previews** on the final exports.

### 1.6 Light correction only (Lumetri Basic Correction)
Footage is recorded with a finished look, so this pass only **fixes and matches**. No LUTs, no Creative tab looks, no grading.

1. Switch to the **Color** workspace (Window > Workspaces > Color). Turn **Toggle Proxies off** so you judge the real image.
2. Open **Lumetri Scopes** (Window > Lumetri Scopes): right-click > **Waveform (Luma)** and **Vectorscope YUV**. Set the scope's colour space to **Rec.709**.
3. **Pick the reference shot:** the vows hero shot (85mm on the couple). Correct it first:
   - Lumetri Color > **Basic Correction** > Input LUT: **None** (leave it empty).
   - **White Balance:** click the **WB Selector** eyedropper on something neutral (a white shirt, the altar cloth, a grey wall), then fine-tune **Temperature** and **Tint** by eye on the skin. Small moves (about ±10).
   - **Tone:** **Exposure** first (faces at about **60–70 IRE** on the waveform; keep moves within ±0.5 stop), then **Highlights** down if windows are hot, **Shadows** up slightly if dark suits are crushed. Keep **Contrast** and **Saturation** near 0 / 100.
   - Check the vectorscope: skin should sit on the **skin-tone line**.
4. **Match the other shots to it:** select a clip > Lumetri Color > **Color Wheels & Match** > **Comparison View** > choose the reference frame > **Apply Match** (tick Face Detection). Then trim Exposure and Temperature by hand in Basic Correction if needed. Apply Match is a starting point, not the final word.
5. **Copy corrections across:** clips from the same setup (same venue, same light) take the same fix. Select the corrected clip > Ctrl+C > select the others > **Edit > Paste Attributes** (Ctrl+Alt+V) > tick only **Lumetri Color**.
6. **Venue trims:** if every church shot needs the same small nudge, put an **Adjustment Layer** (Project panel > New Item > Adjustment Layer) over that section with one Lumetri Basic Correction, instead of touching each clip.
7. **Mixed light in the church** (window daylight and tungsten): correct for faces, not windows. Accept a little warmth; don't fight it with big moves.
8. **8-bit limits:** keep every move small. Big pushes on 8-bit footage show **banding** in white walls, ceilings and window glow, and noise in the shadows. If a shot looks bad after a small correction, swap it for another take instead of pushing harder.
9. **Clipping:** you cannot recover a blown window or face that clipped in camera. Bring Highlights down to soften it; if a face is clipped, use a different take.
10. **Shake:** for a hero shot that wobbles, apply **Warp Stabilizer** (Effects > Video Effects > Distort): Result **Smooth Motion**, Smoothness **5–15%**, Method **Position, Scale, Rotation** (Subspace Warp can warp faces). Render previews afterwards.
11. **Flicker:** if an LED flickers despite the 1/50 shutter, cut away from it or crop it out.

**Phone wide footage** (if shot): newer iPhones record HDR (HLG) by default. If it looks washed out or too bright in the Rec.709 sequence, select the clip > right-click > **Modify > Interpret Footage > Colour Management** > override the input to **Rec. 709**, then use Basic Correction as above. Tell Bartholomew if it still looks wrong.

---

## 2. Day-by-day schedule (Sat 24 Oct to Fri 6 Nov)

About 4–6 hours of edit time per working day. Friday is the weekend in Bangladesh; **Fri 30 Oct** is a rest day, and **Fri 6 Nov** is delivery only.

| Day | Date | Work | Done when |
|---|---|---|---|
| 1 | **Sat 24 Oct** | **Backup and ingest.** Confirm two copies exist (external SSD + a second drive). Create the project from the template, import with the Media Browser, sort bins, Interpret Footage on the 100p clips, create proxies overnight. Copy the phone audio. Note: matthias owns the backup check. | 2 verified copies; proxies rendering; all clips in bins |
| 2 | **Sun 25 Oct** | **Watch everything and select.** Play through all footage once. Mark selects with **in/out points and subclips** (Ctrl+U) or a **label colour**, and add **markers** (M) at the best lines (vows, rings, the banns reading, speech laughs). Build a `SELECTS` sequence of the best 15–20 minutes. Run **Speech to Text** on it (section 6) to get the key spoken lines with timecodes. Shortlist 3–5 licensed music tracks with james-the-less. | Selects sequence + list of key lines + music shortlist |
| 3 | **Mon 26 Oct** | **Full ceremony: sync and assembly.** Sync the camera and phone audio (section 4.2). Lay the whole ceremony in order on one sequence with continuous audio. | Ceremony assembly, in sync end to end |
| 4 | **Tue 27 Oct** | **Full ceremony: cover the gaps and trim.** Cover camera stops, jump cuts and focus misses with b-roll and reactions. Trim the dead time before the start and after the end. Add chapter markers. | Ceremony fine cut v1 (picture locked unless QC finds problems) |
| 5 | **Wed 28 Oct** | **Highlight: the "radio edit".** Build the audio story first: the best vow lines, the banns, one or two speech lines, then lay the music under them. Lock the music track and its edit points (cut the music to length; Premiere's **Remix** tool can retime a track to an exact length). | Highlight audio spine + music locked |
| 6 | **Thu 29 Oct** | **Highlight: picture cut v1.** Put pictures on the audio spine beat by beat (section 3). Cut to the music; use slow motion for the arrival, exit, cake and food. | Highlight v1, about 4:30–5:00 |
| – | Fri 30 Oct | **Rest.** Optional: watch highlight v1 once on a phone, with fresh eyes, and write notes. Don't edit. | Notes list |
| 7 | **Sat 31 Oct** | **Highlight v2: rhythm and cutting down.** Apply the notes. Cut anything that doesn't serve the story; aim for 4:00–4:20. Cut the **Instagram 9:16 teaser** (30–45 s) from the highlight. | Highlight picture lock + teaser cut |
| 8 | **Sun 1 Nov** | **Light correction pass** (section 1.6). Proxies off. Match exposure, white balance and skin tones across both films with Lumetri Basic Correction. The films share clips, so correct each clip once in the highlight and **Paste Attributes** into the ceremony sequence. Check for clipping and banding. Usually 2–3 hours, not a full day; use the rest to start the audio cleanup. | Both films corrected and matched |
| 9 | **Mon 2 Nov** | **Sound mix** (with james-the-less). Dialogue cleanup, music ducking, room tone under the cuts (section 4.4). Ceremony: smooth the level between officiant, readers and vows. | Both mixes clean and balanced |
| 10 | **Tue 3 Nov** | **Titles, captions and the first exports.** Opening title and end card (couple's names, date, church: **need these from Frank**). Captions (section 6). Export v1 of every deliverable through the Media Encoder queue (section 5). **Hand to thomas for QC.** | v1 files + QC request |
| 11 | **Wed 4 Nov** | **QC fixes.** Fix thomas's notes (sync slips, spelling, loudness, black frames, flashes). Frank watches both films in full. | QC passed; Frank's notes in |
| 12 | **Thu 5 Nov** | **Final exports and archive.** Final renders; play every file through once; upload privately (unlisted/private) **only after Frank approves**. Archive with File > **Project Manager > Collect Files and Copy to New Location** (exclude unused clips, include proxies only if space allows), plus exports and music licences, on two drives. | Final files + archive done |
| 13 | **Fri 6 Nov** | **Delivery**: Frank sends the links and the WhatsApp file to the couple (his approval and his send). Post the teaser only if Frank and the couple agree. | Delivered |

**Buffer:** day 8 is now short (light correction, not grading), and Wed 4 Nov has slack. If audio runs long, push the exports to Wed and keep Thu as the safety day.
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
- **Rhythm:** wide shots 3–5 s, close-ups 2–3 s, slow motion 3–6 s (it reads slower). Cut on the music's beat in beats 2, 5 and 8; cut on speech pauses and reactions in beats 4 and 7. Tip: play the music and tap **M** on each beat to drop markers, then cut to them.
- **Hold the moments:** do not cut away during a vow line; cut on the breath after it.
- **Cut everything that doesn't serve the story:** repeated detail shots, guests with no connection to the couple, shaky walking shots, anything you have to explain.
- **Speed ramps:** none. Real-time and interpreted slow motion only; it suits the occasion.
- **Audio from 100p clips is dropped.** Use room tone or the music under slow motion; add natural sound (applause, laughter) from the 25p clips if needed.
- **Titles:** use the **Type tool** (T) or Essential Graphics > Browse for a simple, clean title. Save the style as a **Text Style** so the title and end card match.

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

### 4.2 Sync the phone backup audio, step by step
1. **Check the camera track layout:** select a camera clip in the Project panel > right-click > **Modify > Audio Channels**. If the receiver recorded split (TX1 left, TX2 right), set Clip Channel Format to **Mono** with 2 audio clips, so each mic gets its own track. If it is a mono mix, leave it as stereo.
2. **Phone file format:** if the phone recorded M4A/AAC at 44.1 kHz, Premiere plays it fine. If sync drifts badly or the file won't conform, convert it to **48 kHz WAV** in Media Encoder (Format: Waveform Audio) and import that instead.
3. **Ceremony: Synchronize on the timeline** (best for one long phone recording and many camera clips):
   1. New sequence from the `WFT 4K25 UHD` preset, name it `CEREMONY FULL`.
   2. Put the **phone recording on A2**, starting at 00:00:00:00. It runs continuously, so it defines the timeline.
   3. Drag the church camera clips onto **V1/A1** in roughly the right place, in order (use the clip times or the claps at each camera restart as a guide).
   4. Select the phone clip **and** one camera clip > right-click > **Synchronize** > **Audio**, Track Channel **1** > OK. Premiere moves the camera clip to match the phone waveform. Repeat for each camera clip (you can select the phone clip and several camera clips at once; if one lands wrong, undo and do it on its own).
   5. Zoom in and check each clip against the waveform on a clap or a hard consonant.
4. **Highlight and lunch: Merge Clips** (best for short clips with a matching piece of phone audio, e.g. the speeches at the head table):
   1. In the Project panel, select **one camera clip and the phone recording** > right-click > **Merge Clips**.
   2. Synchronize Point: **Audio**. Tick **Remove Audio from AV Clip** only if the camera audio is useless (keep it if the DJI lav is on it). Name the merged clip, e.g. `SPEECH_01_merged`.
   3. The merged clip now behaves like one clip with both sound sources, so you can cut it freely in the highlight without losing sync.
   4. Merge Clips takes **one video clip at a time**, and the merged clip spans the whole phone recording, so trim it in the Source Monitor. For many clips against one long recording, use the timeline Synchronize method (3) instead.
5. **Drift check:** the phone and camera clocks drift slightly over long takes (often 1–2 frames per 10–20 minutes). Check sync at the **start and end of every long camera clip**. If it drifts, cut the phone audio at a pause every 10 minutes (**C** Razor tool, or Ctrl+K at the playhead) and nudge the later piece back into sync (select it > **Alt+Left/Right arrow** moves it 1 frame). Add a 2-frame **Constant Power** crossfade at each cut (Ctrl+Shift+D).
6. **Lock** the synced audio tracks (padlock icon on the track header) before cutting picture.

### 4.3 Picture: single camera, so cover the cuts with b-roll
- **Main angle:** the 85mm static shots of the officiant and the couple, and the 24mm wide from the back (shot 2).
- **Camera stops** (battery or card swaps, lens changes): the phone audio continues. Cover the gap with, in order of preference:
  1. The **phone locked-off wide** (if shot), synced the same way. This is the ideal safety angle.
  2. **B-roll from the same moment:** congregation (11), family reactions (10), details (3), the interior wide (2).
  3. **Exterior/detail shots** shot before or after (1, 3) with a slow, gentle push-in (Effect Controls > Motion > **Scale** keyframes, 100% to 105%).
  4. Last resort: a slow **Dip to Black** and back, only for long gaps in non-key moments.
- **Jump cuts** (where you trimmed inside a static shot): put a 2–4 s reaction or detail shot on V2 over the cut; the audio continues underneath. Use reactions from the same section, so the light and positions match.
- **Focus misses and shaky moments:** cover them the same way. Don't cover the vows or the rings unless there is truly nothing else. A slightly soft real moment is better than b-roll.
- **Never** cover the vows or ring exchange with unrelated b-roll. If the camera missed them, use the phone wide or hold on the couple's two-shot.
- **Dead time:** trim the waiting before the entrance and long pauses (people moving to the lectern) with the audio crossfaded (5–10 frames) and covered with b-roll. Keep the liturgy intact; don't shorten readings, prayers or the banns.
- **Slow motion:** not used in the ceremony film, except in a short opening and closing (the entrance and the exit).
- **Structure:** a 20–30 s opening (exterior, details, title), the ceremony in real time, then a 30–60 s closing (exit, greetings, group photo) under licensed music, then the end card.

### 4.4 Audio cleanup in Premiere (both films)
Window > Workspaces > **Audio**, then use the **Essential Sound** panel. Select clips and tag them first: **Dialogue** (vows, readings, speeches), **Music**, **Ambience** (room tone, applause), **SFX**.

**Dialogue clips:**
1. **Pick the best source line by line:** the **groom's lav for vows**, the lectern TX or the phone for the officiant and readers. Crossfade between sources over 5–10 frames; never play two sources together at full level (it causes phasing/echo). Mute the source you are not using (Shift+E disables a clip).
2. **Enhance Speech** (Essential Sound > Dialogue): use it on the phone audio and any noisy lav lines. Set **Mix Amount to 40–70%**; at 100% voices can sound artificial. It processes in the background; listen to every line it touches.
3. **Repair** (tick only what the clip needs, keep amounts low):
   - **Reduce Noise** 2–5 for fan/AC hiss
   - **Reduce Rumble** 3–6 for traffic or handling noise
   - **DeHum** 50 Hz (Bangladesh mains) if you hear a buzz
   - **DeEss** 3–5 on harsh "s" sounds
   - **Reduce Reverb** 2–4 for the church echo, sparingly
4. **Clarity:** Dynamics (gentle compression) on, EQ preset **Subtle Voice Enhancement** or a high-pass at 80–100 Hz. Avoid Enhance and heavy EQ together; it gets thin.
5. **Loudness:** Essential Sound > Dialogue > **Auto-Match** to even out levels between clips. The final -14 LUFS target is set on export (section 5).

**Music clips:**
- Essential Sound > Music > **Ducking**: Duck against **Dialogue** clips, Sensitivity about 6, Reduce By **-18 to -22 dB**, Fades **800 ms** > **Generate Keyframes**. Then fix any duck that sounds wrong by hand with the keyframes on the clip.

**Room tone and joins:**
- Lay the **room tone** recording on A3 under every audio cut so silence doesn't drop out.
- Put a **Hard Limiter** (Effects > Audio Effects > Amplitude and Compression) on the **Mix** track in the Audio Track Mixer: Maximum Amplitude **-1.5 dB**. It catches peaks in applause and singing before the export normalization.
- Watch the Loudness Radar or meters while you mix: dialogue peaks around -10 to -6 dBFS, music bed well below.

### 4.5 Chapters
Add sequence markers at each part and, for the YouTube description, write chapter times: `00:00 Opening`, `Entrance`, `Readings`, `The Banns`, `Vows`, `Rings`, `Blessing`, `Exit`. YouTube needs the first chapter at 00:00 and at least three chapters of 10 s or more. Tip: name each marker, then File > Export > **Markers** (CSV) gives you the list with timecodes.

---

## 5. Export specs (Premiere Export mode and Media Encoder)

**For every export:**
1. Select the sequence > **File > Export > Media** (Ctrl+M) to open Export mode.
2. **Use Proxies: off** (Video section, unticked) and **Use Previews: off**. The export reads the camera originals.
3. Under **Video > More**, tick **Render at Maximum Depth** and **Use Maximum Render Quality** (important for the 1080p and 9:16 exports, which scale the 4K).
4. Encoding: **Hardware Encoding** when available (NVIDIA NVENC on the RTX). For the WhatsApp file, use **Software Encoding** with **VBR, 2 pass** for the best quality at a low bitrate.
5. **Loudness Normalization** (Effects section in the export settings, tick it): Loudness Standard **ITU BS.1770-3**, Target Loudness **-14 LUFS**, Tolerance **1 LU**, Max True Peak Level **-1 dBTP**. Premiere measures the whole programme and adjusts the gain to hit the target. Mix well first (section 4.4); normalization sets the level, it does not fix a bad mix.
6. Colour: the files are tagged **Rec.709**. Nothing to set.
7. Click **Send to Media Encoder** (not Export) to queue every deliverable, then press the green Start button in Media Encoder and let it run overnight while you keep editing (or sleep).
8. Play each finished file all the way through once before it goes anywhere, check it with the ffprobe/ffmpeg commands in `projects/studio-setup/qc-checklist.md`, then send it to thomas for QC.

### 5.1 Highlight film: YouTube / private link master
| Setting | Value |
|---|---|
| Format / codec | **H.264**, Profile **High**, Level **5.1** |
| Resolution | **3840 x 2160** |
| Frame rate | **25** |
| Bitrate encoding | **VBR, 1 pass** (hardware) or **VBR, 2 pass** (software); Target **50 Mbps**, Maximum **60 Mbps**. YouTube recommends 35–45 Mbps for 4K SDR at 24–30 fps; the extra headroom protects against banding in 8-bit footage. |
| Keyframe distance | Leave automatic |
| Audio | **AAC, 48 kHz, stereo, 320 kbps** |
| Loudness | Loudness Normalization on: **-14 LUFS**, **-1 dBTP** |
| File size | About 1.6 GB for 4:20 |
| Captions | **Create Sidecar File**, format **SubRip (.srt)** (section 6) |
| Upload | YouTube **Unlisted** (or Vimeo with a password), after Frank approves. YouTube shows the 4K version a while after HD finishes processing. |
| File name | `2026-10-23_Banns_Highlight_4K_v1.mp4` |

**Archive master** (keep, not for sharing): Format **QuickTime**, codec **Apple ProRes 422 HQ**, 3840 x 2160, 25p, audio **Uncompressed 24-bit, 48 kHz**, Loudness Normalization on. About 20–25 GB for 4:20. If the drive is tight, skip this and archive the project, media and music instead.

### 5.2 Full ceremony film: YouTube / private link
| Setting | Value |
|---|---|
| Format / codec | H.264, Profile **High**, Level **4.2** |
| Resolution | **1920 x 1080** (default chosen: about 9 GB per hour instead of about 22 GB at 4K, so it uploads overnight on a typical Dhaka connection; use 4K at 45 Mbps if the upload speed allows) |
| Frame rate | 25 |
| Bitrate encoding | VBR, Target **20 Mbps**, Maximum **24 Mbps** |
| Audio | AAC, 48 kHz, stereo, 320 kbps |
| Loudness | Loudness Normalization on: **-14 LUFS**, **-1 dBTP** (the speech is quieter on average than the highlight; normalization brings it up to match) |
| Captions | Sidecar **.srt** |
| Upload | YouTube **Unlisted**, after Frank approves; add the chapter list to the description |
| File name | `2026-10-23_Banns_Ceremony_1080p_v1.mp4` |

### 5.3 Instagram Reels / TikTok 9:16 teaser (30–45 s)
1. Cut the teaser in the 16:9 highlight first: duplicate the highlight sequence (Ctrl+Shift+/) > rename `TEASER cut`. Recut it short: cold-open vow line > arrival SM > vows > exit SM > cake/laugh > names card. Cut to the music; aim for 30–45 s (Reels and TikTok both allow longer, but shorter keeps people watching).
2. Select `TEASER cut` in the Project panel > **Sequence > Auto Reframe Sequence**: Target Aspect Ratio **Vertical 9:16**, Motion Tracking **Slower Motion**, Clip Nesting **Don't Nest Clips**. Premiere makes a new 1080 x 1920 sequence and tracks the subject in each shot.
3. Check every shot. Fix any bad framing in Effect Controls > **Auto Reframe** > Adjust > **Position**, or remove the effect and set Motion > Position by hand.
4. **Prefer 4K shots:** they give an almost-native 1215 x 2160 crop. The 1080p slow motion only gives a 607 x 1080 crop, upscaled about 1.8x, so it goes soft; use it briefly or skip it.
5. **Safe zones:** keep text and faces out of the **top 250 px and bottom 400 px** (the app's buttons and captions sit there) and about 60 px from each side. **Burn in** captions for the vow line: many people watch on mute.

| Setting | Value |
|---|---|
| Format / codec | H.264, Profile **High**, Level **4.2** |
| Resolution | **1080 x 1920 (9:16)** |
| Frame rate | 25 |
| Bitrate encoding | VBR, Target **16 Mbps**, Maximum **20 Mbps** (Instagram and TikTok recompress; a clean source helps) |
| Audio | AAC, 48 kHz, stereo, 320 kbps |
| Loudness | Loudness Normalization on: **-14 LUFS**, **-1 dBTP** |
| Captions | **Burn Captions into Video** |
| Length | 30–45 s |
| Music | The **same licensed track**, if the licence covers Instagram and TikTok. Otherwise use Instagram's in-app music: export without music and add it in the app. |
| Posting | Only if **Frank and the couple agree**; jude handles the caption. Not before the couple has seen the highlight film. |
| File name | `2026-10-23_Banns_Teaser_9x16_v1.mp4` |

### 5.4 WhatsApp-friendly highlight
For family who will watch on their phones and forward it.

| Setting | Value |
|---|---|
| Format / codec | H.264, Profile **Main**, Level **4.1** (plays on old phones) |
| Resolution | **1920 x 1080** (from the 4K highlight sequence; Render at Maximum Depth and Maximum Render Quality on) |
| Frame rate | 25 |
| Bitrate encoding | **Software Encoding, VBR 2 pass**, Target **3 Mbps**, Maximum **4 Mbps** |
| Audio | **AAC, 48 kHz, stereo, 128 kbps** |
| Loudness | Loudness Normalization on: **-14 LUFS**, **-1 dBTP** |
| File size | **About 100 MB** for 4:20 |
| File name | `2026-10-23_Banns_Highlight_WhatsApp.mp4` |

- Sent as a **video** in WhatsApp (tap **HD** before sending), it gets recompressed but still looks fine on a phone.
- To send it **without recompression**, attach it as a **Document** instead: the recipient gets this exact file.
- If the family mostly uses mobile data, also make a **720p (1280 x 720), 1.5 Mbps** version: about 50 MB.
- **Do not WhatsApp the full ceremony.** Send the private YouTube link instead.

### 5.5 Export presets
In Export mode, after setting each of 5.1–5.4, click the **Preset** menu > **Save Preset**: `WFT YT 4K25`, `WFT YT 1080p25`, `WFT Reel 9x16`, `WFT WhatsApp 1080`, `WFT Archive ProRes HQ`. Saved presets appear in Media Encoder too, so later jobs take two clicks. On Tue 3 Nov, send all four deliverables to the Media Encoder queue and render overnight.

---

## 6. Captions (Speech to Text)
1. Open the sequence > **Window > Text** > **Transcript** tab > **Transcribe sequence**. Language: the language spoken (English for an English service). Tick **Recognize when different speakers are talking**. Audio Analysis: **Mix** (or only the dialogue track if music is loud).
2. Read through the transcript and correct names, scripture references and church words. Premiere often mishears names; check them against the brief.
3. **Captions** tab > **Create captions** from the transcript: Maximum length **32 characters** (42 for the 16:9 films), Minimum duration 1.5 s, Lines **Double** (16:9) / **Single** (9:16).
4. Style them once in **Essential Graphics** (clean sans-serif, white with a soft shadow or a 60% black background) and save a **Track Style** so every caption matches.
5. **Mixed languages:** if parts of the service are in Bangla or another language Premiere does not transcribe, type those captions by hand (Captions tab > **+** to add a caption block), or leave them uncaptioned. Default chosen: caption the vows, readings and speeches; skip hymns.
6. Export: **sidecar .srt** for the YouTube films (upload it in YouTube Studio > Subtitles), **burned in** for the 9:16 teaser and, optionally, the WhatsApp file.

---

## 7. Open items for Frank
- The **couple's names** and the **church name** (needed for titles by Tue 3 Nov).
- **Laptop model**, RAM and GPU (to confirm the proxy preset and playback resolution), and the **Premiere Pro version** installed.
- The **language(s)** of the service and speeches (for Speech to Text, section 6).
- Whether the **phone locked-off wide** was shot, and whether there were **1 or 2 transmitters**.
- **Music choice**: approve one track from james-the-less's shortlist (needed by Wed 28 Oct).
- Permission from the couple to post the teaser publicly (default: private only).

## 8. Suggested board tasks (for the team lead)
- `matthias`: verify the two backups and set up the Premiere project template, sequence preset and proxy settings on the laptop (Sat 24 Oct, High)
- `james-the-less`: shortlist and license the music; help with the audio cleanup and mix (shortlist by Sun 25 Oct, mix Mon 2 Nov)
- `bartholomew`: edit, light correction, captions and exports per this plan (Sat 24 Oct – Thu 5 Nov)
- `thomas`: QC every deliverable (Tue 3 – Wed 4 Nov)
- `jude`: teaser caption and posting plan, only if the couple agrees (by Thu 5 Nov)
