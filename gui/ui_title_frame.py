from PySide6.QtCore import QCoreApplication, QMetaObject, Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QCheckBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QSizePolicy,
    QSpacerItem,
)

import requests


class Ui_Frame(QFrame):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName("Frame")
        Frame.resize(276, 40)
        self.gridLayout = QGridLayout(Frame)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.thumbnail_label = QLabel(Frame)
        self.thumbnail_label.setObjectName("thumbnail_label")

        self.horizontalLayout.addWidget(self.thumbnail_label)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.title_label = QLabel(Frame)
        self.title_label.setObjectName("title_label")

        self.horizontalLayout.addWidget(self.title_label)

        self.dl_check = QCheckBox(Frame)
        self.dl_check.setObjectName("dl_check")
        self.dl_check.setCheckable(False)

        self.horizontalLayout.addWidget(self.dl_check)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", "Frame", None))
        self.thumbnail_label.setText(
            QCoreApplication.translate("Frame", "thumbnail", None)
        )
        self.title_label.setText(QCoreApplication.translate("Frame", "title", None))
        self.dl_check.setText("")

    # retranslateUi

    def check_downloaded(self):
        self.dl_check.setChecked(True)

    def set_title(self, title):
        self.title_label.setText(title)

    def set_thumbnail(self, thumbnail):
        pixmap = self.get_thumbnail(thumbnail)
        if pixmap:
            self.thumbnail_label.setPixmap(
                pixmap.scaled(
                    160,
                    90,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation,
                )
            )
        else:
            self.thumbnail_label.setText("Missing thumbnail")

    def get_thumbnail(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                pix = QPixmap()
                pix.loadFromData(response.content)
                return pix
        except Exception:
            pass
        return None
