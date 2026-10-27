# Frank Willson Talukder — Studio Profile

Frank is a **one-person filmmaker**: he writes, shoots, flies, edits and sells his own work.
Every plan must be doable by one person.

## Gear

| Item | Notes |
|---|---|
| Sony A7C | Full-frame. Internal 8-bit 4:2:0 XAVC S, 4K up to 30p, 1080p up to 120p, S-Log2/S-Log3/HLG, IBIS, one SD slot, 3.5mm mic input and headphone jack |
| 24mm prime | Wide: establishing shots, interiors, handheld, vlog |
| 85mm prime | Tele: portraits, interviews, compression, details |
| DJI Neo 2 | Small drone. Check specs, flight modes and local rules against DJI's and the aviation authority's official sources before relying on them |
| DJI Mic Mini 2 | Wireless mic kit. Check exact specs (transmitters, range, recording options) on DJI's official page before relying on them |
| Adobe Premiere Pro | Frank's editing software. He does **not** use DaVinci Resolve. He does not sell colour grading yet; since 27 Oct 2026 he is **learning colour grading in Premiere Pro** (see `projects/color-grading-course/`). Footage should look right straight out of camera; in Premiere only light correction (exposure, white balance, Lumetri basics) as part of an edit |
| ASUS TUF laptop | Editing machine. Exact model, CPU, GPU and RAM not recorded yet; ask Frank |

Not owned (as far as we know): lights, gimbal,
ND filters, tripod. Ask before assuming.

## The team board

The task board lives in the **live dashboard** (https://claude.ai/artifact/KRL7PmYwVCgQXfBdS1pVhA),
in its database. Only the team lead (main session) reads and writes it, with the `ArtifactData` tool:

- `tasks/<id>`: `{title, owner, project, status, priority, next, updated}`.
  `status` is one of `To do`, `In progress`, `Needs Frank`, `Done`; `priority` is `High`, `Medium` or `Low`;
  `owner` is the agent id from `team/roster.json`.
- `members/<agent id>`: `{name, role, focus, order}`.
- `activity/<id>`: `{at, by, text, sub}`, a short progress note. Keep it to about 30 entries; delete the oldest.
- `commands/<id>`: `{text, taskId, at, status, reply}` written when Frank taps or types a command on the
  dashboard. `status` goes `queued` → `working` → `done`; put a one-line `reply` on it when done.

Specialists don't write to the board. They return new tasks or status changes in their report, and
the team lead applies them.
