# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'itsawidgetnow.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(500, 500)
        Form.setMinimumSize(QSize(500, 500))
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.stackedWidget = QStackedWidget(Form)
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

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.scrollArea = QScrollArea(Form)
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

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 2)

        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 93, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 93, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 6, 1, 1, 1)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)
        self.trigSettings.setCurrentIndex(0)
        self.funcSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
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

