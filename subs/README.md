# Subtitle Processing Procedures

<!-- MarkdownTOC levels="1,2" -->

- [JA Procedure](#ja-procedure)
- [ES Procedure](#es-procedure)
- [Archived](#archived)

<!-- /MarkdownTOC -->

## JA Procedure
_Updated 2022/10/18_

1. Download MP4s and SRTs using Anystream (or Netflix Subtitle Downloader/Flixgrab as backup).
2. `rename_files.py` to simplify/standardize filenames.
3. `vtt_to_srt.py` to convert to SRT + build fulltext.
4. `analyze_ja.py` to analyze fulltext and supplement target word list.
5. `target_words.txt` make one for content using manual notes + analysis results.
6. `filter.py` to filter subtitle files against target words.
7. `massage_target_words_ja.py` to figure out best jamdict output.
8. `subs2srs.exe` to generate Anki TSV/clips.
    - Subs1: C:\~\lang\ja\subs2srs\Gintama\subs_ja\filtered\Gintama_*_ja.srt
    - Output: C:\~\lang\ja\subs2srs\Gintama
    - Video: C:\~\lang\ja\subs2srs\Gintama\mp4\Gintama_*.mp4
    - Generate Video Clips: 720x480
    - Pad Timings: 1000ms / 1000ms
9. `postprocess_subs2srs_tsv_ja.py` to post-process Anki TSV.
10. Import into Anki.


## ES Procedure
_Updated 2022/06/07_

1. Identify movies of interest on Language Reactor.
2. Download MP4s and SRTs using Anystream (or Netflix Subtitle Downloader/Flixgrab as backup).
3. Convert to SRT + build fulltext using `vtt_to_srt.py`.
4. Analyze fulltext using `analyze_es.py`.
5. Glue subs using `glue.py`.
6. Generate Anki TSV/clips using `subs2srs.exe`.
7. Import into Anki.



## Archived
### `2022/04/15` Holy Power Combo
- **Netflix / [LanguageReactor](https://www.languagereactor.com/) + AnyStream + [subs2srs](http://subs2srs.sourceforge.net)**
- Flixgrab + [Netflix Subtitle Downloader](https://greasyfork.org/en/scripts/26654-netflix-subtitle-downloader)
    + Before this line: `result = await Promise.race([resultPromise, progress.stop, asyncSleep(30, STOP_THE_DOWNLOAD)]);`
    + Add this to be more respectful: `await asyncSleep(15);`


### `2018/01/08` Subtitle Sources
- [D-Addicts](http://www.d-addicts.com/forums/page/subtitles#Japanese)
- [Project Modelino](http://project-modelino.com/movies.php?site_language=english&learn_language=japanese#top_of_page)
- [Kitsunekko](http://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F)


### `2018/01/14` Lessons Learned So Far
- Given how long it takes to work through (study) each 25ish-episode series and the fact that you basically already know Japanese (you’re far into 20% land), it only makes sense to SUBS2SRS the very VERY best shows. Your time is precious, and your Japanese is already good enough that it doesn’t make sense to spend a lot of time on this project.
    + Done. Have all candidate shows sorted by MAL rating.
- Looking at some rough numbers, you should be looking to do about 50 episodes per year (that’s about 2000 36 second cards per year or 6 such cards per day, which I know to be a comfortable, sustainable amount).
- I guess shows with fewer than 25ish episodes per season are also better because you get exposed to more different contexts.


### `2018/01/11` Anki Card Creation Workflow
1. If subtitles in ASS format, [convert to SRT](https://lab.sorz.org/tools/asstosrt/?lang=en) (make sure to use UTF-8 encoding).
2. Glue up the subtitles using `glue_srt.py`.
3. Use DVD Decrypter to pull VIDEO_TS data.
4. Use Subrip to pull English subtitles (or find on Kitsunekko).
5. Use Handbrake to encode videos.
6. Use SUBS2SRS to make cards.


### `2018/01/16` Candidate Show List Update Workflow
1. Pull any new shows from Kitsunekko using `scrape_kitsunekko.py`.
2. Pull the data for those new shows using `scrape_MAL.py`.
3. Put new show data in `SUBS2SRS.xlsx` for sorting.


### `2015/11/11` Ghost in the Shell Plan of Attack
| Title                               | KCLS | Price |
|:------------------------------------|:-----|:------|
| Ghost in the Shell (Original movie) | Yes  | -     |
| Ghost in the Shell 2: Innocence     | No   | $3    |
| Stand Alone Complex 2nd Gig         | No   | $33   |
| Solid State Society                 | Yes  | -     |
| Arise Borders 1 2 3 4               | Yes  | -     |
| Ghost in the Shell The New Movie    | ?    | ?     |
| Arise Border 5                      | ?    | ?     |
