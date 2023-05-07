#!/usr/bin/env python3
"""Filter subtitles against target words/phrases"""

from collections import deque
import os
from statistics import mean

import pysrt

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Initialization
# └─────────────────────────────────────────────────────────────────────────────
TARGET_WORD_FILE = r'C:\~\lang\ja\subs2srs\World Trigger\target_words.txt'
MAX_DURATION_MS = 11000
MAX_DEADTIME_MS = 7500

root_main = os.path.dirname(TARGET_WORD_FILE)
root_srt = root_main + '/subs_ja/srt/'
root_filtered = root_main + '/subs_ja/filtered/'
os.makedirs(root_filtered, exist_ok=True)

# ┌─────────────────────────────────────────────────────────────────────────────
# │ Helper Functions
# └─────────────────────────────────────────────────────────────────────────────
def build_context(srt: pysrt.SubRipFile, i_init: int, i_main: int) -> pysrt.SubRipItem:
    """Bidirectionally expand context around entry sub up to reasonable duration."""
    duration_ok = lambda buffer: (buffer[-1].end.ordinal - buffer[0].start.ordinal) <= MAX_DURATION_MS

    buffer = deque([srt[i_init]])
    direction, stride, i_cand = 1, 0, 0
    while True:
        if direction > 0: stride += 1
        direction *= -1
        i_cand = i_init + stride * direction

        is_in_bounds = 0 <= i_cand < len(srt)
        if not is_in_bounds: continue

        sub_cand = srt[i_cand]
        lo, hi = (sub_cand, buffer[0]) if direction < 0 else (buffer[-1], sub_cand)
        deadtime = hi.start.ordinal - lo.end.ordinal
        if deadtime >= MAX_DEADTIME_MS: continue

        temp_buffer = [buffer[0], sub_cand]
        if not duration_ok(temp_buffer): break

        buffer.appendleft(sub_cand) if direction < 0 else buffer.append(sub_cand)

    new_sub = glue_subs(i_main, list(buffer))
    return new_sub


def glue_subs(index: int, buffer: list[pysrt.SubRipItem]) -> pysrt.SubRipItem:
    """Combine list of subs into a single sub."""
    start, end = buffer[0].start, buffer[-1].end
    text = ' '.join([sub.text_without_tags for sub in buffer])
    glued = pysrt.SubRipItem(index, start, end, text)
    return glued


def main():
    # Load target words and SRT files
    with open(TARGET_WORD_FILE, 'r', encoding='utf-8') as f:
        target_words = [line.strip() for line in f]

    for root, dirs, files in os.walk(root_srt):
        srt_files = files

    # Main loop
    total_subs, mean_durations = 0, []
    for filename in srt_files:
        filtered_subs, pure_texts = [], set()
        srt = pysrt.open(root_srt + filename)

        i_main = 1
        for i_init, sub in enumerate(srt):
            for word in target_words:
                if word in sub.text:
                    new_sub = build_context(srt, i_init, i_main)
                    if new_sub.text not in pure_texts:
                        filtered_subs.append(new_sub)
                        pure_texts.add(new_sub.text)
                        target_words.remove(word)
                        i_main += 1

        srt.data = filtered_subs
        output_filename = root_filtered + filename
        srt.save(output_filename, encoding='utf-8')

        if filtered_subs:
            mean_duration = mean([sub.end.ordinal - sub.start.ordinal for sub in filtered_subs])
            mean_durations.append(mean_duration)
        total_subs += len(filtered_subs)

    print(f'target_words: {target_words}')
    print(f'mean_duration: {mean(mean_durations):.0f}')
    print(f'total_subs: {total_subs}')


if __name__ == '__main__':
    main()
