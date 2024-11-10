# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test3.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test3.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon, QFont)
from PySide6.QtWidgets import (QFormLayout, QFrame, QGridLayout, QCheckBox, QTextEdit, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)
from Icons_rc import qt_resource_data
from toggle import CustomToggle
from functions import SeleniumWorker, runSeleniumWorker, TypeWorker, runTypeWorker, ClickWorker, runClickWorker

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(633, 600)
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
        self.Pages.setFrameShape(QFrame.Shape.StyledPanel)
        self.Pages.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.Pages)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Pages)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(500, 0))
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
        self.label_6 = QLabel(self.Workflows)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_8.addWidget(self.label_6, 4, 1, 1, 1)

        self.label = QLabel(self.Workflows)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)

        self.Text = QFrame(self.Workflows)
        self.Text.setObjectName(u"Text")
        self.Text.setMinimumSize(QSize(0, 30))
        self.Text.setMaximumSize(QSize(16777215, 30))
        self.Text.setStyleSheet(u"background: transparent; border: transparent;")
        self.Text.setFrameShape(QFrame.Shape.StyledPanel)
        self.Text.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.Text)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 10)
        self.TextInput = QTextEdit(self.Text)
        self.TextInput.setObjectName(u"TextInput")
        sizePolicy3.setHeightForWidth(self.TextInput.sizePolicy().hasHeightForWidth())
        self.TextInput.setSizePolicy(sizePolicy3)
        self.TextInput.setMinimumSize(QSize(0, 30))
        self.TextInput.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setPointSize(9)
        font.setStyleStrategy(QFont.PreferDefault)
        self.TextInput.setFont(font)
        self.TextInput.setAutoFillBackground(False)
        self.TextInput.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.TextInput.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout_6.addWidget(self.TextInput, 0, 1, 2, 1, Qt.AlignmentFlag.AlignVCenter)

        self.label_7 = QLabel(self.Text)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.label_7, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.Text, 2, 1, 1, 1)

        self.hotkeyClick = QPushButton(self.Workflows)
        self.hotkeyClick.setObjectName(u"hotkeyClick")

        self.gridLayout_8.addWidget(self.hotkeyClick, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_3, 8, 0, 1, 1)

        self.frame_2 = QFrame(self.Workflows)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 20))
        self.frame_2.setMaximumSize(QSize(16777215, 40))
        self.frame_2.setStyleSheet(u"border: transparent; background: transparent;")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CoordinatesLabel = QLabel(self.frame_2)
        self.CoordinatesLabel.setObjectName(u"CoordinatesLabel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.CoordinatesLabel.sizePolicy().hasHeightForWidth())
        self.CoordinatesLabel.setSizePolicy(sizePolicy4)
        self.CoordinatesLabel.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.CoordinatesLabel, 0, Qt.AlignmentFlag.AlignTop)

        self.xcoord = QTextEdit(self.frame_2)
        self.xcoord.setObjectName(u"xcoord")
        self.xcoord.setMaximumSize(QSize(16777215, 30))
        self.xcoord.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.xcoord.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.xcoord)

        self.ycoord = QTextEdit(self.frame_2)
        self.ycoord.setObjectName(u"ycoord")
        self.ycoord.setMaximumSize(QSize(16777215, 30))
        self.ycoord.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.ycoord.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.horizontalLayout.addWidget(self.ycoord, 0, Qt.AlignmentFlag.AlignTop)


        self.gridLayout_8.addWidget(self.frame_2, 6, 1, 1, 1)

        self.label_5 = QLabel(self.Workflows)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_8.addWidget(self.label_5, 4, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_8.addItem(self.verticalSpacer_4, 8, 1, 1, 1)

        self.frame = QFrame(self.Workflows)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 30))
        self.frame.setMaximumSize(QSize(16777215, 40))
        self.frame.setStyleSheet(u"border: transparent; background: transparent;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setMinimumSize(QSize(0, 30))
        self.textEdit_2.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(8)
        self.textEdit_2.setFont(font1)
        self.textEdit_2.setStyleSheet(u"border: transparent; background: transparent;")
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.textEdit_2.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.gridLayout_9.addWidget(self.textEdit_2, 0, 1, 1, 1,Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout_8.addWidget(self.frame, 3, 1, 1, 1)

        self.label_4 = QLabel(self.Workflows)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_8.addWidget(self.label_4, 0, 1, 1, 1)

        self.XYButton = QPushButton(self.Workflows)
        self.XYButton.setObjectName(u"XYButton")

        self.gridLayout_8.addWidget(self.XYButton, 5, 1, 1, 1)

        self.imgRec = QPushButton(self.Workflows)
        self.imgRec.setObjectName(u"imgRec")

        self.gridLayout_8.addWidget(self.imgRec, 5, 0, 1, 1)

        self.buttonHTML = QPushButton(self.Workflows)
        self.buttonHTML.setObjectName(u"buttonHTML")

        self.gridLayout_8.addWidget(self.buttonHTML, 1, 0, 1, 1)

        self.frame_3 = QFrame(self.Workflows)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 30))
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setStyleSheet(u"border: transparent; background: transparent;")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.HotkeyLabel = QLabel(self.frame_3)
        self.HotkeyLabel.setObjectName(u"HotkeyLabel")

        self.horizontalLayout_2.addWidget(self.HotkeyLabel)

        self.HotkeyInput = QTextEdit(self.frame_3)
        self.HotkeyInput.setObjectName(u"HotkeyInput")
        self.HotkeyInput.setMinimumSize(QSize(0, 30))
        self.HotkeyInput.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_2.addWidget(self.HotkeyInput)


        self.gridLayout_8.addWidget(self.frame_3, 7, 1, 1, 1)

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
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.TopBar.sizePolicy().hasHeightForWidth())
        self.TopBar.setSizePolicy(sizePolicy5)
        self.TopBar.setMinimumSize(QSize(50, 50))
        self.TopBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.TopBar.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.TopBar)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.TopBar)
        self.label_2.setObjectName(u"label_2")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy6)

        self.gridLayout_3.addWidget(self.label_2, 0, 2, 1, 1)

        self.MenuButton = QPushButton(self.TopBar)
        self.MenuButton.setObjectName(u"MenuButton")
        sizePolicy1.setHeightForWidth(self.MenuButton.sizePolicy().hasHeightForWidth())
        self.MenuButton.setSizePolicy(sizePolicy1)
        self.MenuButton.setMinimumSize(QSize(50, 50))
        self.MenuButton.setMaximumSize(QSize(50, 50))
        self.MenuButton.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/menu_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MenuButton.setIcon(icon4)
        self.MenuButton.setIconSize(QSize(50, 50))
        self.MenuButton.setFlat(True)

        self.gridLayout_3.addWidget(self.MenuButton, 0, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.TopBar, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


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
            savedsettings = open(r'Demo2\Script\Settings\compact-mode', 'r')
            compacttext = savedsettings.read()
            if compacttext == 'False':
                savedsettings.close()
                settingstext = open(r'Demo2\Script\Settings\compact-mode', 'w')
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
                settingstext = open(r'Demo2\Script\Settings\compact-mode', 'w')
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
        def HTMLClickEvent():
            print("MainWindow: Button clicked")
            runSeleniumWorker()
        def TypeWorkerEvent():
            hotkey=self.textEdit_2.toPlainText()
            content=self.TextInput.toPlainText()
            runTypeWorker(hotkey=hotkey, content=content)
        def ClickWorkerEvent():
            xcoord=self.xcoord.toPlainText()
            ycoord=self.ycoord.toPlainText()
            hotkey=self.HotkeyInput.toPlainText()
            runClickWorker(x=xcoord, y=ycoord, hotkey=hotkey)
        self.buttonHTML.clicked.connect(HTMLClickEvent)
        self.XYButton.clicked.connect(ClickWorkerEvent)
        self.TextInput.setText('skibdi')
        self.textEdit_2.setText(']')
        self.hotkeyClick.clicked.connect(TypeWorkerEvent)
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
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Hotkey Trigger (stop with esc)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Button Trigger", None))
        self.TextInput.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>", None))
        self.TextInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Your text here", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.hotkeyClick.setText(QCoreApplication.translate("MainWindow", u"Typing in a specified location", None))
        self.CoordinatesLabel.setText(QCoreApplication.translate("MainWindow", u"Coordinates", None))
        self.xcoord.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X-Coord", None))
        self.ycoord.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y-Coord", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"no clue :3", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Hotkey", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hotkey here", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Hotkey Trigger (stop with esc)", None))
        self.XYButton.setText(QCoreApplication.translate("MainWindow", u"Clicking in a specified location", None))
        self.imgRec.setText(QCoreApplication.translate("MainWindow", u"Clicking on a location based on image", None))
        self.buttonHTML.setText(QCoreApplication.translate("MainWindow", u"Clicking on HTML elements", None))
        self.HotkeyLabel.setText(QCoreApplication.translate("MainWindow", u"Hotkey", None))
        self.HotkeyInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Hotkey here", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"This part is an extra part of the app, if I finish and still want to keep going to improve the user experience of the app, etc. I will only need to do this after I finish all of the other parts of my app.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Compact Mode</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Page Name</span></p></body></html>", None))
        self.MenuButton.setText("")
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
        savedsettings = open(r'Demo2\Script\Settings\compact-mode', 'r')
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
    # retranslateUi

