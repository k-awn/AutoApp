# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test3VGoflT.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt, QRect)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtWidgets import (QFormLayout, QFrame, QGridLayout, QCheckBox, QTextEdit, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget, QScrollArea)
import Icons_rc
from toggle import CustomToggle
from os.path import isfile
from os import remove
import threading
import time
from os import path

class Ui_Form(QWidget):
    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(500, 500)

        self.setMinimumSize(QSize(500, 500))
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.stackedWidget = QStackedWidget(self)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 150))
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 2)

        self.triggerDropDown = QComboBox(self.page_2)
        self.triggerDropDown.addItem("")
        self.triggerDropDown.addItem("")
        self.triggerDropDown.setObjectName(u"triggerDropDown")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.triggerDropDown.sizePolicy().hasHeightForWidth())
        self.triggerDropDown.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.triggerDropDown, 1, 1, 1, 1)

        self.trigSettings = QStackedWidget(self.page_2)
        self.trigSettings.setObjectName(u"trigSettings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.trigSettings.sizePolicy().hasHeightForWidth())
        self.trigSettings.setSizePolicy(sizePolicy1)
        self.trigSettings.setMinimumSize(QSize(200, 50))
        self.trigSettings.setMaximumSize(QSize(16777215, 50))
        self.hotkeySettings = QWidget()
        self.hotkeySettings.setObjectName(u"hotkeySettings")
        self.hotkeySettings.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_2 = QGridLayout(self.hotkeySettings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.textEdit = QTextEdit(self.hotkeySettings)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy2)
        self.textEdit.setMinimumSize(QSize(0, 0))
        self.textEdit.setMaximumSize(QSize(16777215, 25))
        self.textEdit.setStyleSheet(u"border:none; background:transparent")

        self.gridLayout_2.addWidget(self.textEdit, 0, 1, 1, 1)

        self.label_5 = QLabel(self.hotkeySettings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.trigSettings.addWidget(self.hotkeySettings)
        self.intervalSettings = QWidget()
        self.intervalSettings.setObjectName(u"intervalSettings")
        self.gridLayout_4 = QGridLayout(self.intervalSettings)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_6 = QLabel(self.intervalSettings)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.textEdit_2 = QTextEdit(self.intervalSettings)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMaximumSize(QSize(16777215, 25))
        self.textEdit_2.setStyleSheet(u"border:none; background:transparent")

        self.gridLayout_4.addWidget(self.textEdit_2, 0, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.trigSettings.addWidget(self.intervalSettings)

        self.gridLayout_3.addWidget(self.trigSettings, 4, 0, 1, 2)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_10 = QGridLayout(self.page_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.functionDropDown = QComboBox(self.page_3)
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.setObjectName(u"functionDropDown")
        sizePolicy.setHeightForWidth(self.functionDropDown.sizePolicy().hasHeightForWidth())
        self.functionDropDown.setSizePolicy(sizePolicy)

        self.gridLayout_10.addWidget(self.functionDropDown, 1, 1, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.funcSettings = QStackedWidget(self.page_3)
        self.funcSettings.setObjectName(u"funcSettings")
        self.funcSettings.setMaximumSize(QSize(16777215, 50))
        self.openBrowserSettings = QWidget()
        self.openBrowserSettings.setObjectName(u"openBrowserSettings")
        self.gridLayout_5 = QGridLayout(self.openBrowserSettings)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.openBrowserSettings)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.textEdit_3 = QTextEdit(self.openBrowserSettings)
        self.textEdit_3.setObjectName(u"textEdit_3")
        self.textEdit_3.setMaximumSize(QSize(16777215, 25))
        self.textEdit_3.setStyleSheet(u"border:none; background:transparent")

        self.gridLayout_5.addWidget(self.textEdit_3, 0, 1, 1, 1)

        self.funcSettings.addWidget(self.openBrowserSettings)
        self.clickButton = QWidget()
        self.clickButton.setObjectName(u"clickButton")
        self.gridLayout_6 = QGridLayout(self.clickButton)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_4, 2, 0, 1, 1)

        self.xPathLabel = QLabel(self.clickButton)
        self.xPathLabel.setObjectName(u"xPathLabel")

        self.gridLayout_6.addWidget(self.xPathLabel, 0, 0, 1, 1)

        self.xPathInput = QTextEdit(self.clickButton)
        self.xPathInput.setObjectName(u"xPathInput")
        self.xPathInput.setMaximumSize(QSize(16777215, 25))
        self.xPathInput.setStyleSheet(u"border:none; background:transparent")

        self.gridLayout_6.addWidget(self.xPathInput, 0, 1, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.funcSettings.addWidget(self.clickButton)
        self.clickScreenSettings = QWidget()
        self.clickScreenSettings.setObjectName(u"clickScreenSettings")
        self.gridLayout_7 = QGridLayout(self.clickScreenSettings)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.yCoordLabel = QLabel(self.clickScreenSettings)
        self.yCoordLabel.setObjectName(u"yCoordLabel")

        self.gridLayout_7.addWidget(self.yCoordLabel, 1, 0, 1, 1)

        self.xCoordLabel = QLabel(self.clickScreenSettings)
        self.xCoordLabel.setObjectName(u"xCoordLabel")

        self.gridLayout_7.addWidget(self.xCoordLabel, 0, 0, 1, 1)

        self.yCoordInputClick = QTextEdit(self.clickScreenSettings)
        self.yCoordInputClick.setObjectName(u"yCoordInputClick")
        self.yCoordInputClick.setMaximumSize(QSize(16777215, 25))
        self.yCoordInputClick.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_7.addWidget(self.yCoordInputClick, 1, 1, 1, 1)

        self.xCoordInputClick = QTextEdit(self.clickScreenSettings)
        self.xCoordInputClick.setObjectName(u"xCoordInputClick")
        self.xCoordInputClick.setMaximumSize(QSize(16777215, 25))
        self.xCoordInputClick.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_7.addWidget(self.xCoordInputClick, 0, 1, 1, 1)

        self.funcSettings.addWidget(self.clickScreenSettings)
        self.typewriteSettings = QWidget()
        self.typewriteSettings.setObjectName(u"typewriteSettings")
        self.gridLayout_8 = QGridLayout(self.typewriteSettings)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.contentInput = QTextEdit(self.typewriteSettings)
        self.contentInput.setObjectName(u"contentInput")
        self.contentInput.setMaximumSize(QSize(16777215, 25))
        self.contentInput.setStyleSheet(u"border:none; background:transparent;")

        self.gridLayout_8.addWidget(self.contentInput, 0, 1, 1, 1)

        self.contentLabel = QLabel(self.typewriteSettings)
        self.contentLabel.setObjectName(u"contentLabel")

        self.gridLayout_8.addWidget(self.contentLabel, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.funcSettings.addWidget(self.typewriteSettings)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_9 = QGridLayout(self.page)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.textEdit_4 = QTextEdit(self.page)
        self.textEdit_4.setObjectName(u"textEdit_4")
        self.textEdit_4.setMaximumSize(QSize(16777215, 25))
        self.textEdit_4.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_9.addWidget(self.textEdit_4, 0, 1, 1, 1)

        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 1, 0, 1, 1)

        self.funcSettings.addWidget(self.page)

        self.gridLayout_10.addWidget(self.funcSettings, 3, 0, 1, 2)

        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_10.addWidget(self.pushButton_2, 2, 0, 1, 2, Qt.AlignmentFlag.AlignTop)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_10.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 2)

        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 480, 94))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LabelLayout = QGridLayout()
        self.LabelLayout.setObjectName(u"LabelLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LabelLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.LabelLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 2)

        self.pushButton_3 = QPushButton(self)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 2)

        self.label_11 = QLabel(self)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 93, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 93, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 1)


        self.retranslateUi(self)

        self.stackedWidget.setCurrentIndex(0)
        self.trigSettings.setCurrentIndex(0)
        self.funcSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Workflow Creator</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"Trigger Selected:", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Add Trigger", None))
        self.triggerDropDown.setItemText(0, QCoreApplication.translate("Form", u"Hotkey", None))
        self.triggerDropDown.setItemText(1, QCoreApplication.translate("Form", u"Set interval", None))

        self.textEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Type your hotkey here", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Hotkey", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Interval:", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"Write your interval here", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Create Trigger</span></p></body></html>", None))
        self.functionDropDown.setItemText(0, QCoreApplication.translate("Form", u"Open Browser ", None))
        self.functionDropDown.setItemText(1, QCoreApplication.translate("Form", u"Click Button(Browser)", None))
        self.functionDropDown.setItemText(2, QCoreApplication.translate("Form", u"Click On Screen", None))
        self.functionDropDown.setItemText(3, QCoreApplication.translate("Form", u"Typewrite", None))
        self.functionDropDown.setItemText(4, QCoreApplication.translate("Form", u"Wait", None))

        self.label_7.setText(QCoreApplication.translate("Form", u"Browser URL", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("Form", u"Type your browser URL here", None))
        self.xPathLabel.setText(QCoreApplication.translate("Form", u"XPath:", None))
        self.xPathInput.setPlaceholderText(QCoreApplication.translate("Form", u"Type the XPath to the button here (Find in inspect element)", None))
        self.yCoordLabel.setText(QCoreApplication.translate("Form", u"Y-Coordinate", None))
        self.xCoordLabel.setText(QCoreApplication.translate("Form", u"X-Coordinate", None))
        self.yCoordInputClick.setPlaceholderText(QCoreApplication.translate("Form", u"Type your Y-Coordinate here", None))
        self.xCoordInputClick.setPlaceholderText(QCoreApplication.translate("Form", u"Type your X-Coordinate here", None))
        self.contentInput.setPlaceholderText(QCoreApplication.translate("Form", u"Type your content here", None))
        self.contentLabel.setText(QCoreApplication.translate("Form", u"Content", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("Form", u"Type your wait duration here", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Wait Duration", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Add Function", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Function Selected:", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Create Function</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Item List</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Compile Code", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"This is the part where I say where your code has been saved", None))
    # retranslateUi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(731, 558)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.MenuBar = QFrame(self.centralwidget)
        self.MenuBar.setObjectName(u"MenuBar")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MenuBar.sizePolicy().hasHeightForWidth())
        self.MenuBar.setSizePolicy(sizePolicy)
        self.MenuBar.setMinimumSize(QSize(125, 0))
        self.MenuBar.setMaximumSize(QSize(125, 16777215))
        self.MenuBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.MenuBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.MenuBar)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(4, 9, 4, 0)
        self.WorkflowsButton = QPushButton(self.MenuBar)
        self.WorkflowsButton.setObjectName(u"WorkflowsButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.WorkflowsButton.sizePolicy().hasHeightForWidth())
        self.WorkflowsButton.setSizePolicy(sizePolicy1)
        self.WorkflowsButton.setMinimumSize(QSize(100, 50))
        self.WorkflowsButton.setMaximumSize(QSize(100, 50))
        self.WorkflowsButton.setStyleSheet(u"text-align:left;")
        icon = QIcon()
        icon.addFile(u":/Icons/account_tree_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.WorkflowsButton.setIcon(icon)
        self.WorkflowsButton.setIconSize(QSize(20, 20))
        self.WorkflowsButton.setFlat(True)

        self.gridLayout_2.addWidget(self.WorkflowsButton, 2, 0, 1, 1)

        self.MenuText = QLabel(self.MenuBar)
        self.MenuText.setObjectName(u"MenuText")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.MenuText.sizePolicy().hasHeightForWidth())
        self.MenuText.setSizePolicy(sizePolicy2)

        self.gridLayout_2.addWidget(self.MenuText, 0, 0, 1, 1)

        self.SettingsButton = QPushButton(self.MenuBar)
        self.SettingsButton.setObjectName(u"SettingsButton")
        sizePolicy1.setHeightForWidth(self.SettingsButton.sizePolicy().hasHeightForWidth())
        self.SettingsButton.setSizePolicy(sizePolicy1)
        self.SettingsButton.setMinimumSize(QSize(100, 50))
        self.SettingsButton.setMaximumSize(QSize(100, 50))
        self.SettingsButton.setStyleSheet(u"text-align:left;")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/settings_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.SettingsButton.setIcon(icon1)
        self.SettingsButton.setIconSize(QSize(20, 20))
        self.SettingsButton.setFlat(True)

        self.gridLayout_2.addWidget(self.SettingsButton, 4, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.HomepageButton = QPushButton(self.MenuBar)
        self.HomepageButton.setObjectName(u"HomepageButton")
        sizePolicy1.setHeightForWidth(self.HomepageButton.sizePolicy().hasHeightForWidth())
        self.HomepageButton.setSizePolicy(sizePolicy1)
        self.HomepageButton.setMinimumSize(QSize(100, 50))
        self.HomepageButton.setMaximumSize(QSize(100, 50))
        self.HomepageButton.setStyleSheet(u"text-align:left;")
        icon2 = QIcon()
        icon2.addFile(u":/Icons/home_24dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.HomepageButton.setIcon(icon2)
        self.HomepageButton.setIconSize(QSize(20, 20))
        self.HomepageButton.setFlat(True)

        self.gridLayout_2.addWidget(self.HomepageButton, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 5, 0, 1, 1)

        self.ToolsButton = QPushButton(self.MenuBar)
        self.ToolsButton.setObjectName(u"ToolsButton")
        sizePolicy1.setHeightForWidth(self.ToolsButton.sizePolicy().hasHeightForWidth())
        self.ToolsButton.setSizePolicy(sizePolicy1)
        self.ToolsButton.setMinimumSize(QSize(100, 50))
        self.ToolsButton.setMaximumSize(QSize(100, 50))
        self.ToolsButton.setStyleSheet(u"text-align:left;")
        icon3 = QIcon()
        icon3.addFile(u":/Icons/build_circle_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ToolsButton.setIcon(icon3)
        self.ToolsButton.setIconSize(QSize(20, 20))
        self.ToolsButton.setFlat(True)

        self.gridLayout_2.addWidget(self.ToolsButton, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.MenuBar, 1, 0, 1, 1)

        self.Pages = QFrame(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy3)
        self.Pages.setMinimumSize(QSize(600, 0))
        self.Pages.setFrameShape(QFrame.Shape.StyledPanel)
        self.Pages.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.Pages)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 500))
        self.stackedWidget.setAcceptDrops(False)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.Shape.NoFrame)
        self.stackedWidget.setFrameShadow(QFrame.Shadow.Plain)
        self.Homepage = QWidget()
        self.Homepage.setObjectName(u"Homepage")
        self.gridLayout_5 = QGridLayout(self.Homepage)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_12 = QLabel(self.Homepage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.label_11 = QLabel(self.Homepage)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 2, 0, 1, 1)

        self.stackedWidget.addWidget(self.Homepage)
        self.Workflows = QWidget()
        self.Workflows.setObjectName(u"Workflows")
        self.gridLayout_8 = QGridLayout(self.Workflows)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.scrollArea = QScrollArea(self.Workflows)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 566, 417))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.Workflow1 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow1.setObjectName(u"Workflow1")
        self.Workflow1.setMinimumSize(QSize(0, 75))
        self.Workflow1.setMaximumSize(QSize(16777215, 75))
        self.Workflow1.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.Workflow1)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.StartWorkflow1 = QPushButton(self.Workflow1)
        self.StartWorkflow1.setObjectName(u"StartWorkflow1")
        self.StartWorkflow1.setMinimumSize(QSize(50, 50))
        self.StartWorkflow1.setMaximumSize(QSize(50, 50))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/start_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StartWorkflow1.setIcon(icon4)
        self.StartWorkflow1.setIconSize(QSize(50, 50))
        self.StartWorkflow1.setFlat(True)

        self.gridLayout_14.addWidget(self.StartWorkflow1, 0, 2, 1, 1)

        self.DeleteWorkflow1 = QPushButton(self.Workflow1)
        self.DeleteWorkflow1.setObjectName(u"DeleteWorkflow1")
        self.DeleteWorkflow1.setMinimumSize(QSize(50, 50))
        self.DeleteWorkflow1.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/delete_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DeleteWorkflow1.setIcon(icon5)
        self.DeleteWorkflow1.setIconSize(QSize(50, 50))
        self.DeleteWorkflow1.setFlat(True)

        self.gridLayout_14.addWidget(self.DeleteWorkflow1, 0, 3, 1, 1)

        self.label_17 = QLabel(self.Workflow1)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_14.addWidget(self.label_17, 0, 0, 1, 1)

        self.horizontalSpacer_8 = QSpacerItem(379, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_8, 0, 1, 1, 1)


        self.gridLayout_6.addWidget(self.Workflow1, 0, 0, 1, 1)

        self.Workflow2 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow2.setObjectName(u"Workflow2")
        self.Workflow2.setMinimumSize(QSize(0, 75))
        self.Workflow2.setMaximumSize(QSize(16777215, 75))
        self.Workflow2.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.Workflow2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_20 = QLabel(self.Workflow2)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_17.addWidget(self.label_20, 0, 0, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(379, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_17.addItem(self.horizontalSpacer_11, 0, 1, 1, 1)

        self.StartWorkflow2 = QPushButton(self.Workflow2)
        self.StartWorkflow2.setObjectName(u"StartWorkflow2")
        self.StartWorkflow2.setMinimumSize(QSize(50, 50))
        self.StartWorkflow2.setMaximumSize(QSize(50, 50))
        self.StartWorkflow2.setIcon(icon4)
        self.StartWorkflow2.setIconSize(QSize(50, 50))
        self.StartWorkflow2.setFlat(True)

        self.gridLayout_17.addWidget(self.StartWorkflow2, 0, 2, 1, 1)

        self.DeleteWorkflow2 = QPushButton(self.Workflow2)
        self.DeleteWorkflow2.setObjectName(u"DeleteWorkflow2")
        self.DeleteWorkflow2.setMinimumSize(QSize(50, 50))
        self.DeleteWorkflow2.setMaximumSize(QSize(50, 50))
        self.DeleteWorkflow2.setStyleSheet(u"")
        self.DeleteWorkflow2.setIcon(icon5)
        self.DeleteWorkflow2.setIconSize(QSize(50, 50))
        self.DeleteWorkflow2.setFlat(True)

        self.gridLayout_17.addWidget(self.DeleteWorkflow2, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.Workflow2, 1, 0, 1, 1)

        self.Workflow3 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow3.setObjectName(u"Workflow3")
        self.Workflow3.setMinimumSize(QSize(0, 75))
        self.Workflow3.setMaximumSize(QSize(16777215, 75))
        self.Workflow3.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_13 = QGridLayout(self.Workflow3)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.label_16 = QLabel(self.Workflow3)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_13.addWidget(self.label_16, 0, 0, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(379, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_7, 0, 1, 1, 1)

        self.StartWorkflow3 = QPushButton(self.Workflow3)
        self.StartWorkflow3.setObjectName(u"StartWorkflow3")
        self.StartWorkflow3.setMinimumSize(QSize(50, 50))
        self.StartWorkflow3.setMaximumSize(QSize(50, 50))
        self.StartWorkflow3.setIcon(icon4)
        self.StartWorkflow3.setIconSize(QSize(50, 50))
        self.StartWorkflow3.setFlat(True)

        self.gridLayout_13.addWidget(self.StartWorkflow3, 0, 2, 1, 1)

        self.DeleteWorkflow3 = QPushButton(self.Workflow3)
        self.DeleteWorkflow3.setObjectName(u"DeleteWorkflow3")
        self.DeleteWorkflow3.setMinimumSize(QSize(50, 50))
        self.DeleteWorkflow3.setMaximumSize(QSize(50, 50))
        self.DeleteWorkflow3.setIcon(icon5)
        self.DeleteWorkflow3.setIconSize(QSize(50, 50))
        self.DeleteWorkflow3.setFlat(True)

        self.gridLayout_13.addWidget(self.DeleteWorkflow3, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.Workflow3, 2, 0, 1, 1)

        self.Workflow4 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow4.setObjectName(u"Workflow4")
        self.Workflow4.setMinimumSize(QSize(0, 75))
        self.Workflow4.setMaximumSize(QSize(16777215, 75))
        self.Workflow4.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow4.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_16 = QGridLayout(self.Workflow4)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_19 = QLabel(self.Workflow4)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_16.addWidget(self.label_19, 0, 0, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(379, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_10, 0, 1, 1, 1)

        self.StartWorkflow4 = QPushButton(self.Workflow4)
        self.StartWorkflow4.setObjectName(u"StartWorkflow4")
        self.StartWorkflow4.setMinimumSize(QSize(50, 50))
        self.StartWorkflow4.setMaximumSize(QSize(50, 50))
        self.StartWorkflow4.setIcon(icon4)
        self.StartWorkflow4.setIconSize(QSize(50, 50))
        self.StartWorkflow4.setFlat(True)

        self.gridLayout_16.addWidget(self.StartWorkflow4, 0, 2, 1, 1)

        self.DeleteWorkflow4 = QPushButton(self.Workflow4)
        self.DeleteWorkflow4.setObjectName(u"DeleteWorkflow4")
        self.DeleteWorkflow4.setMinimumSize(QSize(50, 50))
        self.DeleteWorkflow4.setMaximumSize(QSize(50, 50))
        self.DeleteWorkflow4.setIcon(icon5)
        self.DeleteWorkflow4.setIconSize(QSize(50, 50))
        self.DeleteWorkflow4.setFlat(True)

        self.gridLayout_16.addWidget(self.DeleteWorkflow4, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.Workflow4, 3, 0, 1, 1)

        self.Workflow5 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow5.setObjectName(u"Workflow5")
        self.Workflow5.setMinimumSize(QSize(0, 75))
        self.Workflow5.setMaximumSize(QSize(16777215, 75))
        self.Workflow5.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow5.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.Workflow5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.VerticalSpacer_Temp = QFrame(self.scrollAreaWidgetContents)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 5, 0, 1, 1)
        self.gridLayout_15.addItem(self.horizontalSpacer_9, 1, 1, 1, 1)

        self.DeleteWorkflow5 = QPushButton(self.Workflow5)
        self.DeleteWorkflow5.setObjectName(u"DeleteWorkflow5")
        self.DeleteWorkflow5.setMinimumSize(QSize(50, 50))
        self.DeleteWorkflow5.setMaximumSize(QSize(50, 50))
        self.DeleteWorkflow5.setIcon(icon5)
        self.DeleteWorkflow5.setIconSize(QSize(50, 50))
        self.DeleteWorkflow5.setFlat(True)

        self.gridLayout_15.addWidget(self.DeleteWorkflow5, 1, 3, 1, 1)

        self.label_18 = QLabel(self.Workflow5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_15.addWidget(self.label_18, 1, 0, 1, 1)

        self.StartWorkflow5 = QPushButton(self.Workflow5)
        self.StartWorkflow5.setObjectName(u"StartWorkflow5")
        self.StartWorkflow5.setMinimumSize(QSize(50, 50))
        self.StartWorkflow5.setMaximumSize(QSize(50, 50))
        self.StartWorkflow5.setIcon(icon4)
        self.StartWorkflow5.setIconSize(QSize(50, 50))
        self.StartWorkflow5.setFlat(True)

        self.gridLayout_15.addWidget(self.StartWorkflow5, 1, 2, 1, 1)


        self.gridLayout_6.addWidget(self.Workflow5, 4, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_8.addWidget(self.scrollArea, 2, 0, 1, 1)

        self.label = QLabel(self.Workflows)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.Workflows)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))

        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Workflows)
        self.Tools = QWidget()
        self.Tools.setObjectName(u"Tools")
        self.formLayout = QFormLayout(self.Tools)
        self.formLayout.setObjectName(u"formLayout")
        self.label_13 = QLabel(self.Tools)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setWordWrap(True)

        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.label_13)

        self.stackedWidget.addWidget(self.Tools)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.gridLayout_7 = QGridLayout(self.Settings)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.customToggle = CustomToggle(self.Settings)
        self.customToggle.setObjectName(u"buttonToggle")
        self.gridLayout_7.addWidget(self.customToggle, 1, 0, 1, 1, Qt.AlignmentFlag.AlignLeft)
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 2, 0, 1, 1)

        self.label_3 = QLabel(self.Settings)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_7.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Settings)

        self.gridLayout_4.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.Pages, 1, 1, 1, 1)

        self.TopBar = QFrame(self.centralwidget)
        self.TopBar.setObjectName(u"TopBar")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.TopBar.sizePolicy().hasHeightForWidth())
        self.TopBar.setSizePolicy(sizePolicy4)
        self.TopBar.setMinimumSize(QSize(50, 50))
        self.TopBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.TopBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.TopBar)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.TopBar)
        self.label_2.setObjectName(u"label_2")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy5)

        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)

        self.MenuButton = QPushButton(self.TopBar)
        self.MenuButton.setObjectName(u"MenuButton")
        sizePolicy1.setHeightForWidth(self.MenuButton.sizePolicy().hasHeightForWidth())
        self.MenuButton.setSizePolicy(sizePolicy1)
        self.MenuButton.setMinimumSize(QSize(50, 50))
        self.MenuButton.setMaximumSize(QSize(50, 50))
        self.MenuButton.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        icon6 = QIcon()
        icon6.addFile(u":/Icons/menu_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MenuButton.setIcon(icon6)
        self.MenuButton.setIconSize(QSize(50, 50))
        self.MenuButton.setFlat(True)

        self.gridLayout_3.addWidget(self.MenuButton, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.TopBar, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
        def hidemenu():
            if self.MenuBar.isVisible():
                self.MenuBar.hide()
            elif self.MenuBar.isHidden():
                self.MenuBar.show()
        self.MenuButton.clicked.connect(hidemenu)
        self.HomepageButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.WorkflowsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.ToolsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.SettingsButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        def setButtonSize(iconsize, buttonwidth):
            self.SettingsButton.setIconSize(QSize(iconsize, iconsize))
            self.HomepageButton.setIconSize(QSize(iconsize, iconsize))
            self.WorkflowsButton.setIconSize(QSize(iconsize, iconsize))
            self.ToolsButton.setIconSize(QSize(iconsize, iconsize))
            self.SettingsButton.setMinimumWidth(buttonwidth)
            self.ToolsButton.setMinimumWidth(buttonwidth)
            self.HomepageButton.setMinimumWidth(buttonwidth)
            self.WorkflowsButton.setMinimumWidth(buttonwidth)
            self.SettingsButton.setFixedWidth(buttonwidth)
            self.WorkflowsButton.setFixedWidth(buttonwidth)
            self.HomepageButton.setFixedWidth(buttonwidth)
            self.ToolsButton.setFixedWidth(buttonwidth)    
            self.WorkflowsButton.setStyleSheet('text-align:right')
            self.SettingsButton.setStyleSheet('text-align:right')
            self.HomepageButton.setStyleSheet('text-align:right')

        def compactMode():
            abspath = path.dirname(path.abspath(__file__))
            savedsettings = open(path.join(abspath, r'Files\Settings\compact-mode.txt'), 'r')
            compacttext = savedsettings.read()
            if compacttext == 'False':
                savedsettings.close()
                settingstext = open(path.join(abspath, r'Files\Settings\compact-mode.txt'), 'w')
                settingstext.write('True')             
                settingstext.close()
                self.MenuText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:700;\">Menu</span></p></body></html>", None))
                self.SettingsButton.setText("")
                self.HomepageButton.setText("")
                self.WorkflowsButton.setText("")
                self.ToolsButton.setText("")
                setButtonSize(iconsize=25, buttonwidth=40)
                self.MenuBar.setFixedWidth(50)
                self.ToolsButton.setStyleSheet('text-align:left')
                self.WorkflowsButton.setStyleSheet('text-align:left')
                self.SettingsButton.setStyleSheet('text-align:left')
                self.HomepageButton.setStyleSheet('text-align:left')
                self.ToolsButton.setStyleSheet('QPushButton {text-align: center;}')
                self.HomepageButton.setStyleSheet('QPushButton {text-align: center;}')
                self.WorkflowsButton.setStyleSheet('QPushButton {text-align: center;}')
                self.SettingsButton.setStyleSheet('QPushButton {text-align: center;}')
            elif compacttext == 'True':
                savedsettings.close()
                settingstext = open(path.join(abspath, r'Files\Settings\compact-mode.txt'), 'w')
                settingstext.write('False')
                settingstext.close()
                self.MenuText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Menu</span></p></body></html>", None))
                setButtonSize(iconsize=20, buttonwidth=100)
                self.SettingsButton.setText("Settings")
                self.HomepageButton.setText("Homepage")
                self.WorkflowsButton.setText("Workflows")
                self.ToolsButton.setText("Tools")
                self.MenuBar.setFixedWidth(100)
                self.ToolsButton.setStyleSheet('QPushButton{text-align: left;}')
                self.WorkflowsButton.setStyleSheet('QPushButton{text-align: left;}')
                self.HomepageButton.setStyleSheet('QPushButton{text-align: left;}')
                self.SettingsButton.setStyleSheet('QPushButton{text-align: left;}')
        self.customToggle.stateChanged.connect(compactMode)    
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.WorkflowsButton.setText(QCoreApplication.translate("MainWindow", u"Workflows", None))
        self.MenuText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Menu</span></p></body></html>", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.HomepageButton.setText(QCoreApplication.translate("MainWindow", u"Homepage", None))
        self.ToolsButton.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"This is the draft of an app meant to automate certain tasks. It is going to be made for Daniel Emmer's Personal Project. ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">What is this?</span></p></body></html>", None))
        self.StartWorkflow1.setText("")
        self.DeleteWorkflow1.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Workflow 1", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Workflow 2", None))
        self.StartWorkflow2.setText("")
        self.DeleteWorkflow2.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Workflow 3", None))
        self.StartWorkflow3.setText("")
        self.DeleteWorkflow3.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Workflow 4", None))
        self.StartWorkflow4.setText("")
        self.DeleteWorkflow4.setText("")
        self.DeleteWorkflow5.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Workflow 5", None))
        self.StartWorkflow5.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Current Workflows</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Workflow Creator", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"This part is an extra part of the app, if I finish and still want to keep going to improve the user experience of the app, etc. I will only need to do this after I finish all of the other parts of my app.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Compact Mode</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Page Name</span></p></body></html>", None))
        self.MenuButton.setText("")
    # retranslateUi
        def setButtonSize(iconsize, buttonwidth):
            self.SettingsButton.setIconSize(QSize(iconsize, iconsize))
            self.HomepageButton.setIconSize(QSize(iconsize, iconsize))
            self.WorkflowsButton.setIconSize(QSize(iconsize, iconsize))
            self.ToolsButton.setIconSize(QSize(iconsize, iconsize))
            self.SettingsButton.setMinimumWidth(buttonwidth)
            self.ToolsButton.setMinimumWidth(buttonwidth)
            self.HomepageButton.setMinimumWidth(buttonwidth)
            self.WorkflowsButton.setMinimumWidth(buttonwidth)
            self.SettingsButton.setFixedWidth(buttonwidth)
            self.WorkflowsButton.setFixedWidth(buttonwidth)
            self.HomepageButton.setFixedWidth(buttonwidth)
            self.ToolsButton.setFixedWidth(buttonwidth)    
            self.WorkflowsButton.setStyleSheet('text-align:right')
            self.SettingsButton.setStyleSheet('text-align:right')
            self.HomepageButton.setStyleSheet('text-align:right')
        def update_page_label():
            current_widget = self.stackedWidget.currentWidget()
            page_name = current_widget.objectName()
            print(page_name)
            self.label_2.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">{page_name}</span></p></body></html>", None))
        self.stackedWidget.currentChanged.connect(update_page_label)
        update_page_label()
        abspath = path.dirname(path.abspath(__file__))
        savedsettings = open(path.join(abspath, r'Files\Settings\compact-mode.txt'), 'r')
        compacttext = savedsettings.read()
        if compacttext == 'True':
            self.customToggle.setCheckState(Qt.CheckState.Checked)
            self.MenuText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt; font-weight:700;\">Menu</span></p></body></html>", None))
            self.MenuBar.setFixedWidth(50)
            setButtonSize(25,40)
            self.SettingsButton.setText("")
            self.HomepageButton.setText("")
            self.WorkflowsButton.setText("")
            self.ToolsButton.setText("")
            self.ToolsButton.setStyleSheet('text-align:left')
            self.WorkflowsButton.setStyleSheet('text-align:left')
            self.SettingsButton.setStyleSheet('text-align:left')
            self.HomepageButton.setStyleSheet('text-align:left')
            self.ToolsButton.setStyleSheet('QPushButton {text-align: center;}')
            self.HomepageButton.setStyleSheet('QPushButton {text-align: center;}')
            self.WorkflowsButton.setStyleSheet('QPushButton {text-align: center;}')
            self.SettingsButton.setStyleSheet('QPushButton {text-align: center;}')
        else:
            self.customToggle.setCheckState(Qt.CheckState.Unchecked)
            self.MenuText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Menu</span></p></body></html>", None))
            setButtonSize(iconsize=20, buttonwidth=100)
            self.SettingsButton.setText("Settings")
            self.HomepageButton.setText("Homepage")
            self.WorkflowsButton.setText("Workflows")
            self.ToolsButton.setText("Tools")
            self.MenuBar.setFixedWidth(100)
            self.ToolsButton.setStyleSheet('QPushButton{text-align: left;}')
            self.WorkflowsButton.setStyleSheet('QPushButton{text-align: left;}')
            self.HomepageButton.setStyleSheet('QPushButton{text-align: left;}')
            self.SettingsButton.setStyleSheet('QPushButton{text-align: left;}')
            abspath = path.dirname(path.abspath(__file__))
            Workflow1Exists = isfile(path.join(abspath, 'Files/workflows/workflow1.py'))
            Workflow22Exists = isfile(path.join(abspath, 'Files/workflows/workflow2.py'))
            Workflow3Exists = isfile(path.join(abspath, 'Files/workflows/workflow3.py'))
            Workflow4Exists = isfile(path.join(abspath, 'Files/workflows/workflow4.py'))
            Workflow5Exists = isfile(path.join(abspath, 'Files/workflows/workflow5.py'))
            if Workflow1Exists is True:
                self.Workflow1.setVisible(True)
            else:
                self.Workflow1.setVisible(False)
            if Workflow22Exists is True:
                self.Workflow2.setVisible(True)
            else:
                self.Workflow2.setVisible(False)
            if Workflow3Exists is True:
                self.Workflow3.setVisible(True)
            else:
                self.Workflow3.setVisible(False)
            if Workflow4Exists is True:
                self.Workflow4.setVisible(True)
            else:
                self.Workflow4.setVisible(False)
            if Workflow5Exists is True:
                self.Workflow5.setVisible(True)
            else:
                self.Workflow5.setVisible(False)
            class runStart:
                def run(self, num):
                    from pyautogui import typewrite, click
                    import keyboard
                    import undetected_chromedriver as uc
                    from selenium.webdriver.common.by import By
                    from selenium.webdriver.support import expected_conditions as EC
                    from time import sleep as wait
                    from os import _exit
                    abspath = path.dirname(path.abspath(__file__))
                    workflow_path = path.join(abspath, 'Files/workflows/workflow' + str(num) + '.py')
                    globals_dict = {
                        'typewrite': typewrite,
                        'click': click,
                        'keyboard': keyboard,
                        'uc': uc,
                        'By': By,
                        'EC': EC,
                        'wait': wait,
                        '_exit': _exit
                    }
                    globals_dict['WORKFLOW_PATH'] = workflow_path
                    exec(open(path.join(abspath, 'Files/workflows/workflow' + str(num) + '.py')).read(), globals_dict)
            def runStartWorkflow(num):
                worker = runStart()
                thread = threading.Thread(target=worker.run, args=(num,))  
                thread.start()
            
            self.StartWorkflow1.clicked.connect(lambda: runStartWorkflow(1))
            self.StartWorkflow2.clicked.connect(lambda: runStartWorkflow(2))
            self.StartWorkflow3.clicked.connect(lambda: runStartWorkflow(3))
            self.StartWorkflow4.clicked.connect(lambda: runStartWorkflow(4))
            self.StartWorkflow5.clicked.connect(lambda: runStart(5))
            class runDelete():
                def run(self,num):
                    abspath = path.dirname(path.abspath(__file__))
                    remove(path.join(abspath, f'Files/Workflows/Workflow{num}.py'))
            def runDeleteWorkflow(num):
                worker = runDelete()
                thread = threading.Thread(target=worker.run, args=(num,))  
                thread.start()
            self.DeleteWorkflow1.clicked.connect(lambda: runDeleteWorkflow(1))
            self.DeleteWorkflow2.clicked.connect(lambda: runDeleteWorkflow(2))
            self.DeleteWorkflow3.clicked.connect(lambda: runDeleteWorkflow(3))
            self.DeleteWorkflow4.clicked.connect(lambda: runDeleteWorkflow(4))
            self.DeleteWorkflow5.clicked.connect(lambda: runDeleteWorkflow(5))

    # setupUi