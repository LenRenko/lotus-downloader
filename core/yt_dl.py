from __future__ import unicode_literals

import os
import yt_dlp as yt
import json

from .entities import Format, DOWNLOAD_LIST, COMPLETED_LIST, URLError, YOUTUBE_BASE

from threading import Thread, Event
from PySide6.QtCore import Signal, QObject


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


# ===================================== #
class DownloadSignals(QObject):
    downloaded_signal = Signal(int)
    error_signal = Signal(str)


class YTDownloadManager(Thread):
    def __init__(self):
        super().__init__()
        self.song_list = []
        self.signals = DownloadSignals()
        self._stop_event = Event()
        self._pause_event = Event()
        self._pause_event.set()

    def run(self):
        print("Manager started :", self.ident)
        with open(os.path.abspath("data/settings.json"), "r") as f:
            settings = json.load(f)
        yt_opt = set_options(
            settings["output_dir"], settings["output_format"], skip_dl=False
        )
        for index, song_url in enumerate(self.song_list):
            if self._stop_event.is_set():
                break

            self._pause_event.wait()
            try:
                if song_url not in COMPLETED_LIST:
                    self.download_song(yt_opt, song_url)
                    self.signals.downloaded_signal.emit(index)
                    COMPLETED_LIST.append(song_url)
            except Exception:
                self.signals.error_signal.emit("Could not download song...")
        print("Manager exited")

    def download_song(self, yt_opt, url):
        try:
            with yt.YoutubeDL(yt_opt) as ydl:
                ydl.download([url])
        except yt.utils.DownloadError:
            raise URLError

    def set_song_list(self, song_list: list):
        self.song_list = song_list

    def stop(self):
        self._stop_event.set()
        self._pause_event.set()
        self.join(timeout=5.0)

    def pause(self):
        self._pause_event.clear()

    def resume(self):
        self._pause_event.set()
