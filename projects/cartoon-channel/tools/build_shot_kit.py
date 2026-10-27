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
# EP01 pro pilot (keyframes + Frames to Video)
pmd = open(base + 'ep01-pilot-pro.md').read()
rows = {}
for line in pmd.split('## 4 · Shot list', 1)[1].split('## 5', 1)[0].splitlines():
    c = [x.strip() for x in line.strip().strip('|').split('|')]
    if len(c) == 9 and re.match(r'S\d\d$', c[0]):
        rows[c[0]] = {'edit': c[1], 'size': c[3], 'move': c[5], 'see': re.sub(r'\*\*', '', c[6]), 'cut': re.sub(r'\*\*', '', c[7])}
pshots = []
for chunk in re.split(r'\n### (?=S\d\d · )', pmd.split('## 5 ·', 1)[1].split('\n## 6', 1)[0])[1:]:
    head = chunk.split('\n', 1)[0].strip()
    sid = head[:3]
    def block(label):
        m = re.search(r'\*\*' + label + r'\*\*([^\n]*)\n```text\n(.*?)\n```', chunk, re.S)
        return (m.group(1).strip(), m.group(2).strip()) if m else ('', '')
    sk, ek, vp = block('Start keyframe'), block('End keyframe'), block('Flow video prompt')
    pshots.append(dict(id=sid, head=head, start=sk[1], startnote=sk[0], end=ek[1], endnote=ek[0], video=vp[1], **rows.get(sid, {})))
stage = pmd.split('## 2 · Staging map', 1)[1].split('```text\n', 1)[1].split('\n```', 1)[0]
assert len(pshots) == 11 and all(p['start'] and p['video'] and p.get('edit') for p in pshots)
pilot = {'shots': pshots, 'map': stage,
         'rules': ['Moto সবসময় screen-right-এ মুখ করে, Mishti screen-left-এ। Mishti-র লাফ ডান থেকে বাঁয়ে।',
                   'Cone সবসময় Moto-র ডান থাবায়; থাবা কখনো খোলে না।',
                   'নিচে হলুদ scoop, উপরে সবুজ। সংখ্যা: ২, তারপর ১, তারপর আবার ২।',
                   'আলো: সকাল সাড়ে ১০টা, রোদ camera-র বাঁ দিক থেকে। পুরো পর্বে একই।',
                   'চায়ের দোকান সবসময় ডানে, রিকশা বাঁয়ে। উল্টো দেখলে take-টা mirror হয়েছে।']}
tpl = open(base + 'tools/shot-kit-template.html').read()
data = json.dumps({'episodes': episodes, 'plates': plates, 'pilot': pilot}, ensure_ascii=False).replace('</', '<\\/')
open(base + 'shot-kit.html', 'w').write(tpl.replace('/*DATA*/null', data))
for e in episodes: print(e['num'], e['caption'], [(s['id'], s['chars'], s['loc']) for s in e['shots']])
