#!/usr/bin/env python3
"""Filter everything known out of a piece of Chinese content"""

from collections import Counter
from datetime import datetime
import json
import re

import jieba

from common_va import is_cjk_ideograph

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Setup
# └─────────────────────────────────────────────────────────────────────────────
INPUT_FILE = r'C:\~\langs\zh\temp__1tingli read.txt'
SOURCE = 'tingli'  # 'spoonfed', 'tingli', or 'subs'
CHARSET = 's'  # t = traditional, s = simplified

# Load up necessary files
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    text = [line.strip() for line in f]

with open('seen_lemmas_zh.json', 'r', encoding='utf-8') as f:
    lemmas_seen = json.load(f)

with open(r'C:\~\langs\zh\CEDICT\cedict_ts.json', 'r', encoding='utf-8') as f:
    cedict = json.load(f)

jieba.load_userdict(rf'C:\~\langs\zh\CEDICT\cedict_{CHARSET}_jieba.txt')

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Filter
# └─────────────────────────────────────────────────────────────────────────────
new = []
for t in text:
    target = t.split('\t')[0]
    target = re.sub(r'<(.*?)>', '', target)

    lemmas_all = list(jieba.cut(target, cut_all=False))
    lemmas_real = [l for l in lemmas_all if l in cedict]  # Keep "real" lemmas
    lemmas_real_new = [l for l in lemmas_real if l not in lemmas_seen]

    for l in lemmas_real_new:
        lemmas_seen[l] = 1

    if lemmas_real_new: new.append(t)

with open(r'temp_new.txt', 'w+', newline='\n', encoding='utf-8') as f:
    f.write('\n'.join(new))

print(len(text))
print(len(new))
