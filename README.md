A [yt-dlp](https://github.com/yt-dlp/yt-dlp) extractor [plugin](https://github.com/yt-dlp/yt-dlp#plugins) for using custom Youtube chapter lists

---

## Usage

Pass `--extractor-args "youtube:chapters_file=/path/to/chapters.txt"` with your yt-dlp command to have the Youtube extractor parse the given text file for chapters.

The text file should be formatted with 1 chapter per line, with a line structure of `START:TIME Chapter Name`, e.g.:

```
00:00 Introduction
01:15 Beginning
02:40 Middle
04:20 End
```


## Installation

Requires yt-dlp `2023.01.02` or above.

You can download the wheel of the [latest release](https://github.com/bashonly/yt-dlp-YTCustomChapters/releases/latest) and place the `.whl` file in one of [yt-dlp's plugin paths](https://github.com/yt-dlp/yt-dlp#installing-plugins).

Or you can install this package with pip:
```
python3 -m pip install -U https://github.com/bashonly/yt-dlp-YTCustomChapters/archive/master.zip
```

See [the plugins section of the yt-dlp README](https://github.com/yt-dlp/yt-dlp#installing-plugins) for more information.
