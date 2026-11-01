#!/usr/bin/env python3
"""Exporta PNGs de todas as peças HTML em exportados/ (Playwright + chromium.launch()).
Uso: python3 render.py [filtro_de_ID]   ex.: python3 render.py BAN-0
Carrosséis: um PNG por slide (CAR-01_s1.png...)."""
import os, sys, re, glob
from playwright.sync_api import sync_playwright
BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "exportados")
filtro = sys.argv[1] if len(sys.argv) > 1 else ""
def size_of(path):
    m = re.search(r'class="a(?: slide)?" style="width:(\d+)px;height:(\d+)px', open(path, encoding="utf-8").read())
    return int(m.group(1)), int(m.group(2))
n = 0
with sync_playwright() as p:
    b = p.chromium.launch()
    for f in sorted(glob.glob(os.path.join(BASE, "pecas", "*", "*.html"))):
        pid = os.path.basename(f)[:-5]
        if filtro not in pid: continue
        w, h = size_of(f)
        pg = b.new_page(viewport={"width": w, "height": h})
        pg.goto("file://" + f); pg.wait_for_load_state("load")
        os.makedirs(OUT, exist_ok=True)
        slides = pg.query_selector_all(".slide")
        if slides:
            for i, s in enumerate(slides, 1):
                s.screenshot(path=os.path.join(OUT, f"{pid}_s{i}.png")); n += 1
        else:
            pg.screenshot(path=os.path.join(OUT, f"{pid}.png"), clip={"x": 0, "y": 0, "width": w, "height": h}); n += 1
        pg.close()
    b.close()
print(n, "PNGs em", OUT)
