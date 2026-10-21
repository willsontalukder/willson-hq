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
| ASUS TUF laptop | Editing machine. Exact model, CPU, GPU and RAM not recorded yet; ask Frank |

Not owned (as far as we know): lights, gimbal,
ND filters, tripod. Ask before assuming.

## The team board

`team/board.json` is the task list shown on Frank's dashboard
(https://claude.ai/artifact/T8T6R7Xy33u1VNk6RNG1yC). Each task:

```json
{"id": "T14", "title": "…", "owner": "james", "project": "…", "status": "To do", "priority": "High",
 "ask": "…", "next": "…", "updated": "YYYY-MM-DD"}
```

- `status` is one of `To do`, `In progress`, `Needs Frank`, `Done`.
- `priority` is one of `High`, `Medium`, `Low`.
- `owner` is the agent id from `team/roster.json`.
- `ask` (only when status is `Needs Frank`): one short question Frank must answer.
- `next`: one line on what the disciple does next.

When a task starts, finishes or gets blocked on Frank, update its status and `updated` date,
then refresh the dashboard (re-upload `board.json` to the dashboard's Task board source).
