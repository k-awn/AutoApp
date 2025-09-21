from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import (QFont, QIcon)
from PySide6.QtWidgets import (QComboBox, QGridLayout, QLabel,
    QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QFileDialog,
    QWidget, QLineEdit, QPlainTextEdit, QFrame, QMessageBox)
from os import path
from customcombo import CustomCombo
import Icons_rc

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(750, 750)
        MainWindow.setMinimumSize(QSize(750, 750))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(9, -1, -1, -1)
        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(500, 250))
        self.scrollArea.setStyleSheet(u"background-color:#302c2c;\n"
"border-radius:10px;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 732, 263))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LabelLayout = QGridLayout()
        self.LabelLayout.setObjectName(u"LabelLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LabelLayout.addItem(self.verticalSpacer_3, 999, 0, 1, 1)


        self.verticalLayout.addLayout(self.LabelLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 4, 0, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"padding:5px;")

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
        self.stackedWidget.setMaximumSize(QSize(16777215, 350))
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setStyleSheet(u"background-color:#302c2c")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_9 = QLabel(self.page_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_3.addWidget(self.label_9, 0, 0, 1, 5)

        self.triggerDropDown = QComboBox(self.page_2)
        self.triggerDropDown.addItem("")
        self.triggerDropDown.addItem("")
        self.triggerDropDown.setObjectName(u"triggerDropDown")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.triggerDropDown.sizePolicy().hasHeightForWidth())
        self.triggerDropDown.setSizePolicy(sizePolicy)

        self.gridLayout_3.addWidget(self.triggerDropDown, 1, 4, 1, 1)

        self.trigSettings = QStackedWidget(self.page_2)
        self.trigSettings.setObjectName(u"trigSettings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.trigSettings.sizePolicy().hasHeightForWidth())
        self.trigSettings.setSizePolicy(sizePolicy1)
        self.trigSettings.setMinimumSize(QSize(200, 125))
        self.trigSettings.setMaximumSize(QSize(16777215, 200))
        self.trigSettings.setStyleSheet(u"")
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

        self.verticalSpacer_16 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_16, 2, 0, 1, 1)

        self.trigSettings.addWidget(self.instantRunSettings)
        self.hotkeySettings = QWidget()
        self.hotkeySettings.setObjectName(u"hotkeySettings")
        self.hotkeySettings.setMaximumSize(QSize(16777215, 150))
        self.gridLayout_2 = QGridLayout(self.hotkeySettings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.label_5 = QLabel(self.hotkeySettings)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(self.hotkeySettings)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background:transparent; border:none;")
        self.lineEdit.setMaxLength(1)

        self.gridLayout_2.addWidget(self.lineEdit, 1, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(self.hotkeySettings)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_2.addWidget(self.lineEdit_4, 3, 2, 1, 1)

        self.comboBox = QComboBox(self.hotkeySettings)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"b")

        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 2)

        self.label_13 = QLabel(self.hotkeySettings)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.label_26 = QLabel(self.hotkeySettings)
        self.label_26.setObjectName(u"label_26")

        self.gridLayout_2.addWidget(self.label_26, 3, 0, 1, 1)

        self.label_6 = QLabel(self.hotkeySettings)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.hotkeySettings)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"background:transparent; border:none;")

        self.gridLayout_2.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        self.trigSettings.addWidget(self.hotkeySettings)

        self.gridLayout_3.addWidget(self.trigSettings, 4, 0, 1, 5)

        self.infoButtonTrig = QPushButton(self.page_2)
        self.infoButtonTrig.setObjectName(u"infoButtonTrig")
        self.infoButtonTrig.setMinimumSize(QSize(50, 50))
        self.infoButtonTrig.setMaximumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/Icons/question_mark_24dp_FFFFF0_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.infoButtonTrig.setIcon(icon)
        self.infoButtonTrig.setIconSize(QSize(50, 50))
        self.infoButtonTrig.setFlat(True)

        self.gridLayout_3.addWidget(self.infoButtonTrig, 5, 0, 1, 1)

        self.label = QLabel(self.page_2)
        self.label.setObjectName(u"label")

        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)

        self.InfoTrig = QLabel(self.page_2)
        self.InfoTrig.setObjectName(u"InfoTrig")
        self.InfoTrig.setMinimumSize(QSize(50, 0))
        font = QFont()
        font.setPointSize(11)
        self.InfoTrig.setFont(font)
        self.InfoTrig.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_3.addWidget(self.InfoTrig, 5, 1, 1, 4)

        self.pushButton = QPushButton(self.page_2)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout_3.addWidget(self.pushButton, 3, 0, 1, 5)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_10 = QGridLayout(self.page_3)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_10.addWidget(self.label_10, 0, 0, 1, 3)

        self.pushButton_2 = QPushButton(self.page_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_10.addWidget(self.pushButton_2, 3, 0, 1, 3, Qt.AlignmentFlag.AlignTop)

        self.infoButtonFunc = QPushButton(self.page_3)
        self.infoButtonFunc.setObjectName(u"infoButtonFunc")
        self.infoButtonFunc.setMinimumSize(QSize(50, 50))
        self.infoButtonFunc.setMaximumSize(QSize(50, 50))
        self.infoButtonFunc.setIcon(icon)
        self.infoButtonFunc.setIconSize(QSize(50, 50))
        self.infoButtonFunc.setFlat(True)

        self.gridLayout_10.addWidget(self.infoButtonFunc, 5, 0, 1, 1)

        self.label_4 = QLabel(self.page_3)
        self.label_4.setObjectName(u"label_4")
        

        self.gridLayout_10.addWidget(self.label_4, 2, 0, 1, 1)

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

        self.gridLayout_5.addWidget(self.label_7, 1, 0, 1, 1, Qt.AlignmentFlag.AlignVCenter)

        self.URLInput = QPlainTextEdit(self.openBrowserSettings)
        self.URLInput.setObjectName(u"URLInput")
        self.URLInput.setMaximumSize(QSize(16777215, 25))
        self.URLInput.setStyleSheet(u"background:transparent;  border:none;")
        self.URLInput.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.URLInput.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.URLInput.setMaximumBlockCount(1)

        self.gridLayout_5.addWidget(self.URLInput, 1, 2, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_8, 2, 2, 1, 1)

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
        self.keyLabel_4 = QLabel(self.keypressCombinationSettings)
        self.keyLabel_4.setObjectName(u"keyLabel_4")

        self.gridLayout_15.addWidget(self.keyLabel_4, 1, 0, 1, 1)

        self.keyLabel_3 = QLabel(self.keypressCombinationSettings)
        self.keyLabel_3.setObjectName(u"keyLabel_3")

        self.gridLayout_15.addWidget(self.keyLabel_3, 0, 0, 1, 1)

        self.keyInput_3 = QLineEdit(self.keypressCombinationSettings)
        self.keyInput_3.setObjectName(u"keyInput_3")
        self.keyInput_3.setStyleSheet(u"background:transparent; border:none;")
        self.keyInput_3.setMaxLength(15)

        self.gridLayout_15.addWidget(self.keyInput_3, 1, 1, 1, 1)

        self.keyInput_2 = QLineEdit(self.keypressCombinationSettings)
        self.keyInput_2.setObjectName(u"keyInput_2")
        self.keyInput_2.setStyleSheet(u"background:transparent; border:none;")
        self.keyInput_2.setMaxLength(15)

        self.gridLayout_15.addWidget(self.keyInput_2, 0, 1, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_15.addItem(self.verticalSpacer_15, 2, 0, 1, 2)

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

        self.gridLayout_10.addWidget(self.funcSettings, 4, 0, 1, 3)

        self.infoFunc = QLabel(self.page_3)
        self.infoFunc.setObjectName(u"infoFunc")
        self.infoFunc.setFont(font)
        self.infoFunc.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_10.addWidget(self.infoFunc, 5, 1, 1, 2)

        self.stackedWidget.addWidget(self.page_3)

        self.gridLayout.addWidget(self.stackedWidget, 2, 0, 1, 2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(20, 25))
        self.frame.setMaximumSize(QSize(16777215, 25))
        self.frame.setStyleSheet(u"QFrame { background-color: transparent; border: none; }")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_20 = QGridLayout(self.frame)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_20.setHorizontalSpacing(0)
        self.gridLayout_20.setContentsMargins(0, 0, 0, 0)
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(250, 25))
        font1 = QFont()
        font1.setPointSize(9)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setStyleSheet(u"            QPushButton {\n"
"                background-color: #302c2c;\n"
"                border: none;\n"
"                border-top-left-radius: 0px;\n"
"                border-top-right-radius: 10px;\n"
"                border-bottom-left-radius: 0px;\n"
"                border-bottom-right-radius: 0px;\n"
"                margin: 0px;				\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #908c8c;\n"
"            }\n"
"			QPushButton:pressed {\n"
"				background-color:#302c2c\n"
"}")

        self.gridLayout_20.addWidget(self.pushButton_4, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setMinimumSize(QSize(250, 25))
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"            QPushButton {\n"
"                background-color: #302c2c;\n"
"                color: white;\n"
"                border: none;\n"
"                border-top-left-radius: 10px;\n"
"                border-top-right-radius: 0px;\n"
"                border-bottom-left-radius: 0px;\n"
"                border-bottom-right-radius: 0px;\n"
"                margin: 0px;\n"
"                padding: 5px;\n"
"            }\n"
"            QPushButton:hover {\n"
"                background-color: #908c8c;\n"
"            }\n"
"			QPushButton:pressed {\n"
"				background-color:#302c2c\n"
"}")
        self.pushButton_3.setFlat(False)

        self.gridLayout_20.addWidget(self.pushButton_3, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.frame, 1, 0, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"padding:5px;")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.CompileButton = QPushButton(self.centralwidget)
        self.CompileButton.setObjectName(u"CompileButton")
        self.CompileButton.setMinimumSize(QSize(0, 40))
        self.CompileButton.setMaximumSize(QSize(16777215, 50))
        self.CompileButton.setStyleSheet(u"padding:15px;")

        self.gridLayout.addWidget(self.CompileButton, 6, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.trigSettings.setCurrentIndex(0)
        self.funcSettings.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
        data = [
            ("Browser", [
                "Open Browser",
                "Click Button",
                ("Tabs", [
                    "New Tab",
                    "Close Tab",
                ])
            ]),
            ("Keyboard", [
                "Type",
                ("Pressing Keys", [
                    "Press Key",
                    "Press Key Combination",
                ]),
            ]),
            ("Desktops", [
                "New Desktop",
                "Close Desktop",
                "Next Desktop",
                "Previous Desktop",
            ]),
            ("Clicking", [
                "Click",
                "Click Image",
                "Click Button",  
            ]),
            "Pause/Wait",

        ]

        
        custom_indices = {
            "Open Browser": 0,
            "Click Button": 1,
            "Click": 2,
            "Type": 3,
            "Pause/Wait": 4,
            "Press Key": 5, 
            "Press Key Combination": 6,
            "Click Image": 7,
            "New Desktop": 8,
            "Close Desktop": 9, 
            "Next Desktop": 10,
            "Previous Desktop": 11,
            "New Tab": 12,
            "Close Tab": 13, 
    }
        self.functionDropDown = CustomCombo(data,custom_indices)
        self.functionDropDown.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.gridLayout_10.addWidget(self.functionDropDown, 2, 2, 1, 1)
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_4.hide()
        self.lineEdit_3.hide()
        self.label_6.hide()
        self.label_26.hide()
        def changeComboVis():
            print('detecting!')
            if self.comboBox.currentIndex() == 0:
                print('index 0')
                self.label_5.show()
                self.label_6.hide()
                self.label_26.hide()

                self.lineEdit.show()
                self.lineEdit_3.hide()
                self.lineEdit_4.hide()
                self.lineEdit_3.setText('')
                self.lineEdit_4.setText('')
            elif self.comboBox.currentIndex() == 1:
                print('index 1')
                self.label_5.show()
                self.label_6.show()
                self.label_26.hide()
                
                self.lineEdit.show()
                self.lineEdit_3.show()
                self.lineEdit_4.hide()
                self.lineEdit_4.setText('')
            elif self.comboBox.currentIndex() == 2:
                print('index 2')
                self.label_5.show()
                self.label_6.show()
                self.label_26.show()


                self.lineEdit.show()
                self.lineEdit_3.show()
                self.lineEdit_4.show()
        self.comboBox.currentIndexChanged.connect(changeComboVis)
        self.button = QPushButton('Choose File')
        def openFile():
            dialog = QFileDialog()
            dialog.setNameFilter('Images (*.png *.jpg *.jpeg)')
            dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
            
            dialogSuccessful = dialog.exec()
            if dialogSuccessful == 1:
                global files
                files = dialog.selectedFiles()
                self.button.setText('File Selected, Click again to re-select')                
            else:
                print('dialog canceled')
                return
        self.button.clicked.connect(openFile)
        self.gridLayout_12.addWidget(self.button, 0, 1, 1, 1)
        orderedMethod = {}
        def syncFunc():
            dropIndex = self.functionDropDown.currentIndex()
            self.funcSettings.setCurrentIndex(dropIndex)
        self.functionDropDown.on_action_triggered.connect(syncFunc)
        def syncTrig():
            dropIndex = self.triggerDropDown.currentIndex()
            self.trigSettings.setCurrentIndex(dropIndex)
        self.functionDropDown.on_action_triggered.connect(syncFunc)
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
                additionalContent = 'error (pls email me)'
                if self.comboBox.currentIndex() == 0:
                    hotkey = self.lineEdit.text()
                    if len(hotkey) == 0:
                        return
                    orderedMethod[count] = {'type': 'Hotkey', 'hotkey': hotkey}
                    additionalContent = ('that activates the workflow when pressing ' + hotkey)
                if self.comboBox.currentIndex() == 1:
                    hotkey = self.lineEdit.text()
                    hotkey2 = self.lineEdit_3.text()
                    if len(hotkey) == 0 or len(hotkey2) == 0:
                        return
                    orderedMethod[count] = {'type': 'Hotkey', 'hotkey': hotkey, 'hotkey2': hotkey2}
                    additionalContent = ('that activates the workflow when pressing ' + hotkey + ' and ' + hotkey2)
                if self.comboBox.currentIndex() == 2:
                    hotkey = self.lineEdit.text()
                    hotkey2 = self.lineEdit_3.text()
                    hotkey3 = self.lineEdit_4.text()
                    if len(hotkey) == 0 or len(hotkey2) == 0 or len(hotkey3) == 0:
                        return
                    orderedMethod[count] = {'type': 'Hotkey', 'hotkey': hotkey, 'hotkey2': hotkey2, 'hotkey3': hotkey3 }
                    additionalContent = ('that activates the workflow when pressing ' + hotkey + ', ' + hotkey2 + ' and ' + hotkey3)
            self.triggerLabel = QLabel(trigName + ' ' + additionalContent)
            self.triggerLabel.setObjectName(u"step" + str(count))
            self.triggerLabel.setWordWrap(True)
            self.triggerLabel.setStyleSheet('font-size: 15pt')
            self.LabelLayout.addWidget(self.triggerLabel, count, 0, 1, 1)
            print(orderedMethod)
        def placeHolderTrig():
            count = self.LabelLayout.count() - 1
            if count == 0:
                orderedMethod[count] = {'type': 'InstantRun'}
                self.triggerLabel = QLabel('Instant Run')
                self.triggerLabel.setWordWrap(True)
                self.triggerLabel.setStyleSheet('font-size: 15pt')
                self.LabelLayout.addWidget(self.triggerLabel, count, 0, 1, 1)

        self.deleteButtons = {}
            
        def AddFunction():
            funcIndex = str(self.functionDropDown.currentIndex()) # current index of the function dropdown
            count = self.LabelLayout.count() - 1

            #! FuncIndex = 0
            indexKey = {
                0 : 'Open Browser', #Working
                1 : 'Click Button', #Working
                2 : 'Click', #Working
                3 : 'Type', #Working
                4 : 'Wait', #Working
                5 : 'Press Key', #working
                6 : 'Press Key Combination', #working
                7 : 'Click Image', #working
                8 : 'New Desktop', #working
                9 : 'Close Desktop', #working
                10 : 'Next Desktop', #working
                11 : 'Previous Desktop', #working
                12 : 'New Tab', #working
                13 : 'Close Tab' #working
            }
            print(count)
            from time import sleep
            sleep(0.05)
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
                additionalContent = ('with the xPath: ' + xPath)
            if funcIndex == '2':
                xCoord = self.xCoordInputClick.toPlainText()
                yCoord = self.plainTextEdit.toPlainText()
                if len(xCoord) == 0 or len(yCoord) == 0:
                    return
                orderedMethod[count] = {'type':'Click', 'xcoord': xCoord, 'ycoord': yCoord}
                additionalContent = ('at (' + xCoord + ', ' + yCoord + ')')
            if funcIndex == '3':
                content = self.contentInput.toPlainText()
                interval = self.intervalInput.toPlainText()
                if len(content) == 0:
                    return
                orderedMethod[count] = {'type': 'Type', 'content': content, 'interval': interval}
                additionalContent = (content + ' with an interval of ' + interval + ' seconds per letter.')
            if funcIndex == '4':
                duration = self.waitInput.toPlainText()
                if len(duration) == 0:
                    return
                orderedMethod[count] = {'type': 'Wait', 'duration': duration}
                additionalContent = ('for ' + duration + ' seconds')
            if funcIndex == '5':
                key = self.keyInput.text()
                if len(key) == 0:
                    return
                orderedMethod[count] = {'type': 'Press Key', 'key': key}
                additionalContent = (key)
            if funcIndex == '6':
                key1 = self.keyInput_2.text()
                key2 = self.keyInput_3.text()
                if len(key1) == 0 or len(key2) == 0:
                    return
                orderedMethod[count] = {'type': 'Press Key Combination', 'key1': key1, 'key2' : key2}
                additionalContent = ('First key: ' + key1 + ' Second Key: ' + key2)
            if funcIndex == '7':
                try:
                    filepath = files[0]
                    accuracy = (int(self.lineEdit_2.text()) / 100)
                except:
                    return
                if len(filepath) == 0 or len(str(accuracy)) == 0:
                    return
                orderedMethod[count] = {'type': 'Click Image', 'filepath': filepath, 'accuracy': accuracy}
                additionalContent = ('when the computer is ' + (str(accuracy*100)) + '%' + ' sure')
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
            self.functionLabel = QLabel(funcName + ' ' + additionalContent)
            self.functionLabel.setWordWrap(True)
            self.functionLabel.setStyleSheet('font-size: 12pt')
            self.LabelLayout.addWidget(self.functionLabel, count,0,1,1)
            self.deleteButtons[count] = QPushButton('Delete')
            
            self.deleteButtons[count].clicked.connect(lambda checked, key=count: orderedMethod.pop(key, None))
            self.deleteButtons[count].clicked.connect(lambda checked, row=count: [self.LabelLayout.itemAtPosition(row, col).widget().deleteLater() for col in range(2) if self.LabelLayout.itemAtPosition(row, col)])
            self.deleteButtons[count].setStyleSheet("""
                QPushButton {
                    background-color: #292626;
                    color: #696464;
                    border: none;
                    border-top-left-radius: 10px;
                    border-top-right-radius: 10px;
                    border-bottom-left-radius: 10px;
                    border-bottom-right-radius: 10px;
                    margin: 0px;
                    padding: 5px;
                    max-width: 100px;
                    font: bold
                }
                QPushButton:hover {
                    background-color: #908c8c;
                    color: red
                                                    
                }
                QPushButton:pressed {
                    background-color: #302c2c;
                }
            """)
            self.LabelLayout.addWidget(self.deleteButtons[count], count, 1, 1, 1)
        
        
        def Check(): 
            
            if self.LabelLayout.count() - 1 == 0:
                print('trigger not added')
                self.stackedWidget.setCurrentIndex(0)
                return
            elif self.LabelLayout.count() - 1 >= 1:
                print('trigger added')
                self.stackedWidget.setCurrentIndex(1)
                self.pushButton_3.setDisabled(True)
                self.pushButton_3.setStyleSheet(u"            QPushButton {\n"
        "                background-color: #292626;\n"
        "                color: #696464;\n"
        "                border: none;\n"
        "                border-top-left-radius: 10px;\n"
        "                border-top-right-radius: 0px;\n"
        "                border-bottom-left-radius: 0px;\n"
        "                border-bottom-right-radius: 0px;\n"
        "                margin: 0px;\n"
        "                padding: 5px;\n"
        "            }\n"
        "            QPushButton:hover {\n"
        "                background-color: #908c8c;\n"
        "            }\n"
        "			QPushButton:pressed {\n"
        "				background-color:#302c2c\n"
        "}")
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
                    msg = QMessageBox()
                    msg.setWindowTitle('Warning - Maximum Workflows')
                    msg.setText('Maximum amount of workflows has been reached (5). Please delete a workflow using the red trash icon to continue.')
                    ok = QPushButton('OK')
                    msg.addButton(ok, QMessageBox.YesRole)
                    msg.setFixedSize(500, 300)
                    msg.setMinimumSize(500, 300)
                    msg.setMaximumSize(500, 300)
                    msg.exec()

                    break
                if not FileExists:
                    Status = f'opened workflow on filepath {filepath}'
                    open(filepath, 'x')
                    created = True
                
            values = len(orderedMethod)
            writeText = open(filepath, 'w')
            writeText.write('#New start')
            writeText.write('\n' + 'import keyboard' + '\n' + 'from selenium.webdriver.common.by import By' + '\n' + 'from selenium.webdriver.support import expected_conditions as EC' + '\n' + 'import undetected_chromedriver as uc' + '\n' + 'from time import sleep as wait' + '\n' + 'import pyautogui' + '\n' + 'from os import _exit, path' + '\n' + 'from os.path import abspath, join') #? All the imports are here!
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
                        writeText.write('absolutepath = abspath(WORKFLOW_PATH)\n\tparent_dir = path.dirname(absolutepath)\n\tgrand_parent_dir = path.dirname(parent_dir)\n\tchromedriverPath = join(grand_parent_dir, "Chromedriver/chromedriver.exe")\n\t')
                        writeText.write('options2 = uc.ChromeOptions()\n\tprefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}\n\toptions2.add_experimental_option("prefs",prefs)\n\tdriver = uc.Chrome(options=options2, driver_executable_path=chromedriverPath)\n\tdriver.maximize_window()\n\t') #TODO: Make driver.maximize_window optional (might not do this), also these are the settings
                        writeText.write(f'driver.get("{orderedMethod[realnum]['url']}")') #! this is the line that opens the browser at the specified url
                    elif orderedMethod[realnum]['type'] == 'Click Button':
                        writeText.write(f'driver.find_element(By.XPATH, "{(orderedMethod[realnum]['xpath'])}").click()') #TODO: Try to make a tutorial especially for this 
                    elif orderedMethod[realnum]['type'] == 'Click':
                        writeText.write(f'pyautogui.click(x={str(orderedMethod[realnum]['xcoord'])}, y={str(orderedMethod[realnum]['ycoord'])})')
                    elif orderedMethod[realnum]['type'] == 'Type':
                        writeText.write(f'pyautogui.typewrite("{orderedMethod[realnum]['content']}",interval={orderedMethod[realnum]['interval']})') #!Add interval later on
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
                    if self.comboBox.currentIndex() == 0:
                        hotkey = orderedMethod[0]['hotkey']
                        writeText.write(f'\n\nkeyboard.add_hotkey("{hotkey}", response, suppress=True, trigger_on_release=True, timeout=1) ') #TODO: Make trigger on release an option  
                        writeText.write('\nkeyboard.wait("esc")\n_exit(0)')
                    elif self.comboBox.currentIndex() == 1:
                        hotkey = orderedMethod[0]['hotkey']
                        hotkey2 = orderedMethod[0]['hotkey2']
                        writeText.write(f'\n\nkeyboard.add_hotkey("{hotkey} + {hotkey2}", response, suppress=True, trigger_on_release=True, timeout=1) ')
                        writeText.write('\nkeyboard.wait("esc")\n_exit(0)')
                    if self.comboBox.currentIndex() == 2:
                        hotkey = orderedMethod[0]['hotkey']
                        hotkey2 = orderedMethod[0]['hotkey2']
                        hotkey3 = orderedMethod[0]['hotkey3']
                        writeText.write(f'\n\nkeyboard.add_hotkey("{hotkey} + {hotkey2} + {hotkey3}", response, suppress=True, trigger_on_release=True, timeout=1) ')
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
        self.pushButton_2.clicked.connect(placeHolderTrig)
        self.pushButton_2.clicked.connect(AddFunction)
        self.pushButton.clicked.connect(AddTrigger)
        self.pushButton.clicked.connect(Check)
        self.pushButton_2.clicked.connect(Check)
        self.label_2.setStyleSheet('padding: 10px')
        # change the menu button thingy that switches from trigger to function's index
        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        def updateInfo():
            self.functionDropDown.show()
            print('E')
            #!triggertext
            if self.triggerDropDown.currentIndex() == 0:
                self.InfoTrig.setText('This trigger will cause the workflow to run as soon as the green button is pressed.')
            elif self.triggerDropDown.currentIndex() == 1: 
                self.InfoTrig.setText('This trigger will cause the workflow to run when a key or combination of keys is pressed. \nTo make pressing the key(s) start the workflow, press the green button. \nTo stop pressing the key(s) from starting the workflow, press esc (or restart your computer).')
            #!functiontext
            if self.functionDropDown.currentIndex() == 0:
                self.infoFunc.setText('This function will cause a Google Chrome browser to be opened to the URL (Link) given by the user. This is recommended to be used before some other functions, such as "New Tab", "Close Current Tab", "Click Button" etc.')
            elif self.functionDropDown.currentIndex() == 1:
                self.infoFunc.setText('This function will cause a button to be clicked at the given XPATH.\n To find the XPATH, right click on the button you want to have clicked, press Inspect, right click on the highlighted area to the right and select "Copy full XPATH" (not Copy XPATH).\nIf you cannot use this function, a screenshot of the button and the function "Click Image" will provide a similar result.')
            elif self.functionDropDown.currentIndex() == 2:
                self.infoFunc.setText('This function will click at the provided X and Y Coordinates (vertical and horizontal position) on the screen. To find this position, you can use the tool "X-Y Coordinates Finder" in the Tools section.')
            elif self.functionDropDown.currentIndex() == 3:
                self.infoFunc.setText('This function will type the provided text with a pause (in seconds) specified by the user.')
            elif self.functionDropDown.currentIndex() == 4:
                self.infoFunc.setText('This function will pause the workflow for the period of time (in seconds) given by the user. ')
            elif self.functionDropDown.currentIndex() == 5:
                self.infoFunc.setText('This function will press any key on your computer. Simply spell the key out as it is labeled on your keyboard. \nFor example, the control button is ctrl, and the escape button is esc.')
            elif self.functionDropDown.currentIndex() == 6:
                self.infoFunc.setText('This function will press any combination of keys on your computer. Simply spell each key out as it is labeled on your keyboard. \nFor example, the control button is ctrl, and the escape button is esc. ')
            elif self.functionDropDown.currentIndex() == 7:
                self.infoFunc.setText('This function will click on an image on the screen that resembles the image provided by the user, when the computer is sure to a certain percentage that the images match. If the percentage is too low, the computer might think that the image provided is the same as the image on the screen even if the user does not want the computer to click on it.')
            elif self.functionDropDown.currentIndex() == 8:
                self.infoFunc.setText('This function will open a new desktop on your computer. To see all of your desktops and manage them yourself, press Windows + Tab.')
            elif self.functionDropDown.currentIndex() == 9:
                self.infoFunc.setText('This function only activates when there are 2 or more desktops.\nThis function will close the currently opened desktop on your computer. To see all of your desktops and manage them yourself, press Windows + Tab.')
            elif self.functionDropDown.currentIndex() == 10:
                self.infoFunc.setText('This function only activates when there are 2 or more desktops.\nThis function will switch your computer to the next desktop. For example, Desktop 1 will switch to whatever desktop is to the right of it when the function is activated. To see the order of desktops and rearrange them manually, press Windows + Tab.')
            elif self.functionDropDown.currentIndex() == 11:
                self.infoFunc.setText('This function only activates when there are 2 or more desktops.\nThis function will switch your computer to the previous desktop. For example, Desktop 2 will switch to whatever desktop is to the left of it when the function is activated. To see the order of desktops and rearrange them manually, press Windows + Tab.')
            elif self.functionDropDown.currentIndex() == 12:
                self.infoFunc.setText('This function only activates when any browser engine is on-screen.\n This function will open a new tab at the URL (Link) given by the user.')
            elif self.functionDropDown.currentIndex() == 13:
                self.infoFunc.setText('This function only activates when any browser engine is on-screen.\n This function will close the current tab.')
        updateInfo()
        def updateVis():
            if self.infoFunc.isHidden():
                self.infoFunc.show()
            elif self.infoFunc.isVisible():
                self.infoFunc.hide()
            if self.InfoTrig.isHidden(): #you might notice different spelling styles, this is because I made a typo 
                self.InfoTrig.show()
            elif self.InfoTrig.isVisible():
                self.InfoTrig.hide()
        self.infoButtonFunc.clicked.connect(updateVis)
        self.InfoTrig.setWordWrap(True)
        self.infoFunc.setWordWrap(True)
        self.InfoTrig.setText('This trigger will cause the workflow to run as soon as the green button is pressed.')
        self.infoFunc.setText('This function will cause a Google Chrome browser to be opened to the URL (Link) given by the user. This is recommended to be used before some other functions, such as "New Tab", "Close Current Tab", "Click Button" etc.')
        self.infoButtonTrig.clicked.connect(updateVis)
        self.triggerDropDown.currentIndexChanged.connect(updateInfo)
        self.functionDropDown.on_action_triggered.connect(updateInfo)
        self.triggerDropDown.setCurrentIndex(0)
        self.functionDropDown.setCurrentIndex(0)


        

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Workflow Steps</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Create Trigger</span></p></body></html>", None))
        self.triggerDropDown.setItemText(0, QCoreApplication.translate("MainWindow", u"Instantly run", None))
        self.triggerDropDown.setItemText(1, QCoreApplication.translate("MainWindow", u"Hotkey", None))

        self.label_24.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">This trigger has no settings.</span></p></body></html>", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">Simply press the &quot;Add Trigger&quot; button to add it to your Workflow!</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hotkey", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The button you want to press to start the workflow (put it here)", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The third hotkey to start the workflow", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"One Key", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Two Keys", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Three Keys", None))

        self.comboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Amount of keys to press to trigger the workflow", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Amount of Keys", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Third Hotkey", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Second Hotkey", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The second hotkey to start the workflow", None))
        self.infoButtonTrig.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trigger Selected:", None))
        self.InfoTrig.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Trigger", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Create Function</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Function", None))
        self.infoButtonFunc.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Function Selected:", None))
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
        self.keyLabel_4.setText(QCoreApplication.translate("MainWindow", u"Key Two", None))
        self.keyLabel_3.setText(QCoreApplication.translate("MainWindow", u"Key One", None))
        self.keyInput_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The second key in the combination", None))
        self.keyInput_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"The first key in the combination", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"How sure the program should be (integer between 1 and 100) that the image is the one provided", None))
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
        self.infoFunc.setText("")
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Functions", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Triggers", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:700;\">Workflow Creator</span></p></body></html>", None))
        self.CompileButton.setText(QCoreApplication.translate("MainWindow", u"Create Workflow", None))
        self.original_style = """
            QLineEdit, QPlainTextEdit {
                color: #999999;
                border:none;
            }
            QLineEdit::placeholder, QPlainTextEdit::placeholder {
                color: #999999;
            }
        """
        self.red_style = """
            QLineEdit, QPlainTextEdit {
                color: #ff073a;
                border:none;
            }
            QLineEdit::placeholder, QPlainTextEdit::placeholder {
                color: #ff073a;
            }
        """
        
        def on_button_pressed():
            # Get all QLineEdit widgets
            line_edits = MainWindow.findChildren(QLineEdit)
            for widget in line_edits:
                if len(widget.text()) == 0:
                    widget.setStyleSheet(self.red_style)                
            # Get all QPlainTextEdit widgets
            text_edits = MainWindow.findChildren(QPlainTextEdit)
            for widget in text_edits:
                if len(widget.toPlainText()) == 0:
                    widget.setStyleSheet(self.red_style)
        def on_button_released():
            # Get all QLineEdit widgets
            line_edits = MainWindow.findChildren(QLineEdit)
            for widget in line_edits:
                widget.setStyleSheet(self.original_style)
                
            # Get all QPlainTextEdit widgets
            text_edits = MainWindow.findChildren(QPlainTextEdit)
            for widget in text_edits:
                widget.setStyleSheet(self.original_style)

        self.pushButton.pressed.connect(on_button_pressed)
        self.pushButton.released.connect(on_button_released)
        self.pushButton_2.pressed.connect(on_button_pressed)
        self.pushButton_2.released.connect(on_button_released)

        