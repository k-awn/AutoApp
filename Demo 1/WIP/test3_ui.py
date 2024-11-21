# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test3.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QWidget)
import Icons_rc

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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, -27, 566, 423))
        self.gridLayout_6 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
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
        icon4 = QIcon()
        icon4.addFile(u":/Icons/start_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.StartWorkflow3.setIcon(icon4)
        self.StartWorkflow3.setIconSize(QSize(50, 50))
        self.StartWorkflow3.setFlat(True)

        self.gridLayout_13.addWidget(self.StartWorkflow3, 0, 2, 1, 1)

        self.DeleteWorkflow3 = QPushButton(self.Workflow3)
        self.DeleteWorkflow3.setObjectName(u"DeleteWorkflow3")
        self.DeleteWorkflow3.setMinimumSize(QSize(50, 50))
        self.DeleteWorkflow3.setMaximumSize(QSize(50, 50))
        icon5 = QIcon()
        icon5.addFile(u":/Icons/delete_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.DeleteWorkflow3.setIcon(icon5)
        self.DeleteWorkflow3.setIconSize(QSize(50, 50))
        self.DeleteWorkflow3.setFlat(True)

        self.gridLayout_13.addWidget(self.DeleteWorkflow3, 0, 3, 1, 1)


        self.gridLayout_6.addWidget(self.Workflow3, 2, 0, 1, 1)

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
        self.StartWorkflow1.setIcon(icon4)
        self.StartWorkflow1.setIconSize(QSize(50, 50))
        self.StartWorkflow1.setFlat(True)

        self.gridLayout_14.addWidget(self.StartWorkflow1, 0, 2, 1, 1)

        self.DeleteWorkflow1 = QPushButton(self.Workflow1)
        self.DeleteWorkflow1.setObjectName(u"DeleteWorkflow1")
        self.DeleteWorkflow1.setMinimumSize(QSize(50, 50))
        self.DeleteWorkflow1.setMaximumSize(QSize(50, 50))
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

        self.Workflow5 = QFrame(self.scrollAreaWidgetContents)
        self.Workflow5.setObjectName(u"Workflow5")
        self.Workflow5.setMinimumSize(QSize(0, 75))
        self.Workflow5.setMaximumSize(QSize(16777215, 75))
        self.Workflow5.setStyleSheet(u"QFrame { border: none; }")
        self.Workflow5.setFrameShape(QFrame.Shape.StyledPanel)
        self.Workflow5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_15 = QGridLayout(self.Workflow5)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_18 = QLabel(self.Workflow5)
        self.label_18.setObjectName(u"label_18")

        self.gridLayout_15.addWidget(self.label_18, 1, 0, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_9, 1, 1, 1, 1)

        self.DeleteWorkflow5 = QPushButton(self.Workflow5)
        self.DeleteWorkflow5.setObjectName(u"DeleteWorkflow5")
        self.DeleteWorkflow5.setMinimumSize(QSize(50, 50))
        self.DeleteWorkflow5.setMaximumSize(QSize(50, 50))
        self.DeleteWorkflow5.setIcon(icon5)
        self.DeleteWorkflow5.setIconSize(QSize(50, 50))
        self.DeleteWorkflow5.setFlat(True)

        self.gridLayout_15.addWidget(self.DeleteWorkflow5, 1, 3, 1, 1)

        self.StartWorkflow5 = QPushButton(self.Workflow5)
        self.StartWorkflow5.setObjectName(u"StartWorkflow5")
        self.StartWorkflow5.setMinimumSize(QSize(50, 50))
        self.StartWorkflow5.setMaximumSize(QSize(50, 50))
        self.StartWorkflow5.setIcon(icon4)
        self.StartWorkflow5.setIconSize(QSize(50, 50))
        self.StartWorkflow5.setFlat(True)

        self.gridLayout_15.addWidget(self.StartWorkflow5, 1, 2, 1, 1)


        self.gridLayout_6.addWidget(self.Workflow5, 4, 0, 1, 1)

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

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer_3, 5, 0, 1, 1)

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

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
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
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Workflow 3", None))
        self.StartWorkflow3.setText("")
        self.DeleteWorkflow3.setText("")
        self.StartWorkflow1.setText("")
        self.DeleteWorkflow1.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Workflow 1", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Workflow 2", None))
        self.StartWorkflow2.setText("")
        self.DeleteWorkflow2.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Workflow 5", None))
        self.DeleteWorkflow5.setText("")
        self.StartWorkflow5.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Workflow 4", None))
        self.StartWorkflow4.setText("")
        self.DeleteWorkflow4.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Current Workflows</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Open Workflow Creator", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"This part is an extra part of the app, if I finish and still want to keep going to improve the user experience of the app, etc. I will only need to do this after I finish all of the other parts of my app.", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:700;\">Compact Mode</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">Page Name</span></p></body></html>", None))
        self.MenuButton.setText("")
    # retranslateUi

