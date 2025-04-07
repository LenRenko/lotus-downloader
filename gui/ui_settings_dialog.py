# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialogITiPpp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    QSize,
    Qt,
)
from PySide6.QtGui import (
    QIcon,
)
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDialog,
    QDialogButtonBox,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSizePolicy,
    QSpacerItem,
    QVBoxLayout,
    QFileDialog,
)

from qt_material import apply_stylesheet
from core.entities import Format
import json
import os


class Ui_SettingsDialog(QDialog):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName("Settings")
        SettingsDialog.resize(400, 300)
        self.gridLayout_4 = QGridLayout(SettingsDialog)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.main_vlayout = QVBoxLayout()
        self.main_vlayout.setObjectName("main_vlayout")
        self.format_frame = QFrame(SettingsDialog)
        self.format_frame.setObjectName("format_frame")
        self.format_frame.setFrameShape(QFrame.StyledPanel)
        self.format_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.format_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.format_label_layout = QHBoxLayout()
        self.format_label_layout.setObjectName("format_label_layout")
        self.format_label = QLabel(self.format_frame)
        self.format_label.setObjectName("format_label")

        icon = QIcon()
        icon.addFile("gui/static/exe_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        SettingsDialog.setWindowIcon(icon)

        self.format_label_layout.addWidget(self.format_label)

        self.format_label_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.format_label_layout.addItem(self.format_label_spacer)

        self.gridLayout.addLayout(self.format_label_layout, 0, 0, 1, 1)

        # == Format combo box == #
        self.format_choice_layout = QHBoxLayout()
        self.format_choice_layout.setObjectName("format_choice_layout")
        self.format_combo_box = QComboBox(self.format_frame)
        self.format_combo_box.setObjectName("format_combo_box")

        self.format_choice_layout.addWidget(self.format_combo_box)

        self.format_combo_box_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.format_choice_layout.addItem(self.format_combo_box_spacer)

        #
        self.gridLayout.addLayout(self.format_choice_layout, 1, 0, 1, 1)

        self.main_vlayout.addWidget(self.format_frame)
        # == Output folder / btn and label == #
        self.folder_frame = QFrame(SettingsDialog)
        self.folder_frame.setObjectName("folder_frame")
        self.folder_frame.setFrameShape(QFrame.StyledPanel)
        self.folder_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.folder_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.folder_label_layout = QHBoxLayout()
        self.folder_label_layout.setObjectName("folder_label_layout")
        self.folder_label_2 = QLabel(self.folder_frame)
        self.folder_label_2.setObjectName("folder_label_2")

        self.folder_label_layout.addWidget(self.folder_label_2)

        self.folder_label_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.folder_label_layout.addItem(self.folder_label_spacer)

        self.gridLayout_2.addLayout(self.folder_label_layout, 0, 0, 1, 1)

        self.folder_btn_layout = QHBoxLayout()
        self.folder_btn_layout.setObjectName("folder_btn_layout")

        self.folder_browse_btn = QPushButton(self.folder_frame)
        self.folder_browse_btn.setObjectName("folder_browse_btn")
        icon1 = QIcon()
        icon1.addFile("gui/static/folder_open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.folder_browse_btn.setIcon(icon1)
        self.folder_browse_btn.clicked.connect(self.open_folder_dialog)

        self.folder_btn_layout.addWidget(self.folder_browse_btn)

        self.folder_mid_spacer = QSpacerItem(
            38, 18, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.folder_btn_layout.addItem(self.folder_mid_spacer)

        self.folder_label = QLabel(self.folder_frame)
        self.folder_label.setObjectName("folder_label")

        self.folder_btn_layout.addWidget(self.folder_label)

        self.gridLayout_2.addLayout(self.folder_btn_layout, 1, 0, 1, 1)

        self.main_vlayout.addWidget(self.folder_frame)
        # == Dark mode checkbox == #
        self.dark_mode_frame = QFrame(SettingsDialog)
        self.dark_mode_frame.setObjectName("dark_mode_frame")
        self.dark_mode_frame.setFrameShape(QFrame.StyledPanel)
        self.dark_mode_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.dark_mode_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.dark_mode_layout = QHBoxLayout()
        self.dark_mode_layout.setObjectName("dark_mode_layout")
        self.dark_mode_checkbox = QCheckBox(self.dark_mode_frame)
        self.dark_mode_checkbox.setObjectName("dark_mode_checkbox")

        self.dark_mode_layout.addWidget(self.dark_mode_checkbox)

        self.dark_mode_spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum
        )

        self.dark_mode_layout.addItem(self.dark_mode_spacer)

        self.gridLayout_3.addLayout(self.dark_mode_layout, 0, 0, 1, 1)

        self.main_vlayout.addWidget(self.dark_mode_frame)

        # == Dialog btn boxes == #
        self.gridLayout_4.addLayout(self.main_vlayout, 0, 0, 1, 1)

        self.btn_boxes = QDialogButtonBox(SettingsDialog)
        self.btn_boxes.setObjectName("btn_boxes")
        self.btn_boxes.setOrientation(Qt.Horizontal)
        self.btn_boxes.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Save
        )

        self.gridLayout_4.addWidget(self.btn_boxes, 1, 0, 1, 1)

        # === Init ===#
        self.retranslateUi(SettingsDialog)
        self.populate_formats()
        self.retrieve_settings()

        self.btn_boxes.accepted.connect(self.save_settings)
        self.btn_boxes.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)

    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(
            QCoreApplication.translate("SettingsDialog", "Settings", None)
        )
        self.format_label.setText(
            QCoreApplication.translate("SettingsDialog", "Format", None)
        )

        self.folder_label_2.setText(
            QCoreApplication.translate("SettingsDialog", "Output Folder", None)
        )
        self.folder_browse_btn.setText(
            QCoreApplication.translate("SettingsDialog", "Browse", None)
        )
        self.folder_label.setText(
            QCoreApplication.translate("SettingsDialog", "", None)
        )
        self.dark_mode_checkbox.setText(
            QCoreApplication.translate("SettingsDialog", "Dark Mode", None)
        )

    # retranslateUi

    def populate_formats(self):
        for name, balue in Format.__members__.items():
            self.format_combo_box.addItem(name)

    # === Actions === #
    def open_folder_dialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.folder_label.setText(folder_path)

    def retrieve_settings(self):
        if os.path.exists("data/settings.json"):
            with open("data/settings.json", "r") as f:
                data = json.load(f)
                self.format_combo_box.setCurrentText(data["output_format"])
                self.folder_label.setText(data["output_dir"])
                self.dark_mode_checkbox.setChecked(data["dark_mode"])

    def save_settings(self):
        data = {
            "output_format": self.format_combo_box.currentText(),
            "output_dir": self.folder_label.text(),
            "dark_mode": self.dark_mode_checkbox.isChecked(),
        }
        with open("data/settings.json", "w") as f:
            json.dump(data, f, indent=4)

        app = QApplication.instance()
        if self.dark_mode_checkbox.isChecked():
            apply_stylesheet(app, theme="dark_amber.xml")
        else:
            apply_stylesheet(app, theme="light_amber.xml", invert_secondary=True)
        self.accept()
