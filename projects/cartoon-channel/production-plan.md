# Oops! Toons · Mishti & Moto · production plan (from 27 Oct 2026)

**Goal:** make a 7-episode buffer of silent slapstick Shorts by Sun 8 Nov, launch on **Mon 9 Nov 2026**, then publish 5 Shorts and 1 compilation a week in about 3–4 h a day, for about $30–40 a month.
Read with `plan.md` (story formula, targets) and `channel-kit.md` (titles, tags, settings).

**Assumptions (change them if wrong):**
- Cartoon time is **3.5 h a day, 6 days a week**, after the colour lesson (30–45 min) and Fiverr work. The 7th day is light (review only).
- Shorts go out **Mon–Fri at 8:00 AM Dhaka**. Compilations are edited on Saturday and go out **Sunday 8:00 AM**.
- Client work (for example, any Banns of Marriage edits still owed from the 23 Oct shoot) comes first. If it takes a cartoon day, the buffer absorbs it. Don't skip QC.
- Episodes 1–2 will take about 5–6 h because the workflow is still new. From episode 3 on, the target is about 3.5 h (`plan.md`).

## 1 · Pre-launch phase (27 Oct – 8 Nov)

| Date | Work (≈3.5 h) | Helpers |
|---|---|---|
| Tue 27 Oct | Finish the channel-kit checklist (handles, 2-step verification, playlists, upload defaults). Create the folder tree (section 4). John starts scripts EP001–EP010. | matthias, jude, john |
| Wed 28 Oct | **Mishti character sheet:** front, side and back views, plus 4 expressions (happy, smug, shocked, sleepy). Lock the red scarf and her orange colour. | james |
| Thu 29 Oct | **Moto character sheet:** the same views and expressions. Then run a **consistency test**: 3 Flow image-to-video clips of each character. If they drift, fix the sheet now. | james |
| Fri 30 Oct | **3 locations, made once:** (A) old-Dhaka street with a tea stall and rickshaws, (B) a rooftop with water tanks and kites, (C) home interior (living room and bathroom). Approve storyboards EP001–EP003. | james, john |
| Sat 31 Oct | **EP001 pilot:** images and animation. Write down every prompt that works in `00_bible/prompts.md`. | james |
| Sun 1 Nov | EP001 edit and sound. Build the **Premiere template** (9:16 sequence, SFX bin, end card, watermark). | bartholomew, james-the-less |
| Mon 2 – Sat 7 Nov | One episode a day: **EP002 → EP007** | all |
| Sun 8 Nov | Thomas runs QC on EP001–EP007. Make thumbnails and metadata, then **schedule EP001–EP005**. John delivers scripts EP011–EP015. | thomas, jude |
| **Mon 9 Nov** | **LAUNCH:** EP001 goes live at 8:00 AM | |

**Why Mon 9 Nov and not earlier (about 10 days out):** a 7-episode buffer at 3.5 h a day, with slow first episodes, needs about 9 working days after the 3 setup days. Launching on a Monday also starts the weekly rhythm cleanly.
**Slip rule:** if fewer than 4 episodes are finished by Thu 5 Nov, move the launch to **Mon 16 Nov**. Don't launch with a thin buffer.

## 2 · Weekly batch rhythm (from the week of 8 Nov)

Each week makes **5 new episodes** and publishes **5 older ones**, so the 7-episode buffer stays the same. Work happens in batches, one stage per day, to save setup time.

| Day | Batch work (≈3.5 h) | Owner/helper |
|---|---|---|
| **Sun** | Weekly review (45 min, section 6). Approve John's 5 scripts and storyboards for the week (1.5 h). Book next week's ideas. | john, jude |
| **Mon** | **Generate images** for all 5 episodes (about 35–40 panels) using the character refs | james |
| **Tue** | **Animate** in Flow, episodes 1–3 of the batch | james |
| **Wed** | **Animate** episodes 4–5, plus retakes of any broken shots | james |
| **Thu** | **Edit and sound** episodes 1–3 | bartholomew, james-the-less |
| **Fri** | **Edit and sound** episodes 4–5, export all, Thomas QC | bartholomew, thomas |
| **Sat** | **Compilation** edit (from week 2 of posting, goes live Sun 8:00 AM), thumbnails, titles/tags, **schedule next week's 5 Shorts**, cross-post | jude, thomas |
| Daily, 8:00–8:30 AM | Short goes live. Pin the comment and reply to comments for 15 min (from the colour-lesson break). | jude |

