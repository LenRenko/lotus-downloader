import json
import os

from qt_material import apply_stylesheet
from PySide6.QtWidgets import QApplication

def init_theme(app: QApplication):
    if os.path.exists("data/settings.json"):
        with open("data/settings.json", "r") as f:
            settings = json.load(f)
        
        if settings["dark_mode"]:
            apply_stylesheet(app, theme="dark_amber.xml")
        else:
            apply_stylesheet(app, theme="light_amber.xml", invert_secondary=True)
    else:
        apply_stylesheet(app, theme="dar_amber.xml")
