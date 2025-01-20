# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WorkflowMakereEWWmb.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout, QFileDialog,
    QWidget, QLineEdit, QPlainTextEdit)
from os import path

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(665, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 645, 125))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LabelLayout = QGridLayout()
        self.LabelLayout.setObjectName(u"LabelLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LabelLayout.addItem(self.verticalSpacer_3, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.LabelLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 2)

        self.compileResult = QLabel(self.centralwidget)
        self.compileResult.setObjectName(u"compileResult")

        self.gridLayout.addWidget(self.compileResult, 5, 0, 1, 2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 9, 1, 1, 1)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.CompileButton = QPushButton(self.centralwidget)
        self.CompileButton.setObjectName(u"CompileButton")

        self.gridLayout.addWidget(self.CompileButton, 4, 0, 1, 2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMaximumSize(QSize(16777215, 200))
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
        self.trigSettings.setMinimumSize(QSize(200, 75))
        self.trigSettings.setMaximumSize(QSize(16777215, 100))
        self.instantRunSettings = QWidget()
        self.instantRunSettings.setObjectName(u"instantRunSettings")
        self.gridLayout_4 = QGridLayout(self.instantRunSettings)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_24 = QLabel(self.instantRunSettings)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)

        self.label_25 = QLabel(self.instantRunSettings)
        self.label_25.setObjectName(u"label_25")

        self.gridLayout_4.addWidget(self.label_25, 1, 0, 1, 1)

        self.trigSettings.addWidget(self.instantRunSettings)
        self.hotkeySettings = QWidget()
        self.hotkeySettings.setObjectName(u"hotkeySettings")
        self.hotkeySettings.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_2 = QGridLayout(self.hotkeySettings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.label_5 = QLabel(self.hotkeySettings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(self.hotkeySettings)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background:transparent; border:none;")
        self.lineEdit.setMaxLength(1)

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.trigSettings.addWidget(self.hotkeySettings)

        self.gridLayout_3.addWidget(self.trigSettings, 4, 0, 1, 2)

        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_10 = QGridLayout(self.page_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_10.addWidget(self.pushButton_2, 2, 0, 1, 2, Qt.AlignmentFlag.AlignTop)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_10.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 2)

        self.functionDropDown = QComboBox(self.page_3)
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
        self.functionDropDown.addItem("")
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
        self.funcSettings.setMinimumSize(QSize(0, 75))
        self.funcSettings.setMaximumSize(QSize(16777215, 100))
        self.openBrowserSettings = QWidget()
        self.openBrowserSettings.setObjectName(u"openBrowserSettings")
        self.gridLayout_5 = QGridLayout(self.openBrowserSettings)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_7 = QLabel(self.openBrowserSettings)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.URLInput = QPlainTextEdit(self.openBrowserSettings)
        self.URLInput.setObjectName(u"URLInput")
        self.URLInput.setMaximumSize(QSize(16777215, 25))
        self.URLInput.setStyleSheet(u"background:transparent;  border:none;")
        self.URLInput.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.URLInput.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.URLInput.setMaximumBlockCount(1)

        self.gridLayout_5.addWidget(self.URLInput, 0, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_6, 1, 0, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 1, 1, 1, 1)

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

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_5, 2, 1, 1, 1)

        self.xPathInput = QPlainTextEdit(self.clickButton)
        self.xPathInput.setObjectName(u"xPathInput")
        self.xPathInput.setMaximumSize(QSize(16777215, 25))
        self.xPathInput.setStyleSheet(u"border:none; background:transparent;")

        self.gridLayout_6.addWidget(self.xPathInput, 0, 1, 1, 1)

        self.funcSettings.addWidget(self.clickButton)
        self.clickScreenSettings = QWidget()
        self.clickScreenSettings.setObjectName(u"clickScreenSettings")
        self.gridLayout_7 = QGridLayout(self.clickScreenSettings)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.plainTextEdit = QPlainTextEdit(self.clickScreenSettings)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setMaximumSize(QSize(16777215, 25))
        self.plainTextEdit.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_7.addWidget(self.plainTextEdit, 2, 1, 1, 1)

        self.xCoordInputClick = QPlainTextEdit(self.clickScreenSettings)
        self.xCoordInputClick.setObjectName(u"xCoordInputClick")
        self.xCoordInputClick.setMaximumSize(QSize(16777215, 25))
        self.xCoordInputClick.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_7.addWidget(self.xCoordInputClick, 0, 1, 1, 1)

        self.yCoordLabel = QLabel(self.clickScreenSettings)
        self.yCoordLabel.setObjectName(u"yCoordLabel")

        self.gridLayout_7.addWidget(self.yCoordLabel, 2, 0, 1, 1)

        self.xCoordLabel = QLabel(self.clickScreenSettings)
        self.xCoordLabel.setObjectName(u"xCoordLabel")

        self.gridLayout_7.addWidget(self.xCoordLabel, 0, 0, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_9, 3, 0, 1, 2)

        self.funcSettings.addWidget(self.clickScreenSettings)
        self.typewriteSettings = QWidget()
        self.typewriteSettings.setObjectName(u"typewriteSettings")
        self.gridLayout_8 = QGridLayout(self.typewriteSettings)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.contentLabel = QLabel(self.typewriteSettings)
        self.contentLabel.setObjectName(u"contentLabel")

        self.gridLayout_8.addWidget(self.contentLabel, 0, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.label_12 = QLabel(self.typewriteSettings)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_8.addWidget(self.label_12, 1, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.intervalInput = QPlainTextEdit(self.typewriteSettings)
        self.intervalInput.setObjectName(u"intervalInput")
        self.intervalInput.setMaximumSize(QSize(16777215, 25))
        self.intervalInput.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_8.addWidget(self.intervalInput, 1, 2, 1, 1)

        self.contentInput = QPlainTextEdit(self.typewriteSettings)
        self.contentInput.setObjectName(u"contentInput")
        self.contentInput.setMaximumSize(QSize(16777215, 25))
        self.contentInput.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_8.addWidget(self.contentInput, 0, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_10, 2, 0, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_11, 2, 2, 1, 1)

        self.funcSettings.addWidget(self.typewriteSettings)
        self.waitSettings = QWidget()
        self.waitSettings.setObjectName(u"waitSettings")
        self.gridLayout_9 = QGridLayout(self.waitSettings)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.label_8 = QLabel(self.waitSettings)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_7, 2, 0, 1, 1)

        self.waitInput = QPlainTextEdit(self.waitSettings)
        self.waitInput.setObjectName(u"waitInput")
        self.waitInput.setMaximumSize(QSize(16777215, 25))
        self.waitInput.setStyleSheet(u"background:transparent; border:none")

        self.gridLayout_9.addWidget(self.waitInput, 0, 1, 1, 1)

        self.funcSettings.addWidget(self.waitSettings)
        self.pressKeySettings = QWidget()
        self.pressKeySettings.setObjectName(u"pressKeySettings")
        self.gridLayout_11 = QGridLayout(self.pressKeySettings)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.keyInput = QLineEdit(self.pressKeySettings)
        self.keyInput.setObjectName(u"keyInput")
        self.keyInput.setStyleSheet(u"background:transparent; border:none;")
        self.keyInput.setMaxLength(1)

        self.gridLayout_11.addWidget(self.keyInput, 0, 1, 1, 1)

        self.keyLabel = QLabel(self.pressKeySettings)
        self.keyLabel.setObjectName(u"keyLabel")

        self.gridLayout_11.addWidget(self.keyLabel, 0, 0, 1, 1)

        self.verticalSpacer_13 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_11.addItem(self.verticalSpacer_13, 1, 0, 1, 2)

        self.funcSettings.addWidget(self.pressKeySettings)
        self.keypressCombinationSettings = QWidget()
        self.keypressCombinationSettings.setObjectName(u"keypressCombinationSettings")
        self.gridLayout_15 = QGridLayout(self.keypressCombinationSettings)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.keyLabel_3 = QLabel(self.keypressCombinationSettings)
        self.keyLabel_3.setObjectName(u"keyLabel_3")

        self.gridLayout_15.addWidget(self.keyLabel_3, 0, 0, 1, 1)

        self.keyInput_2 = QLineEdit(self.keypressCombinationSettings)
        self.keyInput_2.setObjectName(u"keyInput_2")
        self.keyInput_2.setStyleSheet(u"background:transparent; border:none;")
        self.keyInput_2.setMaxLength(15)

        self.gridLayout_15.addWidget(self.keyInput_2, 0, 1, 1, 1)

        self.keyLabel_4 = QLabel(self.keypressCombinationSettings)
        self.keyLabel_4.setObjectName(u"keyLabel_4")

        self.gridLayout_15.addWidget(self.keyLabel_4, 1, 0, 1, 1)

        self.keyInput_3 = QLineEdit(self.keypressCombinationSettings)
        self.keyInput_3.setObjectName(u"keyInput_3")
        self.keyInput_3.setStyleSheet(u"background:transparent; border:none;")
        self.keyInput_3.setMaxLength(15)

        self.gridLayout_15.addWidget(self.keyInput_3, 1, 1, 1, 1)

        self.funcSettings.addWidget(self.keypressCombinationSettings)
        self.clickImagesettings = QWidget()
        self.clickImagesettings.setObjectName(u"clickImagesettings")
        self.gridLayout_12 = QGridLayout(self.clickImagesettings)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.lineEdit_2 = QLineEdit(self.clickImagesettings)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"background:transparent; border:none;")
        self.lineEdit_2.setMaxLength(2)

        self.gridLayout_12.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.keyLabel_2 = QLabel(self.clickImagesettings)
        self.keyLabel_2.setObjectName(u"keyLabel_2")

        self.gridLayout_12.addWidget(self.keyLabel_2, 0, 0, 1, 1)

        self.label_14 = QLabel(self.clickImagesettings)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_12.addWidget(self.label_14, 1, 0, 1, 1)

        self.funcSettings.addWidget(self.clickImagesettings)
        self.newWindow = QWidget()
        self.newWindow.setObjectName(u"newWindow")
        self.gridLayout_14 = QGridLayout(self.newWindow)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.label_11 = QLabel(self.newWindow)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_14.addWidget(self.label_11, 0, 0, 1, 1)

        self.label_15 = QLabel(self.newWindow)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_14.addWidget(self.label_15, 1, 0, 1, 1)

        self.funcSettings.addWidget(self.newWindow)
        self.closeWindow = QWidget()
        self.closeWindow.setObjectName(u"closeWindow")
        self.gridLayout_16 = QGridLayout(self.closeWindow)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.label_16 = QLabel(self.closeWindow)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_16.addWidget(self.label_16, 0, 0, 1, 1)

        self.label_17 = QLabel(self.closeWindow)
        self.label_17.setObjectName(u"label_17")

        self.gridLayout_16.addWidget(self.label_17, 1, 0, 1, 1)

        self.funcSettings.addWidget(self.closeWindow)
        self.nextWindowSettings = QWidget()
        self.nextWindowSettings.setObjectName(u"nextWindowSettings")
        self.gridLayout_19 = QGridLayout(self.nextWindowSettings)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.label_22 = QLabel(self.nextWindowSettings)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_19.addWidget(self.label_22, 0, 0, 1, 1)

        self.label_23 = QLabel(self.nextWindowSettings)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_19.addWidget(self.label_23, 1, 0, 1, 1)

        self.funcSettings.addWidget(self.nextWindowSettings)
        self.previousWindowSettings = QWidget()
        self.previousWindowSettings.setObjectName(u"previousWindowSettings")
        self.gridLayout_17 = QGridLayout(self.previousWindowSettings)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.label_18 = QLabel(self.previousWindowSettings)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_17.addWidget(self.label_18, 0, 0, 1, 1)

        self.label_19 = QLabel(self.previousWindowSettings)
        self.label_19.setObjectName(u"label_19")

        self.gridLayout_17.addWidget(self.label_19, 1, 0, 1, 1)

        self.funcSettings.addWidget(self.previousWindowSettings)
        self.newTabSettings = QWidget()
        self.newTabSettings.setObjectName(u"newTabSettings")
        self.gridLayout_13 = QGridLayout(self.newTabSettings)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.tabInput = QPlainTextEdit(self.newTabSettings)
        self.tabInput.setObjectName(u"tabInput")
        self.tabInput.setMaximumSize(QSize(16777215, 25))
        self.tabInput.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_13.addWidget(self.tabInput, 0, 1, 1, 1)

        self.tabLabel = QLabel(self.newTabSettings)
        self.tabLabel.setObjectName(u"tabLabel")

        self.gridLayout_13.addWidget(self.tabLabel, 0, 0, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_12, 1, 0, 1, 2)

        self.funcSettings.addWidget(self.newTabSettings)
        self.closeTabSettings = QWidget()
        self.closeTabSettings.setObjectName(u"closeTabSettings")
        self.gridLayout_18 = QGridLayout(self.closeTabSettings)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.label_20 = QLabel(self.closeTabSettings)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_18.addWidget(self.label_20, 0, 0, 1, 1)

        self.label_21 = QLabel(self.closeTabSettings)
        self.label_21.setObjectName(u"label_21")

        self.gridLayout_18.addWidget(self.label_21, 1, 0, 1, 1)

        self.funcSettings.addWidget(self.closeTabSettings)

        self.gridLayout_10.addWidget(self.funcSettings, 3, 0, 1, 2)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 1, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.trigSettings.setCurrentIndex(0)
        self.funcSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
        def openFile():
            dialog = QFileDialog()
            dialog.setNameFilter('Images (*.png *.jpg *.jpeg)')
            dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
            
            dialogSuccessful = dialog.exec()
            if dialogSuccessful == 1:
                global files
                files = dialog.selectedFiles()
                
            else:
                print('dialog canceled')
                return
        self.button = QPushButton('Choose File')
        self.button.clicked.connect(openFile)
        self.gridLayout_12.addWidget(self.button, 0, 1, 1, 1)
        orderedMethod = {}
        def syncFunc():
            dropIndex = self.functionDropDown.currentIndex()
            self.funcSettings.setCurrentIndex(dropIndex)
        self.functionDropDown.currentIndexChanged.connect(syncFunc)
        def syncTrig():
            dropIndex = self.triggerDropDown.currentIndex()
            self.trigSettings.setCurrentIndex(dropIndex)
        self.functionDropDown.currentIndexChanged.connect(syncFunc)
        self.triggerDropDown.currentIndexChanged.connect(syncTrig)
        def AddTrigger():
            trigIndex = str(self.triggerDropDown.currentIndex()) # current index of the trigger dropdown
            indexKey = {
                0 : 'Instantly Run',
                1 : 'Hotkey',
            
            }
            trigName = indexKey.get(int(trigIndex))
            count = self.LabelLayout.count() - 1
            if trigIndex == '0':
                orderedMethod[count] = {'type': 'InstantRun'}
                additionalContent = ('')
            if trigIndex == '1':
                hotkey = self.lineEdit.text()
                if len(hotkey) == 0:
                    return
                orderedMethod[count] = {'type': 'Hotkey', 'hotkey': hotkey}
                additionalContent = ('hotkey=' + hotkey)
            self.label = QLabel(trigName + ' ' + additionalContent)
            self.label.setObjectName(u"step" + str(count))
            self.LabelLayout.addWidget(self.label, count, 0, 1, 1)
            print(orderedMethod)
        def AddFunction():
            funcIndex = str(self.functionDropDown.currentIndex()) # current index of the function dropdown
            count = self.LabelLayout.count() - 1

            #! FuncIndex = 0
            indexKey = {
                0 : 'Open Browser', #Working
                1 : 'Click Button', #Working
                2 : 'Click on Screen', #Working
                3 : 'Typewrite', #Working
                4 : 'Wait', #Working
                5 : 'Press Key', #!UNTESTED
                6 : 'Press Key Combination', #!UNTESTED
                7 : 'Click Image', #*TBD 
                8 : 'New Desktop', #*TBD
                9 : 'Close Desktop', #*TBD
                10 : 'Next Desktop', #*TBD
                11 : 'Previous Desktop', #*TBD
                12 : 'New Tab', #*TBD
                13 : 'Close Tab' #*TBD
            }
            if funcIndex == '0':
                url = self.URLInput.toPlainText()
                if url.startswith('http://'):
                    url = url[7:]
                if url.startswith('https://'):
                    url = url[8:]
                if len(url) == 0:
                    return
                url = 'https://' + url
                orderedMethod[count] = {'type': 'Open Browser', 'url': url}
                additionalContent = ('URL: ' + url)
            if funcIndex == '1':
                xPath = self.xPathInput.toPlainText()
                if len(xPath) == 0:
                    return
                orderedMethod[count] = {'type': 'Click Button', 'xpath': xPath}
                additionalContent = ('xPath: ' + xPath)
            if funcIndex == '2':
                xCoord = self.xCoordInputClick.toPlainText()
                yCoord = self.yCoordInputClick.toPlainText()
                if len(xCoord) == 0 or len(yCoord) == 0:
                    return
                orderedMethod[count] = {'type':'Click on Screen', 'xcoord': xCoord, 'ycoord': yCoord}
                additionalContent = ('xCoord: ' + xCoord + ' yCoord: ' + yCoord)
            if funcIndex == '3':
                content = self.contentInput.toPlainText()
                if len(content) == 0:
                    return
                orderedMethod[count] = {'type': 'Typewrite', 'content': content}
                additionalContent = ('content: ' + content)
            if funcIndex == '4':
                duration = self.waitInput.toPlainText()
                if len(duration) == 0:
                    return
                orderedMethod[count] = {'type': 'Wait', 'duration': duration}
                additionalContent = ('duration: ' + duration)
            if funcIndex == '5':
                key = self.keyInput.text()
                if len(key) == 0:
                    return
                orderedMethod[count] = {'type': 'Press Key', 'key': key}
                additionalContent = ('key: ' + key)
            if funcIndex == '6':
                key1 = self.keyInput_2.text()
                key2 = self.keyInput_3.text()
                if len(key1) == 0 or len(key2) == 0:
                    return
                orderedMethod[count] = {'type': 'Press Key Combination', 'key1': key1, 'key2' : key2}
                additionalContent = ('First key: ' + key1 + ' Second Key: ' + key2)
            if funcIndex == '7':
                filepath = files[0]
                accuracy = self.lineEdit_2.text()
                print(accuracy)
                if len(filepath) == 0 or len(str(accuracy)) == 0:
                    return
                orderedMethod[count] = {'type': 'Click Image', 'filepath': filepath, 'accuracy': accuracy}
                additionalContent = ('filepath: ' + filepath + ' accuracy: ' + accuracy)
            if funcIndex == '8':
                orderedMethod[count] = {'type': 'Open New Desktop'}
                additionalContent = ('')
            if funcIndex == '9':
                orderedMethod[count] = {'type': 'Close Desktop'}
                additionalContent = ('')
            if funcIndex == '10':
                orderedMethod[count] = {'type': 'Next Desktop'}
                additionalContent = ('')
            if funcIndex == '11':
                orderedMethod[count] = {'type': 'Previous Desktop'}
                additionalContent = ('')
            if funcIndex == '12':
                tab = self.tabInput.toPlainText()
                if len(tab) == 0:
                    return
                orderedMethod[count] = {'type': 'New Tab', 'tab': tab}
                additionalContent = ('tab: ' + tab)
            if funcIndex == '13':
                orderedMethod[count] = {'type': 'Close Tab'}
                additionalContent = ('')


            funcName = indexKey.get(int(funcIndex))
            self.label = QLabel(funcName + ' ' + additionalContent)
            self.LabelLayout.addWidget(self.label, count,0,1,1)
        def Check(): 
            if self.LabelLayout.count() - 1 == 0:
                print('trigger not added')
                self.stackedWidget.setCurrentIndex(0)
                return
            elif self.LabelLayout.count() - 1 >= 1:
                print('trigger added')
                self.stackedWidget.setCurrentIndex(1)
                return
        def Compile():
            #! All the code in this function is in plaintext written into a python file, you may have difficulties understanding what's written here
            #? check if 
            created = False
            for i in range(5):
                if created:
                    break
                num = i+1
                abspath = path.dirname(path.abspath(__file__))
                filepath = path.join(abspath, f'Files/Workflows/Workflow{num}.py')
                FileExists = path.isfile(filepath)
                if num==5 and FileExists:
                    Status = 'all workflows exist'
                    break
                if not FileExists:
                    Status = f'opened workflow on filepath {filepath}'
                    open(filepath, 'x')
                    created = True
                
            values = len(orderedMethod)
            writeText = open(filepath, 'w')
            writeText.write('#New start')
            writeText.write('\n' + 'import keyboard' + '\n' + 'from selenium.webdriver.common.by import By' + '\n' + 'from selenium.webdriver.support import expected_conditions as EC' + '\n' + 'import undetected_chromedriver as uc' + '\n' + 'from time import sleep as wait' + '\n' + 'import pyautogui' + '\n' + 'from os import _exit' + '\n' + 'from os.path import abspath, join' + '\n' + 'from pathlib import Path') #? All the imports are here!
            writeText.write('\n\n' + 'def response():' + '\n\t' + 'print("hotkey pressed")')

            if values > 1:
                for i in range(values-1):
                    realnum = i+1
                    #! all the functions go here
                    prevVersion = open(filepath, 'r')
                    prevText = prevVersion.read()
                    writeText.write(prevText + '\n\t')
                    if orderedMethod[realnum]['type'] == 'Open Browser':
                        #? The below code is barely readable due to the amount of lines required. \n\t means new line, new tab.
                        writeText.write('absolutepath = abspath(WORKFLOW_PATH)\n\tchromedriverPath = join(Path(absolutepath).parent.parent, "Chromedriver/chromedriver.exe")\n\t')
                        writeText.write('options2 = uc.ChromeOptions()\n\tprefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}\n\toptions2.add_experimental_option("prefs",prefs)\n\tdriver = uc.Chrome(options=options2, driver_executable_path=chromedriverPath)\n\tdriver.maximize_window()\n\t') #TODO: Make driver.maximize_window optional (might not do this), also these are the settings
                        writeText.write(f'driver.get("{orderedMethod[realnum]['url']}")') #! this is the line that opens the browser at the specified url
                    elif orderedMethod[realnum]['type'] == 'Click Button':
                        writeText.write(f'driver.find_element(By.XPATH, "{orderedMethod[realnum]['xpath']}").click()') #TODO: Try to make a tutorial especially for this 
                    elif orderedMethod[realnum]['type'] == 'Click on Screen':
                        writeText.write(f'pyautogui.click(x={str(orderedMethod[realnum]['xcoord'])}, y={str(orderedMethod[realnum]['ycoord'])})')
                    elif orderedMethod[realnum]['type'] == 'Typewrite':
                        writeText.write(f'pyautogui.typewrite("{orderedMethod[realnum]['content']}",interval=0.01)') #!Add interval later on
                    elif orderedMethod[realnum]['type'] == 'Wait':
                        writeText.write(f'wait({orderedMethod[realnum]['duration']})')
                    elif orderedMethod[realnum]['type'] == 'Press Key':
                        writeText.write(f'pyautogui.press("{orderedMethod[realnum]['key']}")')
                    elif orderedMethod[realnum]['type'] == 'Press Key Combination': 
                        writeText.write(f'with pyautogui.hold("{orderedMethod[realnum]['key1']}"): \n\t\tpyautogui.press("{orderedMethod[realnum]['key2']}")') #! untested
                    elif orderedMethod[realnum]['type'] == 'Click Image':
                        writeText.write(f'x, y = pyautogui.locateCenterOnScreen("{orderedMethod[realnum]['filepath']}", confidence={orderedMethod[realnum]['accuracy']}) \n\tpyautogui.click(x, y)') #! untested
                    elif orderedMethod[realnum]['type'] == 'Open New Desktop':
                        writeText.write('with pyautogui.hold(["win", "ctrl"]): \n\t\tpyautogui.press("d")') #! untested)
                    elif orderedMethod[realnum]['type'] == 'Close Desktop':
                        writeText.write('with pyautogui.hold(["win", "ctrl", "fn"]): \n\t\tpyautogui.press("f4")') #! untested
                    elif orderedMethod[realnum]['type'] == 'Next Desktop':
                        writeText.write('with pyautogui.hold(["win", "ctrl"]): \n\t\tpyautogui.press("right")') #! untested
                    elif orderedMethod[realnum]['type'] == 'Previous Desktop':
                        writeText.write('with pyautogui.hold(["win", "ctrl"]): \n\t\tpyautogui.press("left")') #! untested
                    elif orderedMethod[realnum]['type'] == 'New Tab':
                        writeText.write(f'with pyautogui.hold("ctrl"): \n\t\tpyautogui.press("t") \n\tpyautogui.typewrite("{orderedMethod[realnum]['tab']}", interval=0)\n\tpyautogui.press("enter")') # WOrking
                    elif orderedMethod[realnum]['type'] == 'Close Tab':
                        writeText.write('with pyautogui.hold("ctrl"): \n\t\tpyautogui.press("w") \n\t') #! untested'
                    
            #!Hotkeys come aftr because it refers to the function where all the functions are sooo
            try:
                if orderedMethod[0]['type'] == 'Hotkey':
                    print('HOTKEY')
                    hotkey = orderedMethod[0]['hotkey']
                    writeText.write(f'\n\nkeyboard.add_hotkey("{hotkey}", response, suppress=True, trigger_on_release=True, timeout=1) ') #TODO: Make trigger on release an option  
                    writeText.write('\nkeyboard.wait("esc")\n_exit(0)')
                    #! My genius idae: since you only have one hotkey you must do hotkey then def response and everything else goes into response !!! screw readability
                elif orderedMethod[0]['type'] == 'InstantRun':
                    print('INSTANT')
                    writeText.write('\nresponse()')
            except:
                print('The list is empty')
                
            
            #writes content (function input) into function.py
            #prevVersion = open(r'Demo2/functionCreator/function.py', 'r')
            #prevText = prevVersion.read()
            #prevVersion.close()
        
        self.CompileButton.clicked.connect(Compile)
        self.pushButton_2.clicked.connect(AddFunction)
        self.pushButton.clicked.connect(AddTrigger)
        self.pushButton.clicked.connect(Check)
        self.pushButton_2.clicked.connect(Check)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700;\">Workflow Creator</span></p></body></html>", None))
        self.compileResult.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Item List</span></p></body></html>", None))
        self.CompileButton.setText(QCoreApplication.translate("MainWindow", u"Compile Code", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trigger Selected:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Trigger", None))
        self.triggerDropDown.setItemText(0, QCoreApplication.translate("MainWindow", u"Instantly run", None))
        self.triggerDropDown.setItemText(1, QCoreApplication.translate("MainWindow", u"Hotkey", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">This trigger has no settings.</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Simply press the &quot;Add Trigger&quot; button to add it to your Workflow!</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hotkey", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The button you want to press to start the workflow (put it here)", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Create Trigger</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Function", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Function Selected:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Create Function</span></p></body></html>", None))
        self.functionDropDown.setItemText(0, QCoreApplication.translate("MainWindow", u"Open Browser ", None))
        self.functionDropDown.setItemText(1, QCoreApplication.translate("MainWindow", u"Click Button(Browser)", None))
        self.functionDropDown.setItemText(2, QCoreApplication.translate("MainWindow", u"Click On Screen", None))
        self.functionDropDown.setItemText(3, QCoreApplication.translate("MainWindow", u"Type", None))
        self.functionDropDown.setItemText(4, QCoreApplication.translate("MainWindow", u"Wait", None))
        self.functionDropDown.setItemText(5, QCoreApplication.translate("MainWindow", u"Keypress", None))
        self.functionDropDown.setItemText(6, QCoreApplication.translate("MainWindow", u"Keypress Combination", None))
        self.functionDropDown.setItemText(7, QCoreApplication.translate("MainWindow", u"Click on Image", None))
        self.functionDropDown.setItemText(8, QCoreApplication.translate("MainWindow", u"New Desktop", None))
        self.functionDropDown.setItemText(9, QCoreApplication.translate("MainWindow", u"Close Current Desktop", None))
        self.functionDropDown.setItemText(10, QCoreApplication.translate("MainWindow", u"Next Desktop", None))
        self.functionDropDown.setItemText(11, QCoreApplication.translate("MainWindow", u"Previous Desktop", None))
        self.functionDropDown.setItemText(12, QCoreApplication.translate("MainWindow", u"New Tab", None))
        self.functionDropDown.setItemText(13, QCoreApplication.translate("MainWindow", u"Close Current Tab", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Browser URL", None))
        self.URLInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The URL the browser will be opened to", None))
        self.xPathLabel.setText(QCoreApplication.translate("MainWindow", u"XPath:", None))
        self.xPathInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The XPath of the button you want to click on (Found in Inspect Element)", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y-Coordinate of the location you want to click on", None))
        self.xCoordInputClick.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X-Coordinate of the location you want to click on", None))
        self.yCoordLabel.setText(QCoreApplication.translate("MainWindow", u"Y-Coordinate", None))
        self.xCoordLabel.setText(QCoreApplication.translate("MainWindow", u"X-Coordinate", None))
        self.contentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Interval", None))
        self.intervalInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The interval between each key that is typed", None))
        self.contentInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The content of what is being typed", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Wait Duration", None))
        self.waitInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The amount of time to pause the workflow for (seconds)", None))
        self.keyInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The key to press", None))
        self.keyLabel.setText(QCoreApplication.translate("MainWindow", u"Key", None))
        self.keyLabel_3.setText(QCoreApplication.translate("MainWindow", u"Key One", None))
        self.keyInput_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The first key to press", None))
        self.keyLabel_4.setText(QCoreApplication.translate("MainWindow", u"Key Two", None))
        self.keyInput_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The second key to press", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"How sure the program should be (decimal between 0 and 1) that the image is the one provided", None))
        self.keyLabel_2.setText(QCoreApplication.translate("MainWindow", u"Image Filepath", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Accuracy", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">This function has no settings.</span></p></body></html>", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Simply press the &quot;Add Function&quot; button to add it to your Workflow!</span></p></body></html>", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">This function has no settings.</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Simply press the &quot;Add Function&quot; button to add it to your Workflow!</span></p></body></html>", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">This function has no settings.</span></p></body></html>", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Simply press the &quot;Add Function&quot; button to add it to your Workflow!</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">This function has no settings.</span></p></body></html>", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Simply press the &quot;Add Function&quot; button to add it to your Workflow!</span></p></body></html>", None))
        self.tabInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The URL to open the tab to", None))
        self.tabLabel.setText(QCoreApplication.translate("MainWindow", u"Tab URL", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">This function has no settings.</span></p></body></html>", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Simply press the &quot;Add Function&quot; button to add it to your Workflow!</span></p></body></html>", None))
    # retranslateUi

