# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowtiYpZS.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import json
import os

from PySide6.QtCore import QCoreApplication, QMetaObject, QTimer, QRect, QSize
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QSpacerItem,
    QStatusBar,
    QToolButton,
    QVBoxLayout,
    QWidget,
    QMessageBox,
    QCheckBox,
)


from .ui_settings_dialog import Ui_SettingsDialog
from .ui_title_frame import Ui_Frame
from core.entities import DEFAULT_SETTINGS, DOWNLOAD_LIST, COMPLETED_LIST, TType
from core.yt_dl import MonoYTExtractThread, YTExtractPlaylistThread, DownloadManager
from core.controller import is_youtube_url, is_youtube_playlist_url


class Ui_MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.download_manager = DownloadManager(
            max_concurrent=5, update_ui_callback=self.on_song_downloaded
        )
        self.download_manager.download_finished.connect(self.on_download_finished)

        self._downloading = False

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(1200, 800))
        icon = QIcon("gui/static/exe_icon.ico")
        MainWindow.setWindowIcon(icon)
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName("main_widget")
        self.gridLayout_3 = QGridLayout(self.main_widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        # = Settings button = #
        self.toolButton = QToolButton(self.main_widget)
        self.toolButton.setObjectName("toolButton")
        self.toolButton.setFixedSize(QSize(60, 40))
        self.toolButton.setIconSize(QSize(50, 40))
        icon1 = QIcon("gui/static/material_setting_icon_1.png")
        self.toolButton.setIcon(icon1)

        self.toolButton.clicked.connect(self.open_settings)

        self.horizontalLayout_4.addWidget(self.toolButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.top_left_spacer = QSpacerItem(
            0, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.top_left_spacer)

        self.top_label_img = QLabel(self.main_widget)
        self.top_label_img.setObjectName("top_label_img")

        self.horizontalLayout_2.addWidget(self.top_label_img)

        self.top_right_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_2.addItem(self.top_right_spacer)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        # = INPUT = #
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.separator_top = QFrame(self.main_widget)
        self.separator_top.setObjectName("separator_top")
        self.separator_top.setFrameShape(QFrame.HLine)
        self.separator_top.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.separator_top)

        self.input_main_vlayout = QVBoxLayout()
        self.input_main_vlayout.setObjectName("input_main_vlayout")
        self.input_line = QLineEdit(self.main_widget)
        self.input_line.setObjectName("input_line")
        self.input_line.returnPressed.connect(self.on_url_add)
        self.input_line.setPlaceholderText("Paste URL here...")

        self.input_main_vlayout.addWidget(self.input_line)

        self.add_btn_hlayout = QHBoxLayout()
        self.add_btn_hlayout.setObjectName("add_btn_hlayout")
        self.add_btn_left_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.add_btn_hlayout.addItem(self.add_btn_left_spacer)

        self.add_btn = QPushButton(self.main_widget)
        self.add_btn.setObjectName("add_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy1)
        self.add_btn.clicked.connect(self.on_url_add)

        self.add_btn_hlayout.addWidget(self.add_btn)

        self.add_btn_right_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.add_btn_hlayout.addItem(self.add_btn_right_spacer)

        self.input_main_vlayout.addLayout(self.add_btn_hlayout)

        self.verticalLayout_2.addLayout(self.input_main_vlayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.warning_label = QLabel(self.main_widget)
        self.warning_label.setObjectName("warning_label")

        self.horizontalLayout.addWidget(self.warning_label)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.separator_bottom = QFrame(self.main_widget)
        self.separator_bottom.setObjectName("separator_bottom")
        self.separator_bottom.setFrameShape(QFrame.HLine)
        self.separator_bottom.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.separator_bottom)

        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        # == LIST == #
        self.frame_pool = []

        self.dl_list_frame = QFrame(self.main_widget)
        self.dl_list_frame.setObjectName("dl_list_frame")
        self.dl_list_frame.setFrameShape(QFrame.StyledPanel)
        self.dl_list_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.dl_list_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.dl_progress_bar = QProgressBar(self.dl_list_frame)
        self.dl_progress_bar.setObjectName("dl_progress_bar")
        self.dl_progress_bar.setValue(0)

        self.horizontalLayout_3.addWidget(self.dl_progress_bar)

        self.count_label = QLabel(self.dl_list_frame)
        self.count_label.setObjectName("count_label")

        self.horizontalLayout_3.addWidget(self.count_label)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.dl_scroll_area = QScrollArea(self.dl_list_frame)
        self.dl_scroll_area.setObjectName("dl_scroll_area")
        self.dl_scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_area_content.setObjectName("scroll_area_content")
        self.scroll_area_content.setGeometry(QRect(0, 0, 756, 331))
        self.scroll_layout = QVBoxLayout()
        self.scroll_area_content.setLayout(self.scroll_layout)
        self.dl_scroll_area.setWidget(self.scroll_area_content)

        self.verticalLayout.addWidget(self.dl_scroll_area)

        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.gridLayout_2.addWidget(self.dl_list_frame, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.dl_btn_left_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.dl_btn_left_spacer)
        # == DL BTN == #
        self.dl_button = QPushButton(self.main_widget)
        self.dl_button.setObjectName("dl_button")
        self.dl_button.clicked.connect(self.start_download)

        self.horizontalLayout_5.addWidget(self.dl_button)

        self.dl_btn_right_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.horizontalLayout_5.addItem(self.dl_btn_right_spacer)

        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.main_widget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Lotus Youtube Downloader", None)
        )
        self.toolButton.setText(QCoreApplication.translate("MainWindow", "...", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", "Add", None))
        self.count_label.setText(QCoreApplication.translate("MainWindow", "0/0", None))
        self.dl_button.setText(
            QCoreApplication.translate("MainWindow", "Download", None)
        )

    def closeEvent(self, event):
        if self._downloading:
            reply = QMessageBox.warning(
                self,
                "Download in progress",
                "Download still running, do you want to quit ?",
                QMessageBox.Yes | QMessageBox.No,
            )

            if reply == QMessageBox.Yes:
                self.download_manager.stop_download()
                event.accept()
            else:
                event.ignore()
        else:
            event.accept()

    # =====                 ===== #
    # ======    EVENTS     ====== #
    # =====                 ===== #
    def on_url_add(self):
        self.clear_warning()
        url = self.input_line.text()
        if is_youtube_playlist_url(url):
            self.show_yes_no_dialog()
        elif is_youtube_url(url):
            if url not in DOWNLOAD_LIST:
                info_thread = MonoYTExtractThread(url)
                info_thread.start()
                self.monitor(info_thread, TType.S)
        else:
            self.display_warning_msg("Not a valid URL", "red")

    # == OPE == #
    def get_song_info(self, url: str):
        if url not in DOWNLOAD_LIST:
            info_thread = MonoYTExtractThread(url)
            info_thread.start()
            self.monitor(info_thread)
        else:
            self.display_warning_msg("Song already in list", "red")

    def get_playlist_info(self, url: str):
        playlist_thread = YTExtractPlaylistThread(url)
        playlist_thread.start()
        self.monitor(playlist_thread, TType.PL)

    def add_song_frame(self, title: str, thumbnail: str):
        """Add a Ui_Frame to the list scroll area"""
        frame = QFrame()
        ui = Ui_Frame()
        ui.setupUi(frame)
        ui.set_title(title)
        ui.set_thumbnail(thumbnail)

        self.scroll_layout.addWidget(frame)
        self.frame_pool.append(frame)

    def start_download(self):
        self.lock_btns(True)
        self.display_warning_msg("Downloading...", "orange")
        self._downloading = True
        if not DOWNLOAD_LIST or len(DOWNLOAD_LIST) == len(COMPLETED_LIST):
            self.display_warning_msg("Nothing to download", "red")
            self.dl_button.setEnabled(True)
        else:
            for index, url in enumerate(DOWNLOAD_LIST):
                if url not in COMPLETED_LIST:
                    self.download_manager.add_song(url, index)

    # == UTILS == #
    def monitor(self, thread, ttype=None):
        if thread.is_alive():
            QTimer.singleShot(500, lambda: self.monitor(thread, ttype))
            self.display_warning_msg("...Adding songs to list...", "orange")
            self.dl_button.setEnabled(False)
            self.dl_progress_bar.setRange(0, 0)
        else:
            if ttype == TType.PL:
                self.update_with_playlist(thread.playlist_titles)
                self.clear_add_state()
            else:
                self.update_info_list(thread.song_info)
                self.clear_add_state()
        self.set_progress_bar()

    def on_song_downloaded(self, index: int):
        # add url to completed list
        COMPLETED_LIST.append(DOWNLOAD_LIST[index])

        # update ui (progress bar and checkbox when download finished)
        self.update_song_count(len(COMPLETED_LIST), len(DOWNLOAD_LIST))
        value = (len(COMPLETED_LIST) / len(DOWNLOAD_LIST)) * 100
        self.dl_progress_bar.setValue(int(value))

        frame = self.scroll_layout.itemAt(index).widget()
        frame.findChild(QCheckBox).setChecked(True)

    def on_download_finished(self):
        self.lock_btns(False)
        self.display_warning_msg("Download completed !", "green")
        self._downloading = False

    ## ================================================= ##
    def open_settings(self):
        """Open settings dialog"""
        if not os.path.exists("data/settings.json"):
            with open("data/settings.json", "w") as f:
                json.dump(DEFAULT_SETTINGS, f, indent=4)

        setting_dialog = Ui_SettingsDialog()
        setting_dialog.setupUi(setting_dialog)
        setting_dialog.exec()

    def show_yes_no_dialog(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Confirmation")
        dialog.setText(
            "URL is part of a playlist, do you want to download the full playlist ?"
        )
        dialog.setIcon(QMessageBox.Question)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = dialog.exec_()

        if result == QMessageBox.Yes:
            self.get_playlist_info(self.input_line.text())
        else:
            song_url = self.input_line.text().split("&")[0]
            self.get_song_info(song_url)

    ## MINIMAL ##
    def display_warning_msg(self, msg: str, color: str):
        self.warning_label.setText(msg)
        self.warning_label.setStyleSheet(f"color: {color};")

    def clear_warning(self):
        self.warning_label.setText("")
        self.warning_label.setStyleSheet("color: black;")

    def clear_add_state(self):
        self.clear_warning()
        self.dl_button.setEnabled(True)
        self.dl_progress_bar.setRange(0, 100)

    def set_progress_bar(self):
        if not DOWNLOAD_LIST or not COMPLETED_LIST:
            self.dl_progress_bar.setValue(0)
        else:
            value = len(COMPLETED_LIST) / len(DOWNLOAD_LIST) * 100
            self.dl_progress_bar.setValue(int(value))

    def update_info_list(self, song_info: dict):
        self.add_song_frame(song_info["title"], song_info["thumbnail"])
        self.update_song_count(len(COMPLETED_LIST), len(DOWNLOAD_LIST))

    def lock_btns(self, lock: bool):
        self.dl_button.setEnabled(not lock)
        self.toolButton.setEnabled(not lock)

    def update_with_playlist(self, pl_info: list):
        for title, thumbnail in zip(
            pl_info["playlist_titles"], pl_info["playlist_thumbnails"]
        ):
            self.add_song_frame(title, thumbnail)

        self.update_song_count(len(COMPLETED_LIST), len(DOWNLOAD_LIST))

    def update_song_count(self, element: int, total: int):
        self.count_label.setText(f"{element}/{total}")
