# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'settings_dialogITiPpp.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QCheckBox, QComboBox,
    QDialog, QDialogButtonBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(400, 300)
        self.gridLayout_4 = QGridLayout(SettingsDialog)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.main_vlayout = QVBoxLayout()
        self.main_vlayout.setObjectName(u"main_vlayout")
        self.format_frame = QFrame(SettingsDialog)
        self.format_frame.setObjectName(u"format_frame")
        self.format_frame.setFrameShape(QFrame.StyledPanel)
        self.format_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.format_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.format_label_layout = QHBoxLayout()
        self.format_label_layout.setObjectName(u"format_label_layout")
        self.format_label = QLabel(self.format_frame)
        self.format_label.setObjectName(u"format_label")

        self.format_label_layout.addWidget(self.format_label)

        self.format_label_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.format_label_layout.addItem(self.format_label_spacer)


        self.gridLayout.addLayout(self.format_label_layout, 0, 0, 1, 1)

        self.format_choice_layout = QHBoxLayout()
        self.format_choice_layout.setObjectName(u"format_choice_layout")
        self.format_combo_box = QComboBox(self.format_frame)
        self.format_combo_box.addItem("")
        self.format_combo_box.addItem("")
        self.format_combo_box.addItem("")
        self.format_combo_box.setObjectName(u"format_combo_box")

        self.format_choice_layout.addWidget(self.format_combo_box)

        self.format_combo_box_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.format_choice_layout.addItem(self.format_combo_box_spacer)


        self.gridLayout.addLayout(self.format_choice_layout, 1, 0, 1, 1)


        self.main_vlayout.addWidget(self.format_frame)

        self.folder_frame = QFrame(SettingsDialog)
        self.folder_frame.setObjectName(u"folder_frame")
        self.folder_frame.setFrameShape(QFrame.StyledPanel)
        self.folder_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.folder_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.folder_label_layout = QHBoxLayout()
        self.folder_label_layout.setObjectName(u"folder_label_layout")
        self.folder_label_2 = QLabel(self.folder_frame)
        self.folder_label_2.setObjectName(u"folder_label_2")

        self.folder_label_layout.addWidget(self.folder_label_2)

        self.folder_label_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.folder_label_layout.addItem(self.folder_label_spacer)


        self.gridLayout_2.addLayout(self.folder_label_layout, 0, 0, 1, 1)

        self.folder_btn_layout = QHBoxLayout()
        self.folder_btn_layout.setObjectName(u"folder_btn_layout")
        self.folder_browse_btn = QPushButton(self.folder_frame)
        self.folder_browse_btn.setObjectName(u"folder_browse_btn")

        self.folder_btn_layout.addWidget(self.folder_browse_btn)

        self.folder_mid_spacer = QSpacerItem(38, 18, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.folder_btn_layout.addItem(self.folder_mid_spacer)

        self.folder_label = QLabel(self.folder_frame)
        self.folder_label.setObjectName(u"folder_label")

        self.folder_btn_layout.addWidget(self.folder_label)


        self.gridLayout_2.addLayout(self.folder_btn_layout, 1, 0, 1, 1)


        self.main_vlayout.addWidget(self.folder_frame)

        self.dark_mode_frame = QFrame(SettingsDialog)
        self.dark_mode_frame.setObjectName(u"dark_mode_frame")
        self.dark_mode_frame.setFrameShape(QFrame.StyledPanel)
        self.dark_mode_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.dark_mode_frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.dark_mode_layout = QHBoxLayout()
        self.dark_mode_layout.setObjectName(u"dark_mode_layout")
        self.dark_mode_checkbox = QCheckBox(self.dark_mode_frame)
        self.dark_mode_checkbox.setObjectName(u"dark_mode_checkbox")

        self.dark_mode_layout.addWidget(self.dark_mode_checkbox)

        self.dark_mode_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.dark_mode_layout.addItem(self.dark_mode_spacer)


        self.gridLayout_3.addLayout(self.dark_mode_layout, 0, 0, 1, 1)


        self.main_vlayout.addWidget(self.dark_mode_frame)


        self.gridLayout_4.addLayout(self.main_vlayout, 0, 0, 1, 1)

        self.btn_boxes = QDialogButtonBox(SettingsDialog)
        self.btn_boxes.setObjectName(u"btn_boxes")
        self.btn_boxes.setOrientation(Qt.Horizontal)
        self.btn_boxes.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Save)

        self.gridLayout_4.addWidget(self.btn_boxes, 1, 0, 1, 1)


        self.retranslateUi(SettingsDialog)
        self.btn_boxes.accepted.connect(SettingsDialog.accept)
        self.btn_boxes.rejected.connect(SettingsDialog.reject)

        QMetaObject.connectSlotsByName(SettingsDialog)
    # setupUi

    def retranslateUi(self, SettingsDialog):
        SettingsDialog.setWindowTitle(QCoreApplication.translate("SettingsDialog", u"Dialog", None))
        self.format_label.setText(QCoreApplication.translate("SettingsDialog", u"Format", None))
        self.format_combo_box.setItemText(0, QCoreApplication.translate("SettingsDialog", u"MP3", None))
        self.format_combo_box.setItemText(1, QCoreApplication.translate("SettingsDialog", u"AAC", None))
        self.format_combo_box.setItemText(2, QCoreApplication.translate("SettingsDialog", u"M4A", None))

        self.folder_label_2.setText(QCoreApplication.translate("SettingsDialog", u"Output Folder", None))
        self.folder_browse_btn.setText(QCoreApplication.translate("SettingsDialog", u"Folder", None))
        self.folder_label.setText(QCoreApplication.translate("SettingsDialog", u"TextLabel", None))
        self.dark_mode_checkbox.setText(QCoreApplication.translate("SettingsDialog", u"Dark Mode", None))
    # retranslateUi

