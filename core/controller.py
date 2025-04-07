import json
import os
import re

from PySide6.QtWidgets import QApplication
from qt_material import apply_stylesheet


def init_theme(app: QApplication):
    if os.path.exists("data/settings.json"):
        with open("data/settings.json", "r") as f:
            settings = json.load(f)

        if settings["dark_mode"]:
            apply_stylesheet(app, theme="dark_amber.xml")
        else:
            apply_stylesheet(app, theme="light_amber.xml", invert_secondary=True)
    else:
        apply_stylesheet(app, theme="dark_amber.xml")


# == Youtube controllers == #


def is_youtube_playlist_url(url):
    # Playlist ID usually starts with PL, LL, FL or UU and has 16–34 chars
    pattern = r"(https?://)?(www\.)?youtube\.com/.*[?&]list=([a-zA-Z0-9_-]+)"
    return re.search(pattern, url) is not None


def is_youtube_url(url):
    pattern = r"(https?://)?(www\.)?(youtube\.com|youtu\.be)/(watch\?v=|v/|embed/)?[a-zA-Z0-9_-]{11}"
    return re.search(pattern, url) is not None


if __name__ == "__main__":
    print(
        is_youtube_url(
            "https://www.youtube.com/watch?v=PO9UC2Zt59c&list=PL3pZ_4pol-jrq92ptfWed2E8_R9R_FC8R"
        )
    )
