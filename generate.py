from jinja2 import Environment, FileSystemLoader, select_autoescape
import os
import json
from pathlib import Path
from operator import itemgetter

env = Environment(
    loader=FileSystemLoader("templates"),
    autoescape=select_autoescape()
)

records_root = Path('./records')
target = Path('index.html')

items = []
for fn in records_root.glob("*.json"):
    with fn.open() as f:
        data = json.load(f)
        items.append(data)

items.sort(key=itemgetter('timestamp'), reverse=True)
template = env.get_template("index.html")
with target.open('w') as f:
    f.write(template.render(items=items))
