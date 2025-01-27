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
    QStackedWidget, QStatusBar, QVBoxLayout, QWidget, QGridLayout, QLayout, QFormLayout)
from functools import partial
from iconsQt_rc import qt_resource_data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from time import sleep as wait
import pyautogui
import undetected_chromedriver as uc

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
        self.frame_2.setMinimumSize(QSize(100, 250))
        self.frame_2.setMaximumSize(QSize(0, 16777215))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.frame_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)

        self.verticalLayout.addWidget(self.frame_5)

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
        self.HomepageButton.setMinimumSize(QSize(100, 50))
        self.HomepageButton.setMaximumSize(QSize(75, 75))
        self.HomepageButton.setSizeIncrement(QSize(0, 0))
        self.HomepageButton.setBaseSize(QSize(0, 0))
        self.HomepageButton.setStyleSheet(u"font-weight: bold; text-align: left")
        icon = QIcon()
        icon.addFile(u":/icons/assets/images/home-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HomepageButton.setIcon(icon)
        self.HomepageButton.setIconSize(QSize(20, 20))
        self.HomepageButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.HomepageButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.WorkflowButton = QPushButton(self.frame_3)
        self.WorkflowButton.setObjectName(u"WorkflowButton")
        sizePolicy3.setHeightForWidth(self.WorkflowButton.sizePolicy().hasHeightForWidth())
        self.WorkflowButton.setSizePolicy(sizePolicy3)
        self.WorkflowButton.setMinimumSize(QSize(100, 50))
        self.WorkflowButton.setStyleSheet(u"font-weight: bold; text-align: left")
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/images/workflow-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.WorkflowButton.setIcon(icon1)
        self.WorkflowButton.setIconSize(QSize(20, 20))
        self.WorkflowButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.WorkflowButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.ToolsButton = QPushButton(self.frame_3)
        self.ToolsButton.setObjectName(u"ToolsButton")
        sizePolicy3.setHeightForWidth(self.ToolsButton.sizePolicy().hasHeightForWidth())
        self.ToolsButton.setSizePolicy(sizePolicy3)
        self.ToolsButton.setMinimumSize(QSize(100, 50))
        self.ToolsButton.setStyleSheet(u"font-weight: bold; text-align: left")
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/images/wrench-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolsButton.setIcon(icon2)
        self.ToolsButton.setIconSize(QSize(20, 20))
        self.ToolsButton.setFlat(True)

        self.verticalLayout_2.addWidget(self.ToolsButton, 0, Qt.AlignmentFlag.AlignHCenter)

        self.SettingsButton = QPushButton(self.frame_3)
        self.SettingsButton.setObjectName(u"SettingsButton")
        sizePolicy3.setHeightForWidth(self.SettingsButton.sizePolicy().hasHeightForWidth())
        self.SettingsButton.setSizePolicy(sizePolicy3)
        self.SettingsButton.setMinimumSize(QSize(100, 50))
        self.SettingsButton.setStyleSheet(u"font-weight: bold; text-align: left")
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/images/settings-icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsButton.setIcon(icon3)
        self.SettingsButton.setIconSize(QSize(20, 20))
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
        self.verticalLayout_8 = QVBoxLayout(self.frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: transparent;")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_11 = QLabel(self.frame_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFrameShape(QFrame.Shape.WinPanel)
        self.label_11.setFrameShadow(QFrame.Shadow.Raised)

        self.horizontalLayout_2.addWidget(self.label_11)


        self.verticalLayout_8.addWidget(self.frame_6)

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

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.frame_7 = QFrame(self.Workflows)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy4)
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_7)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.printButton = QPushButton(self.frame_7)
        self.printButton.setObjectName(u"printButton")

        self.gridLayout_2.addWidget(self.printButton, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_2.addWidget(self.pushButton_2, 0, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 1, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 1, 0, 1, 1)


        self.gridLayout.addWidget(self.frame_7, 0, 0, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)

        self.stackedWidget.addWidget(self.Workflows)
        self.Tools = QWidget()
        self.Tools.setObjectName(u"Tools")
        self.verticalLayout_5 = QVBoxLayout(self.Tools)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.Tools)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_7.addWidget(self.label_7, 0, Qt.AlignmentFlag.AlignTop)

        self.label_8 = QLabel(self.Tools)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setWordWrap(True)

        self.verticalLayout_7.addWidget(self.label_8, 0, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_5.addLayout(self.verticalLayout_7)

        self.ToolsFrame = QFrame(self.Tools)
        self.ToolsFrame.setObjectName(u"ToolsFrame")
        sizePolicy4.setHeightForWidth(self.ToolsFrame.sizePolicy().hasHeightForWidth())
        self.ToolsFrame.setSizePolicy(sizePolicy4)
        self.ToolsFrame.setStyleSheet(u"background: transparent; border: transparent;")
        self.ToolsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ToolsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.ToolsFrame)
        self.formLayout.setObjectName(u"formLayout")
        self.frame_4 = QFrame(self.ToolsFrame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(200, 200))
        self.frame_4.setStyleSheet(u"background: grey;")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.frame_4)


        self.verticalLayout_5.addWidget(self.ToolsFrame)

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

        self.verticalLayout_8.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.HomepageButton.setDefault(False)
        self.stackedWidget.setCurrentIndex(1)
        self.HomepageButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.WorkflowButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 1))
        self.ToolsButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 2))
        self.SettingsButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 3))
        self.stackedWidget.setCurrentIndex(0)   
        def on_button_clicked():
            print('skibidi')     
        self.printButton.clicked.connect(on_button_clicked)
        def she_skibidi_my_toilet_until_i_rizz():
            print('helo')
            options2 = uc.ChromeOptions()
            prefs = {'credentials_enable_service': False,
                    'profile.password_manager_enabled': False}
            options2.add_experimental_option('prefs',prefs)
            driver = uc.Chrome(options=options2)
            driver.maximize_window()
            driver.execute_script("window.scrollTo(0,0)")
            driver.get('https://www.supremacy1914.com')
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'didomi-notice-agree-button'))
            )
            driver.find_element(By.ID, 'didomi-notice-agree-button').click()
            username = 'k4wn_'
            password = 'D@n1el092009'
            WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.ID, 'loginbox_login_input'))
            )

            driver.find_element(By.ID, 'loginbox_login_input').send_keys(username)
            WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.ID, 'loginbox_password_input'))
            )
            driver.find_element(By.ID, 'loginbox_password_input').send_keys(password)
            driver.find_element(By.ID, 'loginbutton_cont').click()
            wait(1)
            driver.close()
            wait(1)
        self.pushButton_2.clicked.connect(she_skibidi_my_toilet_until_i_rizz)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Menu</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.HomepageButton.setToolTip(QCoreApplication.translate("MainWindow", u"Homepage", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.HomepageButton.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.HomepageButton.setText(QCoreApplication.translate("MainWindow", u"Homepage", None))
        self.WorkflowButton.setText(QCoreApplication.translate("MainWindow", u"Workflows", None))
        self.ToolsButton.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"this will display the page title someday", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">What is this?</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:26pt;\">Homepage - QtDesigner Demo</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"This is a demo of my personal project. In this demo, I am using QtDesigner to make a responsive GUI for a program that automates tedious tasks. ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Workflow Page</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"This is going to be the workflow page. There will be one (or multiple, depending on my abilities) trigger to automate a certain tasks. There will be five slots (possibly with the ability to add more) to create workflows in.", None))
        self.printButton.setText(QCoreApplication.translate("MainWindow", u"im going to print something", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"random function test lol", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Tools Page</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"This page will be for tools that will help the user input values for their workflows. For example, if they're trying to figure out what the coordinates are if they want to click on a certain x or y value, they can do so using one of the tools that will be listed here. This is meant to be additive to the \"workflows\" section, meaning it is of a lower priority.  ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Settings</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"This page will help the user configure the app to their liking. For example, they might be able to choose a theme, the menu style (with or without text, with or without icons etc.) to make the app easier for them to use. ", None))
    # retranslateUi

