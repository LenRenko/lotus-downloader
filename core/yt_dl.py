from __future__ import unicode_literals

import os
import yt_dlp as yt
import json

from .entities import Format, DOWNLOAD_LIST, COMPLETED_LIST, URLError, YOUTUBE_BASE

from threading import Thread


def set_options(dir: str, format: str, skip_dl: bool) -> dict:
    """
    Set options for youtube download
    """

    opts = {
        "writethumbnail": True,
        "ignoreerrors": True,
        "outtmpl": os.path.join(dir, "%(title)s.%(ext)s"),
        "ffmpeg_location": os.path.abspath("ffmpeg/bin"),
        "skip_download": skip_dl,
        "quiet": True,
    }

    if format in [Format.MP3.value]:
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": Format[format].value,
                "preferredquality": "1000",
            },
            {
                "key": "EmbedThumbnail",
            },
            {
                "key": "FFmpegMetadata",
            },
        ]
    else:
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": Format[format].value,
                "preferredquality": "1000",
            },
            {
                "key": "FFmpegMetadata",
            },
        ]
    return opts


## ==== Download === ##
def extract_song_info(url: str):
    with open(os.path.abspath("data/settings.json"), "r") as f:
        settings = json.load(f)
    yt_opt = set_options(
        settings["output_dir"], settings["output_format"], skip_dl=True
    )

    if url not in DOWNLOAD_LIST and url not in COMPLETED_LIST:
        DOWNLOAD_LIST.append(url)
    try:
        with yt.YoutubeDL(yt_opt) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info["title"]
            thumbnail = info["thumbnail"]

            return {"title": title, "thumbnail": thumbnail}
    except yt.utils.DownloadError:
        raise URLError


def extract_playlist_songs(url: str):
    playlist_titles = []
    playlist_thumbnails = []
    with open(os.path.abspath("data/settings.json"), "r") as f:
        settings = json.load(f)
    yt_opt = set_options(
        settings["output_dir"],
        settings["output_format"],
        skip_dl=True,
    )
    try:
        with yt.YoutubeDL(yt_opt) as ydl:
            info = ydl.extract_info(url, download=False)
            playlist_count = info["playlist_count"]

            for songs in info["entries"]:
                song_url = YOUTUBE_BASE + str(songs["id"])
                if song_url not in DOWNLOAD_LIST and song_url not in COMPLETED_LIST:
                    DOWNLOAD_LIST.append(song_url)
                    playlist_titles.append(songs["title"])
                    playlist_thumbnails.append(songs["thumbnail"])
            return {
                "playlist_titles": playlist_titles,
                "playlist_thumbnails": playlist_thumbnails,
                "playlist_count": playlist_count,
            }
    except yt.utils.DownloadError:
        raise URLError


class MonoYTExtractThread(Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.sonf_info = {}

    def run(self):
        try:
            self.song_info = extract_song_info(self.url)
            return self.song_info
        except Exception:
            pass


class YTExtractPlaylistThread(Thread):
    def __init__(self, url: str):
        super().__init__()
        self.url = url
        self.playlist_titles = []

    def run(self):
        try:
            self.playlist_titles = extract_playlist_songs(self.url)
            return self.playlist_titles
        except Exception:
            pass
