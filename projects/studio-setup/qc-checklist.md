# Pre-Delivery QC Checklist

Frank's checklist for every export: **YT** = YouTube, **SOC** = Instagram Reels / TikTok, **CLI** = client master (e.g. wedding highlight + full ceremony). Copy it into the project folder and tick each box. Note the timecode (HH:MM:SS:FF) of anything that fails.

## 1. Picture
- [ ] Resolution: YT 3840x2160 or 1920x1080 · SOC 1080x1920 (9:16) · CLI as quoted (usually 4K or 1080p, 16:9)
- [ ] Frame rate is **25p** from shoot to timeline to export, with no 23.976/29.97 conform. Slow motion (50/100p) is conformed to 25p.
- [ ] Aspect ratio and SAR 1:1. No black bars unless intended. SOC: titles and faces are clear of the caption/button areas at the top, bottom and right edge.
- [ ] S-Log3 is fully graded (no flat or grey shots). Skin tones match from shot to shot. Rec.709, video (limited) levels. No crushed blacks and no clipped whites on the scopes.
- [ ] No banding in skies or walls (the A7C records 8-bit, so add grain or dither if it shows). Check on the export, not the timeline.
- [ ] No flicker from LED or mains lighting (50 Hz: shutter 1/50 or 1/100). No flash frames, black frames or stray gaps at cuts.
- [ ] Drone shots: horizon is level, no props in frame, no jello.

## 2. Audio
- [ ] Loudness (integrated) and peak targets:
  - YT: about **-14 LUFS**, true peak **≤ -1 dBTP**. YouTube turns louder videos down and does not turn quieter ones up. [1][2]
  - SOC: about **-14 LUFS**, true peak **≤ -1 dBTP**. This is common practice, not a published Meta/TikTok spec. [3]
  - CLI: the client's spec if they gave one. Otherwise -14 LUFS / -1 dBTP for online playback (-23 LUFS EBU R128 only if it is going to broadcast).
- [ ] Lip sync is right at the start, middle and end of long pieces (ceremony). DJI Mic Mini 2 audio is aligned to the camera scratch track.
- [ ] No clipping, pops, wind or mic rustle. The vows and speeches are intelligible on phone speakers.
- [ ] Music: the licence is valid for this platform and use (client/commercial). Licence PDF is saved in the project. YT Content ID is clear (check in Studio before publishing).

## 3. Text
- [ ] Names are spelled exactly as the client wrote them (couple, venue, date), checked against the brief or email and not from memory.
- [ ] Titles, lower thirds and end card are free of typos, and the date and place are correct.
- [ ] Captions/subtitles are on (burned in for SOC). They are in sync, spelled correctly and don't cover faces. The YT .srt file is uploaded.

## 4. File
- [ ] Codec: H.264 (High) or H.265, yuv420p, AAC 48 kHz stereo, .mp4. CLI archive master (if quoted): ProRes 422 HQ or a high-bitrate H.264.
- [ ] Bitrate (SDR, 25p): 4K about 35-45 Mbps · 1080p about 8-12 Mbps · SOC 1080x1920 about 10-20 Mbps. Audio 320 kbps.
- [ ] File name: `YYYY-MM-DD_Client-Project_Deliverable_Res_v01.mp4` (e.g. `2026-10-18_Rahman-Wedding_Highlight_4K_v01.mp4`). Use no spaces.
- [ ] Check the specs (free, ffprobe):
  `ffprobe -v error -show_entries stream=codec_name,profile,width,height,r_frame_rate,pix_fmt,sample_aspect_ratio,display_aspect_ratio,bit_rate,sample_rate,channels:format=duration,bit_rate -of default=nw=1 "FILE.mp4"`
- [ ] Measure loudness (ffmpeg loudnorm, measuring only, the file is not changed):
  `ffmpeg -hide_banner -nostats -i "FILE.mp4" -af loudnorm=I=-14:TP=-1:LRA=11:print_format=summary -f null - 2>&1 | grep -E "Input (Integrated|True Peak|LRA)"`

## 5. Delivery
- [ ] Watched the full export once on the **laptop** (headphones) and once on a **phone** (speaker). Not the timeline, not scrubbed.
- [ ] Deliverables match what was quoted (count, lengths, formats, raw files yes/no, revision round).
- [ ] Backup kept: project + media + export on 2 drives, with 1 copy off the laptop.
- [ ] Client link works in a private window, downloads are on, expiry date noted. YT: visibility, thumbnail, title and description checked.
- [ ] Frank has approved before anything is sent or published.

---
**Sources** (loudness, checked 2026-10-21). YouTube, Meta and TikTok publish no official LUFS spec, so these figures are well-established industry measurements and not platform guarantees.
[1] Ian Shepherd, "YouTube stats for nerds" explained: https://productionadvice.co.uk/stats-for-nerds/
[2] Audio normalization (YouTube about -14 LUFS, turns down only): https://en.wikipedia.org/wiki/Audio_normalization
[3] Platform loudness table (Reels/TikTok -14 LUFS, -1 dBTP, "starting points, not official"): https://vloggingpro.com/tools/audio-loudness/
