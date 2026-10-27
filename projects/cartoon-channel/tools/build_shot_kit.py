"""Build shot-kit.html from episodes-v2.md and the location plates in character-bible.md.
Usage: python3 -I build_shot_kit.py  (run from anywhere)"""
import json, re, os
base = os.path.dirname(os.path.abspath(__file__)) + '/../'
ep_md = open(base + 'episodes-v2.md').read()
bible = open(base + 'character-bible.md').read()
LOCFILE = {'tea stall lane': 'loc-lane.png', 'rooftop': 'loc-rooftop.png',
           'home doorstep in rain': 'loc-home-doorstep-rain.png', 'home': 'loc-home.png'}

def bullet(text, name):
    m = re.search(r'- \*\*' + re.escape(name) + r'[^*]*\*\*:?\s*(.*)', text)
    return m.group(1).strip().strip('`') if m else ''

def section(text, name):
    part = text.split('### ' + name, 1)
    return part[1].split('\n###', 1)[0].split('\n---', 1)[0] if len(part) > 1 else ''

episodes = []
for chunk in re.split(r'\n## Episode ', ep_md)[1:]:
    head, _, rest = chunk.partition('\n')
    num, title = head.split(' · ', 1)
    loc_name = bullet(rest, 'Location')
    key = next((k for k in LOCFILE if loc_name.lower().startswith(k)), '')
    ep = {'num': int(num), 'title': title.strip(), 'logline': bullet(rest, 'Logline'),
          'location': loc_name, 'props': bullet(rest, 'Props'), 'caption': bullet(rest, 'Hook caption'),
          'descline': bullet(rest, 'Description, first line'), 'hashtags': bullet(rest, 'Hashtags')}
    shots = []
    for m in re.finditer(r'\*\*Shot (\d+[A-D]) · (.+?) · edit (.+?)\*\*\s*\nWhat we see:\s*(.*?)\n+```text\n(.*?)\n```', rest, re.S):
        sid, beat, edit, see, prompt = m.groups()
        chars = [c for c in ('Mishti', 'Moto') if c in prompt]
        loc = LOCFILE.get(key, '')
        if 'lane' in prompt and loc.startswith('loc-home') and 'rain' not in prompt: loc = 'loc-lane.png'
        shots.append({'id': sid, 'beat': beat, 'edit': edit, 'see': see.strip(), 'prompt': prompt.strip(),
                      'chars': chars, 'loc': loc})
    ep['shots'] = shots
    ep['edit'] = [l[2:].strip() for l in section(rest, 'Edit').splitlines() if l.startswith('- ')]
    ep['sfx'] = [l[2:].strip() for l in section(rest, 'Sound effects list').splitlines() if l.startswith('- ')]
    episodes.append(ep)

plates = [{'file': m.group(1), 'prompt': m.group(2).strip()} for m in re.finditer(
    r'`(loc-[\w-]+\.png)`[^\n]*\n```text\n(.*?)\n```', bible.split('### 5.6 Location plates', 1)[1].split('\n---', 1)[0], re.S)]

assert len(episodes) == 7 and all(len(e['shots']) == 4 for e in episodes), [len(e['shots']) for e in episodes]
assert len(plates) == 4 and all(e['caption'] and e['edit'] and e['sfx'] for e in episodes)
tpl = open(base + 'tools/shot-kit-template.html').read()
data = json.dumps({'episodes': episodes, 'plates': plates}, ensure_ascii=False).replace('</', '<\\/')
open(base + 'shot-kit.html', 'w').write(tpl.replace('/*DATA*/null', data))
for e in episodes: print(e['num'], e['caption'], [(s['id'], s['chars'], s['loc']) for s in e['shots']])
