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

from PySide6.QtCore import QCoreApplication, QMetaObject, QTimer, QRect, QSize, Slot
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
)


from .ui_settings_dialog import Ui_SettingsDialog
from .ui_title_frame import Ui_Frame
from core.entities import DEFAULT_SETTINGS, DOWNLOAD_LIST, COMPLETED_LIST, TType
from core.yt_dl import MonoYTExtractThread
from core.controller import is_youtube_url, is_youtube_playlist_url

class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
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
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout_3 = QGridLayout(self.main_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        # = Settings button = #
        self.toolButton = QToolButton(self.main_widget)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setFixedSize(QSize(60, 40))
        self.toolButton.setIconSize(QSize(50, 40))
        icon1 = QIcon("gui/static/material_setting_icon_1.png")
        self.toolButton.setIcon(icon1)
        

        self.toolButton.clicked.connect(self.open_settings)

        self.horizontalLayout_4.addWidget(self.toolButton)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.top_left_spacer = QSpacerItem(0, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.top_left_spacer)

        self.top_label_img = QLabel(self.main_widget)
        self.top_label_img.setObjectName(u"top_label_img")

        self.horizontalLayout_2.addWidget(self.top_label_img)

        self.top_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.top_right_spacer)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
# = INPUT = #
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.separator_top = QFrame(self.main_widget)
        self.separator_top.setObjectName(u"separator_top")
        self.separator_top.setFrameShape(QFrame.HLine)
        self.separator_top.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.separator_top)

        self.input_main_vlayout = QVBoxLayout()
        self.input_main_vlayout.setObjectName(u"input_main_vlayout")
        self.input_line = QLineEdit(self.main_widget)
        self.input_line.setObjectName(u"input_line")
        self.input_line.returnPressed.connect(self.on_url_add)
        self.input_line.setPlaceholderText("Paste URL here...")

        self.input_main_vlayout.addWidget(self.input_line)

        self.add_btn_hlayout = QHBoxLayout()
        self.add_btn_hlayout.setObjectName(u"add_btn_hlayout")
        self.add_btn_left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.add_btn_hlayout.addItem(self.add_btn_left_spacer)

        self.add_btn = QPushButton(self.main_widget)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy1)
        self.add_btn.clicked.connect(self.on_url_add)

        self.add_btn_hlayout.addWidget(self.add_btn)

        self.add_btn_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.add_btn_hlayout.addItem(self.add_btn_right_spacer)


        self.input_main_vlayout.addLayout(self.add_btn_hlayout)


        self.verticalLayout_2.addLayout(self.input_main_vlayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.warning_label = QLabel(self.main_widget)
        self.warning_label.setObjectName(u"warning_label")

        self.horizontalLayout.addWidget(self.warning_label)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.separator_bottom = QFrame(self.main_widget)
        self.separator_bottom.setObjectName(u"separator_bottom")
        self.separator_bottom.setFrameShape(QFrame.HLine)
        self.separator_bottom.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.separator_bottom)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.dl_list_frame = QFrame(self.main_widget)
        self.dl_list_frame.setObjectName(u"dl_list_frame")
        self.dl_list_frame.setFrameShape(QFrame.StyledPanel)
        self.dl_list_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.dl_list_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dl_progress_bar = QProgressBar(self.dl_list_frame)
        self.dl_progress_bar.setObjectName(u"dl_progress_bar")
        self.dl_progress_bar.setValue(0)

        self.horizontalLayout_3.addWidget(self.dl_progress_bar)

        self.count_label = QLabel(self.dl_list_frame)
        self.count_label.setObjectName(u"count_label")

        self.horizontalLayout_3.addWidget(self.count_label)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.dl_scroll_area = QScrollArea(self.dl_list_frame)
        self.dl_scroll_area.setObjectName(u"dl_scroll_area")
        self.dl_scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_area_content.setObjectName(u"scroll_area_content")
        self.scroll_area_content.setGeometry(QRect(0, 0, 756, 331))
        self.scroll_layout = QVBoxLayout()
        self.scroll_area_content.setLayout(self.scroll_layout)
        self.dl_scroll_area.setWidget(self.scroll_area_content)

        self.verticalLayout.addWidget(self.dl_scroll_area)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.dl_list_frame, 2, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.dl_btn_left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.dl_btn_left_spacer)

        self.dl_button = QPushButton(self.main_widget)
        self.dl_button.setObjectName(u"dl_button")

        self.horizontalLayout_5.addWidget(self.dl_button)

        self.dl_btn_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.dl_btn_right_spacer)


        self.gridLayout_2.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.main_widget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Lotus Youtube Downloader", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.top_label_img.setText(QCoreApplication.translate("MainWindow", u"Lotus Youtube Downloader", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.count_label.setText(QCoreApplication.translate("MainWindow", u"0/0", None))
        self.dl_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))

    # == Actions ==#
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
            self.display_warning("Not a valid URL")

    def monitor(self, thread, ttype=None):
        if thread.is_alive():
            QTimer.singleShot(100, lambda: self.monitor(thread, ttype))
        else:
            if ttype == TType.PL:
                self.update_with_playlist(thread.playlist_titles)
            else:
                self.update_info_list(thread.song_info)

    # == OPE == #
    def get_song_info(self, url: str):
        if url not in DOWNLOAD_LIST:
            info_thread = MonoYTExtractThread(url)
            info_thread.start()
            self.monitor(info_thread)
    
    def get_playlist_info(self, url: str):
        pass


    def update_info_list(self, song_info: dict):
        frame = QFrame()
        ui = Ui_Frame()
        ui.setupUi(frame)
        ui.set_title(song_info["title"])
        ui.set_thumbnail(song_info["thumbnail"])
        self.scroll_layout.addWidget(frame)
        self.update_song_count(len(COMPLETED_LIST), len(DOWNLOAD_LIST))

    # == UTILS == #
    def update_progress_bar(self):
        pass

    def update_song_count(self, element: int, total: int):
        self.count_label.setText(f"{element}/{total}")
    
    def display_warning(self, msg: str):
        self.warning_label.setText(msg)
        self.warning_label.setStyleSheet("color: red;")
    
    def display_finished(self):
        self.warning_label.setText("Download finished !")
        self.warning_label.setStyleSheet("color: green;")
    
    def clear_warning(self):
        self.warning_label.setText("")
        self.warning_label.setStyleSheet("color: black;")

    def open_settings(self):
        """Open settings dialog"""
        if not os.path.exists("data/settings.json"):
            with open("data/settings.json", "w") as f:
                json.dump(DEFAULT_SETTINGS, f, indent=4)

        setting_dialog = Ui_SettingsDialog()
        setting_dialog.setupUi(setting_dialog)
        setting_dialog.exec()

## ================================================= ##
    @Slot()
    def show_yes_no_dialog(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("Confirmation")
        dialog.setText("URL is part of a playlist, do you want to download the full playlist ?")
        dialog.setIcon(QMessageBox.Question)
        dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        result = dialog.exec_()

        if result == QMessageBox.Yes:
            print("Yes button clicked")
        else:
            song_url = self.input_line.text().split("&")[0]
            self.get_song_info(song_url)