# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Demo2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget)
from functools import partial
from iconsQt_rc import qt_resource_data
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(641, 521)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMinimumSize(QSize(100, 500))
        self.frame_2.setMaximumSize(QSize(0, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
        self.label.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignTop)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"QFrame::Noframe")
        self.frame_3.setFrameShape(QFrame.Shape.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.HomepageButton = QPushButton(self.frame_3)
        self.HomepageButton.setObjectName(u"HomepageButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.HomepageButton.sizePolicy().hasHeightForWidth())
        self.HomepageButton.setSizePolicy(sizePolicy3)
        self.HomepageButton.setMinimumSize(QSize(75, 75))
        self.HomepageButton.setMaximumSize(QSize(75, 75))
        self.HomepageButton.setSizeIncrement(QSize(0, 0))
        self.HomepageButton.setBaseSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/icons/assets/images/home-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HomepageButton.setIcon(icon)
        self.HomepageButton.setIconSize(QSize(50, 50))
        self.HomepageButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.HomepageButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.WorkflowButton = QPushButton(self.frame_3)
        self.WorkflowButton.setObjectName(u"WorkflowButton")
        sizePolicy3.setHeightForWidth(self.WorkflowButton.sizePolicy().hasHeightForWidth())
        self.WorkflowButton.setSizePolicy(sizePolicy3)
        self.WorkflowButton.setMinimumSize(QSize(75, 75))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/images/workflow-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.WorkflowButton.setIcon(icon1)
        self.WorkflowButton.setIconSize(QSize(50, 50))
        self.WorkflowButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.WorkflowButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.ToolsButton = QPushButton(self.frame_3)
        self.ToolsButton.setObjectName(u"ToolsButton")
        sizePolicy3.setHeightForWidth(self.ToolsButton.sizePolicy().hasHeightForWidth())
        self.ToolsButton.setSizePolicy(sizePolicy3)
        self.ToolsButton.setMinimumSize(QSize(75, 75))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/images/wrench-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolsButton.setIcon(icon2)
        self.ToolsButton.setIconSize(QSize(50, 50))
        self.ToolsButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.ToolsButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.SettingsButton = QPushButton(self.frame_3)
        self.SettingsButton.setObjectName(u"SettingsButton")
        sizePolicy3.setHeightForWidth(self.SettingsButton.sizePolicy().hasHeightForWidth())
        self.SettingsButton.setSizePolicy(sizePolicy3)
        self.SettingsButton.setMinimumSize(QSize(75, 75))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/images/settings-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsButton.setIcon(icon3)
        self.SettingsButton.setIconSize(QSize(50, 50))
        self.SettingsButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.SettingsButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 171, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setBaseSize(QSize(1002, 0))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.Homepage = QWidget()
        self.Homepage.setObjectName(u"Homepage")
        self.verticalLayout_3 = QVBoxLayout(self.Homepage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.Homepage)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.Homepage)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_3.addWidget(self.label_2)

        self.label_4 = QLabel(self.Homepage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_4)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.stackedWidget.addWidget(self.Homepage)
        self.Workflows = QWidget()
        self.Workflows.setObjectName(u"Workflows")
        self.verticalLayout_4 = QVBoxLayout(self.Workflows)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.Workflows)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_4.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignTop)

        self.label_6 = QLabel(self.Workflows)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.Workflows)
        self.Tools = QWidget()
        self.Tools.setObjectName(u"Tools")
        self.verticalLayout_5 = QVBoxLayout(self.Tools)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_7 = QLabel(self.Tools)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignTop)

        self.label_8 = QLabel(self.Tools)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_8)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)

        self.stackedWidget.addWidget(self.Tools)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.verticalLayout_6 = QVBoxLayout(self.Settings)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_9 = QLabel(self.Settings)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_6.addWidget(self.label_9, 0, Qt.AlignmentFlag.AlignTop)

        self.label_10 = QLabel(self.Settings)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_10)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_5)

        self.stackedWidget.addWidget(self.Settings)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.HomepageButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
        self.HomepageButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.WorkflowButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 1))
        self.ToolsButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 2))
        self.SettingsButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 3))
        self.stackedWidget.setCurrentIndex(0)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Menu</p></body></html>", None))
        self.HomepageButton.setText("")
        self.WorkflowButton.setText("")
        self.ToolsButton.setText("")
        self.SettingsButton.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">What is this?</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Homepage - QtDesigner Demo</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"This is a demo of my personal project for Vilnius International School. In this demo, I am using QtDesigner to make a responsive GUI for a program that automates tedious tasks. ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Workflow Page</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"This is going to be the workflow page. There will be one (or multiple, depending on my abilities) trigger to automate a certain tasks. There will be five slots (possibly with the ability to add more) to create workflows in.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Tools Page</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"This page will be for tools that will help the user input values for their workflows. For example, if they're trying to figure out what the coordinates are if they want to click on a certain x or y value, they can do so using one of the tools that will be listed here. This is meant to be additive to the \"workflows\" section, meaning it is of a lower priority.  ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Settings</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"This page will help the user configure the app to their liking. For example, they might be able to choose a theme, the menu style (with or without text, with or without icons etc.) to make the app easier for them to use. ", None))
    # retranslateUi