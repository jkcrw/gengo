#!/usr/bin/env python3
"""Batch-rename files in a directory (2018/01/10)"""

import os
import re

root = r'C:\~\Languages\JA\SUBS2SRS\Monster\mp4'
os.chdir(root)

match_pattern = '.mp4'
filenames = [f for f in os.listdir() if match_pattern in f]

find = r'MONSTER'
repl = r'Monster'
for f in filenames:
    print(re.sub(find, repl, f))
    os.replace(f, re.sub(find, repl, f))
