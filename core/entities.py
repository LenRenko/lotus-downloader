import os

from enum import Enum

DOWNLOAD_LIST = []  # urls in waiting list for download
COMPLETED_LIST = []  # urls of already downloaded songs

YOUTUBE_BASE = "https://www.youtube.com/watch?v="
COMPLETED = "Completed"
DOWNLOADING = "Downloading"
output_format = "MP3"
output_dir = os.path.expanduser("~\\LotusDownloaderOutput\\")

DEFAULT_SETTINGS = {
    "output_dir": output_dir,
    "output_format": output_format,
    "dark_mode": False,
}


class Format(Enum):
    MP3 = "MP3"
    M4A = "M4A"
    WAV = "WAV"
    OGG = "OGG"
    FLAC = "FLAC"


class TType(Enum):
    PL = "PL"
    S = "S"


class URLError(Exception):
    """Raised when bad url is entered for download"""

    pass
