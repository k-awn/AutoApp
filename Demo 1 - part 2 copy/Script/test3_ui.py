# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test3.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QFormLayout, QFrame, QGridLayout, QCheckBox,
    QLabel, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QWidget)
from Icons_rc import qt_resource_data
from functions import ChromeStressTest
from toggle import CustomToggle

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
        self.stackedWidget.addWidget(self.Homepage)
        self.Workflows = QWidget()
        self.Workflows.setObjectName(u"Workflows")
        self.gridLayout_8 = QGridLayout(self.Workflows)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.stackedWidget.addWidget(self.Workflows)
        self.Tools = QWidget()
        self.Tools.setObjectName(u"Tools")
        self.formLayout = QFormLayout(self.Tools)
        self.formLayout.setObjectName(u"formLayout")
        self.stackedWidget.addWidget(self.Tools)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.gridLayout_7 = QGridLayout(self.Settings)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.customToggle = CustomToggle(self.Settings)
        self.gridLayout_7.addWidget(self.customToggle, 2, 0, 1, 1, alignment=Qt.AlignmentFlag.AlignLeft)
        self.gridLayout_7.addItem(self.verticalSpacer_2, 3, 0, 1, 1)

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

        self.stackedWidget.setCurrentIndex(3)


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
        def compactMode():
            print('hi')
            state = self.customToggle.checkState()
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
            if state == Qt.CheckState.Checked:
                print('CHECKED')
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
            else:
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
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Compact Mode</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Page Name</span></p></body></html>", None))
        self.MenuButton.setText("")
    # retranslateUi