Batches run 1–2 weeks ahead. For example, EP008–EP012 are made 9–13 Nov and go out 18–24 Nov.

## 3 · Per-episode pipeline checklist (target ≈3.5 h)

| # | Step | Time | Done when |
|---|---|---|---|
| 1 | Script (John): hook / try / twist / payoff + loop, 6–8 panels | 20 min to approve | One page, and the loop ending matches frame 1 |
| 2 | Storyboard: one line per panel (shot size, action, sound cue) | 10 min | Panel list saved in `01_script/` |
| 3 | Images: each panel generated with the Mishti, Moto and location refs | 40–50 min | Every panel on-model (scarf, colours, size difference) |
| 4 | Animation: Flow (Veo) image-to-video, 4–8 s per shot, 9:16 if offered (otherwise reframe in the edit) | 60–75 min | All shots usable. Max 3 tries per shot, then simplify the action |
| 5 | Premiere edit: cut for timing, hold the gag beat, loop the end into frame 1 | 40 min | 30–60 s, hook in the first 2 s |
| 6 | Sound: SFX (boing, whoosh, splat) and music from the YouTube Audio Library (or a paid Suno plan) | 20 min | Every hit has a sound. Music sits under the SFX. Licence noted |
| 7 | Export: 1080×1920, H.264, frame rate matching the Flow clips | 5 min | File in `07_export/` and played back once on a phone |
| 8 | QC (Thomas): on-model, no glitches or creepy frames, audio levels, title length, made-for-kids answer, AI disclosure | 10 min | Pass, or a list of fixes |
| 9 | Upload: title formula, description template and tags from the channel kit; Related video; playlist; schedule for 8:00 AM | 10 min | Scheduled in YouTube Studio |
| 10 | Cross-post: Instagram Reels, TikTok, Facebook Reels (clean file, no watermarks) | 10 min | Scheduled or posted the same day |

## 4 · Folders and file names (ASUS TUF laptop)

