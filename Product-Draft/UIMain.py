# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test3rcHmBy.ui'
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
import json
from os import path

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(774, 558)
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
        self.formLayout_2 = QFormLayout(self.Pages)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
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
        self.label_6 = QLabel(self.Homepage)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_6, 3, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_5, 4, 0, 1, 1)

        self.label_5 = QLabel(self.Homepage)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_11 = QLabel(self.Homepage)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_5.addWidget(self.label_11, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.label_12 = QLabel(self.Homepage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 50))
        self.label_12.setWordWrap(True)

        self.gridLayout_5.addWidget(self.label_12, 1, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 423))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

        self.Workflow5 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow5.setObjectName(u"Workflow5")
        self.Workflow5.setMinimumSize(QSize(0, 75))
        self.Workflow5.setMaximumSize(QSize(16777215, 75))
        self.Workflow5.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow5.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.Workflow5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.RenameWorkflow5 = QPushButton(self.Workflow5)
        self.RenameWorkflow5.setObjectName(u"RenameWorkflow5")
        self.RenameWorkflow5.setMinimumSize(QSize(30, 30))
        self.RenameWorkflow5.setMaximumSize(QSize(30, 30))
        icon4 = QIcon()
        icon4.addFile(u":/Icons/editName_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RenameWorkflow5.setIcon(icon4)
        self.RenameWorkflow5.setIconSize(QSize(20, 20))
        self.RenameWorkflow5.setFlat(True)

        self.horizontalLayout_4.addWidget(self.RenameWorkflow5)

        self.Workflow5Name = QLabel(self.Workflow5)
        self.Workflow5Name.setObjectName(u"Workflow5Name")

        self.horizontalLayout_4.addWidget(self.Workflow5Name)

        self.horizontalSpacer_15 = QSpacerItem(309, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_15)

        self.StartWorkflow5 = QPushButton(self.Workflow5)
        self.StartWorkflow5.setObjectName(u"StartWorkflow5")
        sizePolicy1.setHeightForWidth(self.StartWorkflow5.sizePolicy().hasHeightForWidth())
        self.StartWorkflow5.setSizePolicy(sizePolicy1)
        self.StartWorkflow5.setMinimumSize(QSize(40, 40))
        self.StartWorkflow5.setMaximumSize(QSize(40, 40))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/start_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StartWorkflow5.setIcon(icon5)
        self.StartWorkflow5.setIconSize(QSize(40, 40))
        self.StartWorkflow5.setFlat(True)

        self.horizontalLayout_4.addWidget(self.StartWorkflow5)

        self.DeleteWorkflow5 = QPushButton(self.Workflow5)
        self.DeleteWorkflow5.setObjectName(u"DeleteWorkflow5")
        sizePolicy1.setHeightForWidth(self.DeleteWorkflow5.sizePolicy().hasHeightForWidth())
        self.DeleteWorkflow5.setSizePolicy(sizePolicy1)
        self.DeleteWorkflow5.setMinimumSize(QSize(40, 40))
        self.DeleteWorkflow5.setMaximumSize(QSize(40, 40))
        icon6 = QIcon()
        icon6.addFile(u":/Icons/delete_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DeleteWorkflow5.setIcon(icon6)
        self.DeleteWorkflow5.setIconSize(QSize(40, 40))
        self.DeleteWorkflow5.setFlat(True)

        self.horizontalLayout_4.addWidget(self.DeleteWorkflow5)


        self.gridLayout_6.addWidget(self.Workflow5, 4, 0, 1, 1)

        self.Workflow4 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow4.setObjectName(u"Workflow4")
        self.Workflow4.setMinimumSize(QSize(0, 75))
        self.Workflow4.setMaximumSize(QSize(16777215, 75))
        self.Workflow4.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow4.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow4.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.Workflow4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.RenameWorkflow4 = QPushButton(self.Workflow4)
        self.RenameWorkflow4.setObjectName(u"RenameWorkflow4")
        self.RenameWorkflow4.setMinimumSize(QSize(30, 30))
        self.RenameWorkflow4.setMaximumSize(QSize(30, 30))
        self.RenameWorkflow4.setIcon(icon4)
        self.RenameWorkflow4.setIconSize(QSize(20, 20))
        self.RenameWorkflow4.setFlat(True)

        self.horizontalLayout.addWidget(self.RenameWorkflow4)

        self.Workflow4Name = QLabel(self.Workflow4)
        self.Workflow4Name.setObjectName(u"Workflow4Name")

        self.horizontalLayout.addWidget(self.Workflow4Name)

        self.horizontalSpacer_14 = QSpacerItem(309, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_14)

        self.StartWorkflow4 = QPushButton(self.Workflow4)
        self.StartWorkflow4.setObjectName(u"StartWorkflow4")
        sizePolicy1.setHeightForWidth(self.StartWorkflow4.sizePolicy().hasHeightForWidth())
        self.StartWorkflow4.setSizePolicy(sizePolicy1)
        self.StartWorkflow4.setMinimumSize(QSize(40, 40))
        self.StartWorkflow4.setMaximumSize(QSize(40, 40))
        self.StartWorkflow4.setIcon(icon5)
        self.StartWorkflow4.setIconSize(QSize(40, 40))
        self.StartWorkflow4.setFlat(True)

        self.horizontalLayout.addWidget(self.StartWorkflow4)

        self.DeleteWorkflow4 = QPushButton(self.Workflow4)
        self.DeleteWorkflow4.setObjectName(u"DeleteWorkflow4")
        sizePolicy1.setHeightForWidth(self.DeleteWorkflow4.sizePolicy().hasHeightForWidth())
        self.DeleteWorkflow4.setSizePolicy(sizePolicy1)
        self.DeleteWorkflow4.setMinimumSize(QSize(40, 40))
        self.DeleteWorkflow4.setMaximumSize(QSize(40, 40))
        self.DeleteWorkflow4.setIcon(icon6)
        self.DeleteWorkflow4.setIconSize(QSize(40, 40))
        self.DeleteWorkflow4.setFlat(True)

        self.horizontalLayout.addWidget(self.DeleteWorkflow4)


        self.gridLayout_6.addWidget(self.Workflow4, 3, 0, 1, 1)

        self.Workflow1 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow1.setObjectName(u"Workflow1")
        self.Workflow1.setMinimumSize(QSize(0, 75))
        self.Workflow1.setMaximumSize(QSize(16777215, 75))
        self.Workflow1.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow1.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.Workflow1)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.horizontalSpacer_8 = QSpacerItem(379, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_14.addItem(self.horizontalSpacer_8, 0, 2, 1, 1)

        self.Workflow1Name = QLabel(self.Workflow1)
        self.Workflow1Name.setObjectName(u"Workflow1Name")

        self.gridLayout_14.addWidget(self.Workflow1Name, 0, 1, 1, 1)

        self.RenameWorkflow1 = QPushButton(self.Workflow1)
        self.RenameWorkflow1.setObjectName(u"RenameWorkflow1")
        self.RenameWorkflow1.setMinimumSize(QSize(30, 30))
        self.RenameWorkflow1.setMaximumSize(QSize(30, 30))
        self.RenameWorkflow1.setIcon(icon4)
        self.RenameWorkflow1.setIconSize(QSize(20, 20))
        self.RenameWorkflow1.setFlat(True)

        self.gridLayout_14.addWidget(self.RenameWorkflow1, 0, 0, 1, 1)

        self.DeleteWorkflow1 = QPushButton(self.Workflow1)
        self.DeleteWorkflow1.setObjectName(u"DeleteWorkflow1")
        sizePolicy1.setHeightForWidth(self.DeleteWorkflow1.sizePolicy().hasHeightForWidth())
        self.DeleteWorkflow1.setSizePolicy(sizePolicy1)
        self.DeleteWorkflow1.setMinimumSize(QSize(40, 40))
        self.DeleteWorkflow1.setMaximumSize(QSize(40, 40))
        self.DeleteWorkflow1.setIcon(icon6)
        self.DeleteWorkflow1.setIconSize(QSize(40, 40))
        self.DeleteWorkflow1.setFlat(True)

        self.gridLayout_14.addWidget(self.DeleteWorkflow1, 0, 4, 1, 1)

        self.StartWorkflow1 = QPushButton(self.Workflow1)
        self.StartWorkflow1.setObjectName(u"StartWorkflow1")
        sizePolicy1.setHeightForWidth(self.StartWorkflow1.sizePolicy().hasHeightForWidth())
        self.StartWorkflow1.setSizePolicy(sizePolicy1)
        self.StartWorkflow1.setMinimumSize(QSize(40, 40))
        self.StartWorkflow1.setMaximumSize(QSize(40, 40))
        self.StartWorkflow1.setIcon(icon5)
        self.StartWorkflow1.setIconSize(QSize(40, 40))
        self.StartWorkflow1.setFlat(True)

        self.gridLayout_14.addWidget(self.StartWorkflow1, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.Workflow1, 0, 0, 1, 1)

        self.Workflow3 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow3.setObjectName(u"Workflow3")
        self.Workflow3.setMinimumSize(QSize(0, 75))
        self.Workflow3.setMaximumSize(QSize(16777215, 75))
        self.Workflow3.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.Workflow3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.RenameWorkflow3 = QPushButton(self.Workflow3)
        self.RenameWorkflow3.setObjectName(u"RenameWorkflow3")
        self.RenameWorkflow3.setMinimumSize(QSize(30, 30))
        self.RenameWorkflow3.setMaximumSize(QSize(30, 30))
        self.RenameWorkflow3.setIcon(icon4)
        self.RenameWorkflow3.setIconSize(QSize(20, 20))
        self.RenameWorkflow3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.RenameWorkflow3)

        self.Workflow3Name = QLabel(self.Workflow3)
        self.Workflow3Name.setObjectName(u"Workflow3Name")

        self.horizontalLayout_2.addWidget(self.Workflow3Name)

        self.horizontalSpacer_13 = QSpacerItem(309, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_13)

        self.StartWorkflow3 = QPushButton(self.Workflow3)
        self.StartWorkflow3.setObjectName(u"StartWorkflow3")
        sizePolicy1.setHeightForWidth(self.StartWorkflow3.sizePolicy().hasHeightForWidth())
        self.StartWorkflow3.setSizePolicy(sizePolicy1)
        self.StartWorkflow3.setMinimumSize(QSize(40, 40))
        self.StartWorkflow3.setMaximumSize(QSize(40, 40))
        self.StartWorkflow3.setIcon(icon5)
        self.StartWorkflow3.setIconSize(QSize(40, 40))
        self.StartWorkflow3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.StartWorkflow3)

        self.DeleteWorkflow3 = QPushButton(self.Workflow3)
        self.DeleteWorkflow3.setObjectName(u"DeleteWorkflow3")
        sizePolicy1.setHeightForWidth(self.DeleteWorkflow3.sizePolicy().hasHeightForWidth())
        self.DeleteWorkflow3.setSizePolicy(sizePolicy1)
        self.DeleteWorkflow3.setMinimumSize(QSize(40, 40))
        self.DeleteWorkflow3.setMaximumSize(QSize(40, 40))
        self.DeleteWorkflow3.setIcon(icon6)
        self.DeleteWorkflow3.setIconSize(QSize(40, 40))
        self.DeleteWorkflow3.setFlat(True)

        self.horizontalLayout_2.addWidget(self.DeleteWorkflow3)


        self.gridLayout_6.addWidget(self.Workflow3, 2, 0, 1, 1)

        self.Workflow2 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow2.setObjectName(u"Workflow2")
        self.Workflow2.setMinimumSize(QSize(0, 75))
        self.Workflow2.setMaximumSize(QSize(16777215, 75))
        self.Workflow2.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.Workflow2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.RenameWorkflow2 = QPushButton(self.Workflow2)
        self.RenameWorkflow2.setObjectName(u"RenameWorkflow2")
        self.RenameWorkflow2.setMinimumSize(QSize(30, 30))
        self.RenameWorkflow2.setMaximumSize(QSize(30, 30))
        self.RenameWorkflow2.setIcon(icon4)
        self.RenameWorkflow2.setIconSize(QSize(20, 20))
        self.RenameWorkflow2.setFlat(True)

        self.horizontalLayout_3.addWidget(self.RenameWorkflow2)

        self.Workflow2Name = QLabel(self.Workflow2)
        self.Workflow2Name.setObjectName(u"Workflow2Name")

        self.horizontalLayout_3.addWidget(self.Workflow2Name)

        self.horizontalSpacer_12 = QSpacerItem(309, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_12)

        self.StartWorkflow2 = QPushButton(self.Workflow2)
        self.StartWorkflow2.setObjectName(u"StartWorkflow2")
        sizePolicy1.setHeightForWidth(self.StartWorkflow2.sizePolicy().hasHeightForWidth())
        self.StartWorkflow2.setSizePolicy(sizePolicy1)
        self.StartWorkflow2.setMinimumSize(QSize(40, 40))
        self.StartWorkflow2.setMaximumSize(QSize(40, 40))
        self.StartWorkflow2.setIcon(icon5)
        self.StartWorkflow2.setIconSize(QSize(40, 40))
        self.StartWorkflow2.setFlat(True)

        self.horizontalLayout_3.addWidget(self.StartWorkflow2)

        self.DeleteWorkflow2 = QPushButton(self.Workflow2)
        self.DeleteWorkflow2.setObjectName(u"DeleteWorkflow2")
        sizePolicy1.setHeightForWidth(self.DeleteWorkflow2.sizePolicy().hasHeightForWidth())
        self.DeleteWorkflow2.setSizePolicy(sizePolicy1)
        self.DeleteWorkflow2.setMinimumSize(QSize(40, 40))
        self.DeleteWorkflow2.setMaximumSize(QSize(40, 40))
        self.DeleteWorkflow2.setIcon(icon6)
        self.DeleteWorkflow2.setIconSize(QSize(40, 40))
        self.DeleteWorkflow2.setFlat(True)

        self.horizontalLayout_3.addWidget(self.DeleteWorkflow2)


        self.gridLayout_6.addWidget(self.Workflow2, 1, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_8.addWidget(self.scrollArea, 2, 0, 1, 1)

        self.label = QLabel(self.Workflows)
        self.label.setObjectName(u"label")

        self.gridLayout_8.addWidget(self.label, 1, 0, 1, 1)

        self.pushButton = QPushButton(self.Workflows)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(11)
        self.pushButton.setFont(font)

        self.gridLayout_8.addWidget(self.pushButton, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.Workflows)
        self.Tools = QWidget()
        self.Tools.setObjectName(u"Tools")
        self.gridLayout_4 = QGridLayout(self.Tools)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_4 = QLabel(self.Tools)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_4.addWidget(self.label_4, 0, 0, 1, 2)

        self.scrollArea_2 = QScrollArea(self.Tools)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 617, 440))
        self.gridLayout_15 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.frame = QFrame(self.scrollAreaWidgetContents_2)
        self.frame.setObjectName(u"frame")
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setMinimumSize(QSize(0, 300))
        self.frame.setMaximumSize(QSize(16777215, 16777215))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 3, 0, 1, 1)

        self.ToolDesc = QLabel(self.frame)
        self.ToolDesc.setObjectName(u"ToolDesc")
        self.ToolDesc.setStyleSheet(u"")
        self.ToolDesc.setWordWrap(True)

        self.gridLayout_9.addWidget(self.ToolDesc, 1, 0, 1, 1)

        self.ToolTitle = QLabel(self.frame)
        self.ToolTitle.setObjectName(u"ToolTitle")

        self.gridLayout_9.addWidget(self.ToolTitle, 0, 0, 1, 1)

        self.OpenTool = QPushButton(self.frame)
        self.OpenTool.setObjectName(u"OpenTool")
        self.OpenTool.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.OpenTool.setFont(font1)

        self.gridLayout_9.addWidget(self.OpenTool, 4, 0, 1, 1)

        self.ToolInstructions = QLabel(self.frame)
        self.ToolInstructions.setObjectName(u"ToolInstructions")
        self.ToolInstructions.setWordWrap(True)

        self.gridLayout_9.addWidget(self.ToolInstructions, 2, 0, 1, 1)


        self.gridLayout_15.addWidget(self.frame, 0, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_2, 0, 1, 1, 1)
        self.verticalspacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.gridLayout_15.addItem(self.verticalspacer_7, 1, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout_4.addWidget(self.scrollArea_2, 1, 1, 1, 1)

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

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.stackedWidget)


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
        icon7 = QIcon()
        icon7.addFile(u":/Icons/menu_30dp_FFFFFF_FILL0_wght400_GRAD0_opsz24.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.MenuButton.setIcon(icon7)
        self.MenuButton.setIconSize(QSize(40, 40))
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
        DataTable = open(r'Product-Draft/Files/Settings/WorkflowNameTable.json', 'r')
        data = json.load(DataTable)
        print(data['Workflow1Name'])
        self.Workflow1Name.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:11pt;\">{data['Workflow1Name']}</span></p></body></html>", None))
        self.Workflow2Name.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:11pt;\">{data['Workflow2Name']}</span></p></body></html>", None))
        self.Workflow3Name.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:11pt;\">{data['Workflow3Name']}</span></p></body></html>", None))
        self.Workflow4Name.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:11pt;\">{data['Workflow4Name']}</span></p></body></html>", None))
        self.Workflow5Name.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p><span style=\" font-size:11pt;\">{data['Workflow5Name']}</span></p></body></html>", None))
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.WorkflowsButton.setText(QCoreApplication.translate("MainWindow", u"Workflows", None))
        self.MenuText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Menu</span></p></body></html>", None))
        self.SettingsButton.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.HomepageButton.setText(QCoreApplication.translate("MainWindow", u"Homepage", None))
        self.ToolsButton.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1; font-size:12pt;\"><li>Firstly, the user selects a trigger, of which there are currently two. This will determine how the workflow starts.</li><li>Secondly, the user selects functions, of which there are a variety of. Some, such as \"New Tab\", require the user to be on a browser engine when the workflow is begun or to have opened the browser in one of the previous functions. These functions can be combined to create a workflow.</li><li>Then, the user can begin to use their workflow by pressing the green button next to a workflow.</li><li>After doing this, they can run their workflow by activating the chosen trigger.</li></ul></body></head></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">How does it work?</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">What is this?</span></p></body></html>", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">This is a tool that allows people to automate many mundane tasks. One example of this is setting up your device to get ready for work/school/another occasion. This program can help with that by opening many tabs and desktops for you with the press of a button.</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RenameWorkflow5.setToolTip(QCoreApplication.translate("MainWindow", u"Rename Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.RenameWorkflow5.setText("")
        self.Workflow5Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Workflow 5</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.StartWorkflow5.setToolTip(QCoreApplication.translate("MainWindow", u"Run Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.StartWorkflow5.setText("")
#if QT_CONFIG(tooltip)
        self.DeleteWorkflow5.setToolTip(QCoreApplication.translate("MainWindow", u"Delete Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteWorkflow5.setText("")
#if QT_CONFIG(tooltip)
        self.RenameWorkflow4.setToolTip(QCoreApplication.translate("MainWindow", u"Rename Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.RenameWorkflow4.setText("")
        self.Workflow4Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Workflow 4</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.StartWorkflow4.setToolTip(QCoreApplication.translate("MainWindow", u"Run Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.StartWorkflow4.setText("")
#if QT_CONFIG(tooltip)
        self.DeleteWorkflow4.setToolTip(QCoreApplication.translate("MainWindow", u"Delete Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteWorkflow4.setText("")
        self.Workflow1Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Workflow 1</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.RenameWorkflow1.setToolTip(QCoreApplication.translate("MainWindow", u"Rename Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.RenameWorkflow1.setText("")
#if QT_CONFIG(tooltip)
        self.DeleteWorkflow1.setToolTip(QCoreApplication.translate("MainWindow", u"Delete Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteWorkflow1.setText("")
#if QT_CONFIG(tooltip)
        self.StartWorkflow1.setToolTip(QCoreApplication.translate("MainWindow", u"Run Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.StartWorkflow1.setText("")
#if QT_CONFIG(tooltip)
        self.RenameWorkflow3.setToolTip(QCoreApplication.translate("MainWindow", u"Rename Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.RenameWorkflow3.setText("")
        self.Workflow3Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Workflow 3</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.StartWorkflow3.setToolTip(QCoreApplication.translate("MainWindow", u"Run Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.StartWorkflow3.setText("")
#if QT_CONFIG(tooltip)
        self.DeleteWorkflow3.setToolTip(QCoreApplication.translate("MainWindow", u"Delete Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteWorkflow3.setText("")
#if QT_CONFIG(tooltip)
        self.RenameWorkflow2.setToolTip(QCoreApplication.translate("MainWindow", u"Rename Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.RenameWorkflow2.setText("")
        self.Workflow2Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt;\">Workflow 2</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.StartWorkflow2.setToolTip(QCoreApplication.translate("MainWindow", u"Run Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.StartWorkflow2.setText("")
#if QT_CONFIG(tooltip)
        self.DeleteWorkflow2.setToolTip(QCoreApplication.translate("MainWindow", u"Delete Workflow", None))
#endif // QT_CONFIG(tooltip)
        self.DeleteWorkflow2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:700;\">Current Workflows</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Workflow Creator", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:700;\">Tools</span></p></body></html>", None))
        self.ToolDesc.setText(QCoreApplication.translate("MainWindow", u"Gives the X-Y coordinates of the location of the user's mouse ", None))
        self.ToolTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">X-Y Coordinate Finder</span></p></body></html>", None))
        self.OpenTool.setText(QCoreApplication.translate("MainWindow", u"Open Tool", None))
        self.ToolInstructions.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:700;\">How to use:</span></p><ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Move your mouse to the location you want to find the X-Y coordinates of </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press the ` key (Right below the esc key at the top left) </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copy the X and Y coordinates from the tool </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Paste the X-coordinate into the X-coordinate section </li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; "
                        "text-indent:0px;\">Paste the Y-Coordinate into the Y-Coordinate section </li></ol></body></html>", None))
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
            self.StartWorkflow5.clicked.connect(lambda: runStartWorkflow(5))
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
