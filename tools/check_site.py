#!/usr/bin/env python3
"""Small static release gate for the pages we own (legacy API docs excluded)."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, re
ROOT=Path(__file__).resolve().parents[1]
PAGES=['index.html','haven-under-fire/index.html','haven-under-fire/support/index.html','haven-under-fire/privacy/index.html','products/jasdb/index.html','support/index.html','privacy/index.html','404.html']
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__();self.ids=[];self.refs=[];self.h1=0;self.images=[];self.remote=[];self.canonical=[];self.title=False;self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='title':self.title=True
        if tag=='img':self.images.append(a)
        if tag=='link' and a.get('rel')=='canonical':self.canonical.append(a.get('href',''))
        for key in ('href','src'):
            if key in a:self.refs.append((tag,a.get('rel',''),a[key]))
        if tag in ('script','iframe','img') and a.get('src','').startswith(('http:','https:','//')):self.remote.append(a['src'])
        if tag=='link' and a.get('rel')=='stylesheet' and a.get('href','').startswith(('http:','https:','//')):self.remote.append(a['href'])
parsed={p:Page((ROOT/p).read_text()) for p in PAGES}
for name,page in parsed.items():
    assert page.h1==1,(name,'one h1 required')
    assert page.title and len(page.canonical)==1,(name,'metadata')
    assert len(set(page.ids))==len(page.ids),(name,'duplicate ID')
    assert not page.remote,(name,'unexpected remote resource')
    for image in page.images:assert all(k in image for k in ('alt','width','height')),(name,'image dimensions/alt')
    for tag,rel,ref in page.refs:
        assert ref and not ref.startswith('javascript:'),(name,'empty/unsafe link')
        u=urlsplit(ref)
        if u.scheme or u.netloc:continue
        dest=ROOT/u.path.lstrip('/') if u.path.startswith('/') else ROOT/name.rsplit('/',1)[0]/u.path if '/' in name else ROOT/u.path
        if not u.path:dest=ROOT/name
        if dest.is_dir():dest=dest/'index.html'
        assert dest.exists(),(name,'broken local link',ref)
        if u.fragment:
            target=str(dest.relative_to(ROOT));content=parsed.get(target)
            if content:assert unquote(u.fragment) in content.ids,(name,'missing anchor',ref)
    text=(ROOT/name).read_text()
    assert not any(s in text for s in ('google-analytics','platform.twitter.com','HomeAutomation','Coming soon link','Train Studio')),(name,'retired or unpublished content')
assert (ROOT/'CNAME').read_text().strip()=='www.oberasoftware.com'
assert not (ROOT/'jasdb').exists(),'Do not shadow the existing project documentation site'
products=json.loads((ROOT/'_data/products.json').read_text())
assert {p['id'] for p in products if p.get('published')}=={'haven-under-fire','jasdb'}
for product in products:
    if product.get('published'):assert (ROOT/product['url'].strip('/')/'index.html').exists()
assets=list((ROOT/'assets/products').rglob('*'))
assert all(p.stat().st_size<700_000 for p in assets if p.is_file()),'Optimize individual media below 700 KB'
print(f'PASS: {len(PAGES)} pages; local links/anchors, metadata, images, hosting identity and catalogue checked.')
print(f'Product media: {sum(p.stat().st_size for p in assets if p.is_file())/1024:.0f} KiB total. No third-party resource embeds.')
