# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_windowtiYpZS.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
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
        icon = QIcon()
        icon.addFile("gui/static/exe_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.main_widget = QWidget(MainWindow)
        self.main_widget.setObjectName(u"main_widget")
        self.gridLayout = QGridLayout(self.main_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.top_left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.top_left_spacer)

        self.top_label_img = QLabel(self.main_widget)
        self.top_label_img.setObjectName(u"top_label_img")

        self.horizontalLayout_2.addWidget(self.top_label_img)

        self.top_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.top_right_spacer)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.input_vlayout = QVBoxLayout()
        self.input_vlayout.setObjectName(u"input_vlayout")
        self.separator_top = QFrame(self.main_widget)
        self.separator_top.setObjectName(u"separator_top")
        self.separator_top.setFrameShape(QFrame.HLine)
        self.separator_top.setFrameShadow(QFrame.Sunken)

        self.input_vlayout.addWidget(self.separator_top)

        self.input_main_vlayout = QVBoxLayout()
        self.input_main_vlayout.setObjectName(u"input_main_vlayout")
        self.input_line = QLineEdit(self.main_widget)
        self.input_line.setObjectName(u"input_line")

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

        self.add_btn_hlayout.addWidget(self.add_btn)

        self.add_btn_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.add_btn_hlayout.addItem(self.add_btn_right_spacer)


        self.input_main_vlayout.addLayout(self.add_btn_hlayout)


        self.input_vlayout.addLayout(self.input_main_vlayout)

        self.separator_bottom = QFrame(self.main_widget)
        self.separator_bottom.setObjectName(u"separator_bottom")
        self.separator_bottom.setFrameShape(QFrame.HLine)
        self.separator_bottom.setFrameShadow(QFrame.Sunken)

        self.input_vlayout.addWidget(self.separator_bottom)


        self.verticalLayout.addLayout(self.input_vlayout)

        self.dl_list_frame = QFrame(self.main_widget)
        self.dl_list_frame.setObjectName(u"dl_list_frame")
        self.dl_list_frame.setFrameShape(QFrame.StyledPanel)
        self.dl_list_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.dl_list_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.dl_list_vlayout = QVBoxLayout()
        self.dl_list_vlayout.setObjectName(u"dl_list_vlayout")
        self.dl_progress_bar = QProgressBar(self.dl_list_frame)
        self.dl_progress_bar.setObjectName(u"dl_progress_bar")
        self.dl_progress_bar.setValue(24)

        self.dl_list_vlayout.addWidget(self.dl_progress_bar)

        self.dl_scroll_area = QScrollArea(self.dl_list_frame)
        self.dl_scroll_area.setObjectName(u"dl_scroll_area")
        self.dl_scroll_area.setWidgetResizable(True)
        self.scroll_area_content = QWidget()
        self.scroll_area_content.setObjectName(u"scroll_area_content")
        self.scroll_area_content.setGeometry(QRect(0, 0, 756, 363))
        self.dl_scroll_area.setWidget(self.scroll_area_content)

        self.dl_list_vlayout.addWidget(self.dl_scroll_area)


        self.gridLayout_2.addLayout(self.dl_list_vlayout, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.dl_list_frame)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.dl_btn_left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.dl_btn_left_spacer)

        self.dl_button = QPushButton(self.main_widget)
        self.dl_button.setObjectName(u"dl_button")

        self.horizontalLayout.addWidget(self.dl_button)

        self.dl_btn_right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.dl_btn_right_spacer)

        self.toolButton = QToolButton(self.main_widget)
        self.toolButton.setObjectName(u"toolButton")
        icon1 = QIcon()
        icon1.addFile("gui/static/settings_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.main_widget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.top_label_img.setText(QCoreApplication.translate("MainWindow", u"Lunar Lotus Downloader", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.dl_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
    # retranslateUi

