### JA SUBS2SRS Procedure (2022/10/18)
1. Download MP4s and SRTs using Anystream (or Netflix Subtitle Downloader/Flixgrab as backup).
2. `rename_files.py` to simplify/standardize filenames.
3. `vtt_to_srt.py` to convert to SRT + build fulltext.
4. `analyze_ja.py` to analyze fulltext and supplement target word list.
5. `target_words.txt` make one for content using manual notes + analysis results.
6. `filter.py` to filter subtitle files against target words.
7. `massage_target_words_ja.py` to figure out best jamdict output.
8. `subs2srs.exe` to generate Anki TSV/clips.
9. `postprocess_subs2srs_tsv_ja.py` to post-process Anki TSV.
10. Import into Anki.

### ES SUBS2SRS Procedure (2022/06/07)
1. Identify movies of interest on Language Reactor.
2. Download MP4s and SRTs using Anystream (or Netflix Subtitle Downloader/Flixgrab as backup).
3. Convert to SRT + build fulltext using `vtt_to_srt.py`.
4. Analyze fulltext using `analyze_es.py`.
5. Glue subs using `glue.py`.
6. Generate Anki TSV/clips using `subs2srs.exe`.
7. Import into Anki.
