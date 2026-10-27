import json, re, sys
base = '/home/user/willson-hq/projects/cartoon-channel/'
ep_md = open(base + 'episodes-01-07.md').read()
bible = open(base + 'character-bible.md').read()

LOCS = {
    'loc-lane.png': 'narrow, cheerful old-Dhaka-inspired lane',
    'loc-rooftop.png': 'sunny flat rooftop',
    'loc-home.png': 'small, cosy one-room home',
}

episodes = []
for chunk in re.split(r'\n## Episode ', ep_md)[1:]:
    head, _, rest = chunk.partition('\n')
    num, title = head.split(' · ', 1)
    def bullet(name):
        m = re.search(r'- \*\*' + re.escape(name) + r'[^*]*\*\*:?\s*(.*)', rest)
        return m.group(1).strip() if m else ''
    ep = {
        'num': int(num), 'title': title.strip(),
        'logline': bullet('Logline'), 'feeling': bullet('The one feeling'),
        'location': re.sub(r'\*\*', '', bullet('Location')),
        'props': bullet('Props'),
        'descline': bullet('Description, first line'),
        'hashtags': bullet('Hashtags'),
    }
    sb = rest.split('### Storyboard', 1)[1].split('###', 1)[0]
    rows = {}
    for line in sb.splitlines():
        cells = [c.strip() for c in line.strip().strip('|').split('|')]
        if len(cells) == 4 and re.match(r'\d+\.\d+', cells[0]):
            rows[cells[0]] = cells[3]
    shots = []
    for m in re.finditer(r'\*\*Shot (\d+\.\d+) · (.+?) · edit (.+?)\*\*\s*\n+```text\n(.*?)\n```', rest, re.S):
        sid, beat, edit, prompt = m.groups()
        ingr = []
        if 'Mishti is a tiny' in prompt: ingr.append('Mishti')
        if 'Moto is a big' in prompt: ingr.append('Moto')
        loc = next((f for f, k in LOCS.items() if k in prompt), '')
        if loc == 'loc-home.png' and re.search(r'\brain', prompt.split('Shot (')[0]):
            loc = 'loc-home-doorstep-rain.png'
        shots.append({'id': sid, 'beat': beat, 'edit': edit, 'see': rows.get(sid, ''),
                      'prompt': prompt.strip(), 'chars': ingr, 'loc': loc})
    ep['shots'] = shots
    sfx = rest.split('### Sound effects list', 1)[1].split('###', 1)[0]
    ep['sfx'] = [l[2:].strip() for l in sfx.splitlines() if l.startswith('- ')]
    episodes.append(ep)

plates = []
sec = bible.split('### 5.6 Location plates', 1)[1].split('\n---', 1)[0]
for m in re.finditer(r'`(loc-[\w-]+\.png)`[^\n]*\n```text\n(.*?)\n```', sec, re.S):
    plates.append({'file': m.group(1), 'prompt': m.group(2).strip()})

assert len(episodes) == 7 and all(len(e['shots']) == 7 for e in episodes), [len(e['shots']) for e in episodes]
assert len(plates) == 4
data = {'episodes': episodes, 'plates': plates}
tpl = open(sys.argv[1]).read()
open(sys.argv[2], 'w').write(tpl.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False).replace('</', '<\\/')))
print('ok', sum(len(e['shots']) for e in episodes), [e['shots'][0]['loc'] for e in episodes])