Use the drive with the most free space (default `D:\OopsToons\`, or `C:\OopsToons\` if there is only one drive). Write names in lower case with hyphens and keep the episode number first.

```
OopsToons\
  00_bible\        mishti_sheet_v01.png, moto_sheet_v01.png, loc-A_street.png, loc-B_rooftop.png,
                   loc-C_home.png, prompts.md, style-notes.md
  01_sound\        sfx\ , music\ , licences.md (track, source, date)
  02_templates\    oops-template.prproj, endcard.png, watermark.png
  episodes\
    EP001_falling-ice-cream\
      01_script\   EP001_script.md, EP001_storyboard.md
      02_refs\     copies of the refs used (in case the bible changes later)
      03_images\   EP001_sh01_v01.png, EP001_sh02_v01.png ...
      04_shots\    EP001_sh01_v02.mp4 ...
      05_edit\     EP001_falling-ice-cream.prproj
      06_export\   EP001_falling-ice-cream_1080x1920_v01.mp4, EP001_thumb.png
      07_upload\   EP001_metadata.txt (title, description, tags, publish date, URLs)
  compilations\    COMP01_best-of-1-10\ (same subfolders)
```

**Backup (3-2-1):** keep the laptop copy, an **external drive** and a **cloud copy** (Google Drive). Copy `00_bible`, scripts and exports to the cloud every day (they're small). Mirror the whole `OopsToons\` folder to the external drive every Sunday. Flow also keeps your generations online, but don't treat it as a backup. It isn't recorded whether Frank owns an external drive. If he doesn't, Matthew prices one for Frank's approval. Matthias sets up the folders and the sync.

## 5 · First 4 weeks of publishing (8:00 AM Dhaka)

| Date | Release | Status today (27 Oct) |
|---|---|---|
| Mon 9 Nov | EP001 · Moto vs the Falling Ice Cream 🍦 Oops! | Buffer: make 31 Oct–1 Nov |
| Tue 10 Nov | EP002 · Moto vs the Rickshaw Horn | Buffer: make 2 Nov |
| Wed 11 Nov | EP003 · Mishti's Tea Cup Tower… Oops! ☕ | Buffer: make 3 Nov |
| Thu 12 Nov | EP004 · When the Umbrella Won't Open 🌧️ | Buffer: make 4 Nov |
| Fri 13 Nov | EP005 · Moto's First Kite | Buffer: make 5 Nov |
| Sun 15 Nov | No compilation yet (only 5 episodes out). First Sunday review | |
| Mon 16 Nov | EP006 · The Mango That's Too High | Buffer: make 6 Nov |
| Tue 17 Nov | EP007 · Bath-Time Escape | Buffer: make 7 Nov |
| Wed 18 Nov | EP008 · The Lost Slipper | Batch 1: make 9–13 Nov |
| Thu 19 Nov | EP009 · The Power Cut and the Torch | Batch 1 |
| Fri 20 Nov | EP010 · Moto Tries to Be Quiet | Batch 1 |
| Sun 22 Nov | **COMP01** · Best of EP001–EP010 + new linking scene (~8 min) | Edit Sat 21 Nov |
| Mon 23 – Tue 24 Nov | EP011–EP012 (John's batch 2 ideas, approve Sun 8 Nov) | Batch 1 |
| Wed 25 – Fri 27 Nov | EP013–EP015 | Batch 2: make 16–20 Nov |
| Sun 29 Nov | **COMP02** · EP006–EP015 best moments + linking scene | Edit Sat 28 Nov |
| Mon 30 Nov – Thu 3 Dec | EP016–EP019 | Batch 2 (EP016–017), batch 3: make 23–27 Nov |
| Fri 4 Dec | EP020 | Batch 3 |
| Sun 6 Dec | **COMP03** · Rooftop and rain special | Edit Sat 5 Dec |

November totals: 16 Shorts and 2 compilations, which matches the Month 1 target in `plan.md`. The first compilation waits until week 2 because 5 episodes are too few for 8 minutes.

## 6 · Sunday weekly review (45 min, YouTube Studio)

| Metric | Where | What to do with it |
|---|---|---|
| Viewed vs swiped away (each Short) | Studio → Short → Analytics | The 2 worst: rewrite the hook style (a stronger first image in 0–2 s) |
| Average % viewed and rewatches | Analytics | The best: make a sequel in the same location or with the same gag |
| Views in first 48 h | Content tab | Is 8:00 AM working? Test 7:00 or 9:00 AM for one week only |
| Subscribers gained per video | Analytics → Audience | Find which character or location wins, then use it more |
| Watch hours (compilations) | Analytics → Long videos | If low: better thumbnail, then a longer linking scene |
| Comments (themes, requests) | Comments | Take good viewer ideas into John's next batch |
| Cross-post views (IG, TikTok, FB) | Each app | Drop any platform that takes time and gives nothing after 4 weeks |
| **Production:** hours per episode, Flow generations per episode, credits left, buffer count, money spent | `07_upload` logs, Flow account | If buffer < 5: cut to 4 Shorts next week, never skip QC |

**Rules:** change one thing a week and keep a one-line note of it in `00_bible/style-notes.md`.

## 7 · Owners

| Step | Disciple |
|---|---|
| Scripts, storyboards, idea list, compilation linking scenes | **john** |
| Character/location look, shot design, image and Flow prompts | **james** |
| SFX library, music choice and licence log, mix levels | **james-the-less** |
| Premiere template, edit timing, exports, compilations | **bartholomew** |
| Titles, descriptions, tags, thumbnails, scheduling, cross-posts, Sunday analytics | **jude** |
| QC before anything is scheduled or published | **thomas** |
| Folder tree, sync, Sunday backup, laptop performance | **matthias** |
| Monthly budget, credit tracking, purchases for Frank's approval | **matthew** |

## 8 · Budget and risks

**Budget:** **$30–40 a month** (an AI video plan plus music), as in `plan.md`. Week 1 (27 Oct–2 Nov) uses free tiers only. Upgrade only when free credits stop the buffer work. Matthew checks the current Flow/Veo plan price and credit allowance on Google's official page before Frank pays. Nothing is bought without Frank's approval. Music and SFX come from the YouTube Audio Library (free) first. A paid Suno plan is optional and stays inside the $30–40 cap. Possible one-off cost: an external drive for backup, if he doesn't have one (Matthew quotes it).

| Risk | Mitigation |
|---|---|
| **Veo credits run out mid-week** | Log generations per episode from EP001. Max 3 tries per shot. Do the image work first (cheaper to iterate). Simplify the action instead of re-rolling. Matthew checks credits every Sunday. |
| **Character consistency** (Mishti's scarf, colour, size vs Moto) | One locked sheet in `00_bible` used for every generation. Thomas checks "on-model" at QC. If a shot drifts, regenerate the image, not the video. Version the sheets (v01, v02) and never edit them mid-batch. |
| **AI-content policy honesty** | Original characters only, every episode a written story, your own edit and sound (`plan.md`). The channel description already says animation is made with AI tools. Answer the altered/synthetic question honestly on every upload. Decide "made for kids" per video. No creepy or distressing frames (Thomas rejects them). |
| **Burnout** (3–4 h a day on top of lessons, Fiverr and clients) | Batch days, not daily start-to-finish. Sunday is light. The 7-episode buffer means a sick day or a client shoot costs nothing. If the buffer drops below 5, post 4 a week, not 5. Review the workload honestly at the end of November. |
| **Client work collides** (shoots, the Banns edit, Fiverr deadlines) | Client first. The buffer covers up to a week. Rebuild it the following week. |
| **Laptop or file loss** | 3-2-1 backup (section 4) and weekly mirror. Matthias checks it on Sundays. |
| **Rain or power cuts in Dhaka** | Upload scheduling is done days ahead, so publishing doesn't depend on the day's power or internet. Keep the laptop charged during render days. |

## Task list for the dashboard

| # | Title | Owner | Priority | Next step |
|---|---|---|---|---|
| 1 | Finish channel-kit checklist | jude | High | Reserve handles, set up 2-step verification, playlists, upload defaults today (27 Oct) |
| 2 | Create OopsToons folder tree + backup | matthias | High | Build the section 4 tree. Ask Frank if he has an external drive |
| 3 | Scripts EP001–EP010 | john | High | Write 6–8-panel storyboards. EP001–003 ready for approval Fri 30 Oct |
| 4 | Mishti & Moto character sheets | james | High | Mishti on Wed 28 Oct, Moto and the consistency test on Thu 29 Oct |
| 5 | 3 location references | james | High | Street, rooftop, home on Fri 30 Oct |
| 6 | Premiere 9:16 template + SFX bin | bartholomew | High | Build on Sun 1 Nov during the EP001 edit |
| 7 | SFX and music library + licence log | james-the-less | Medium | Collect boing, whoosh and splat from the YouTube Audio Library by Sat 31 Oct |
| 8 | Produce buffer EP001–EP007 | james / bartholomew | High | EP001 pilot on Sat 31 Oct. Slip check on Thu 5 Nov |
| 9 | QC EP001–EP007 | thomas | High | Run the checklist on Sun 8 Nov before scheduling |
| 10 | Schedule launch week EP001–EP005 | jude | High | Schedule for 8:00 AM, 9–13 Nov, on Sun 8 Nov |
| 11 | Monthly AI/music budget | matthew | Medium | Check the current Flow plan price and credits before the free tier runs out. Needs Frank's approval to buy |
| 12 | Scripts EP011–EP020 | john | Medium | Batch 2 for approval on Sun 8 Nov |
| 13 | Sunday analytics review | jude | Medium | First review on Sun 15 Nov, using the section 6 table |
