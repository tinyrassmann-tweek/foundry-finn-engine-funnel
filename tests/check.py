from pathlib import Path
import json
from html.parser import HTMLParser
from urllib.parse import urlparse, parse_qs
r=Path(__file__).resolve().parents[1]
m=json.loads((r/'config/ventures.json').read_text())
v=m['ventures']; assert m['ventureCount']==len(v)==12
assert len({x['slug'] for x in v})==12
assert {'my-ancestry-lives','my-ancestry-speaks'} <= {x['slug'] for x in v}
class Page(HTMLParser):
 def __init__(self): super().__init__(); self.links=[]; self.ids=set()
 def handle_starttag(self,t,a):
  a=dict(a)
  if 'id' in a: self.ids.add(a['id'])
  if t=='a' and 'href' in a: self.links.append(a['href'])
def parse(p):
 h=Page(); h.feed(p.read_text()); return h
for x in v:
 h=parse(r/'components'/f"{x['slug']}.html")
 assert h.links==[x['entryUrl']],x['slug']
 u=urlparse(h.links[0]); assert f'{u.scheme}://{u.netloc}{u.path}'==m['engineUrl']
 assert parse_qs(u.query)['utm_source']==[x['slug']]
for name in ['index.html','banner-preview.html']:
 h=parse(r/name)
 for link in h.links:
  if link.startswith('#'): assert link[1:] in h.ids,(name,link)
  else:
   u=urlparse(link); assert f'{u.scheme}://{u.netloc}{u.path}'==m['engineUrl'],link
print('PASS: 12 venture snippets, distinct ancestry entries, referral destinations, and local anchors (static only).')
