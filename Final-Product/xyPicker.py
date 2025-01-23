# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'funnytoolbvhgFx.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize)
from PySide6.QtGui import (QIcon)
from PySide6.QtWidgets import (QFrame, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
from pyautogui import position
from time import sleep as wait
import keyboard
import threading

#removal of unnecessary imports SHOULD make it startup faster (?)
class Ui_MainWindow4(object):
    def setupUi(self, MainWindow4):
        if not MainWindow4.objectName():
            MainWindow4.setObjectName(u"MainWindow4")
        MainWindow4.resize(600, 600)
        MainWindow4.setMinimumSize(QSize(600, 600))
        MainWindow4.setMaximumSize(QSize(750, 750))
        self.centralwidget = QWidget(MainWindow4)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 0))
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 7, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.xCoord = QLabel(self.frame_2)
        self.xCoord.setObjectName(u"xCoord")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xCoord.sizePolicy().hasHeightForWidth())
        self.xCoord.setSizePolicy(sizePolicy)
        self.xCoord.setMinimumSize(QSize(50, 30))
        self.xCoord.setAutoFillBackground(True)

        self.gridLayout_3.addWidget(self.xCoord, 1, 2, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 1, 4, 1, 1)

        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(30, 30))
        self.pushButton.setMaximumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/Icons/copy_icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(17, 17))
        self.pushButton.setFlat(True)

        self.gridLayout_3.addWidget(self.pushButton, 1, 6, 1, 1)

        self.yCoord = QLabel(self.frame_2)
        self.yCoord.setObjectName(u"yCoord")
        self.yCoord.setMinimumSize(QSize(50, 30))
        self.yCoord.setMaximumSize(QSize(1000, 16777215))
        self.yCoord.setAutoFillBackground(True)

        self.gridLayout_3.addWidget(self.yCoord, 1, 5, 1, 1)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(30, 30))
        self.pushButton_2.setMaximumSize(QSize(30, 30))
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(17, 17))
        self.pushButton_2.setFlat(True)

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 4, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 6, 0, 1, 2)

        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 2)

        self.startButton = QPushButton(self.frame)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setMinimumSize(QSize(0, 30))
        self.startButton.setMaximumSize(QSize(16777215, 30))

        self.gridLayout_2.addWidget(self.startButton, 5, 0, 1, 2)

        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 2)

        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 2)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        MainWindow4.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow4)

        QMetaObject.connectSlotsByName(MainWindow4)

        def disable():
            global running
            running = False
            keyboard.unhook_all()  # Remove all hotkeys when stopping

        # Initialize the hotkey
        keyboard.add_hotkey('`', callback=disable, suppress=True, trigger_on_release=True)

        class runStart:
            def run(self, xCoord, yCoord):
                global running
                running = True 
                while running:
                    global x, y  
                    x, y = position()
                    xCoord.setText(QCoreApplication.translate("MainWindow4", u"<html><head/><body><p align=\"center\">" + str(x) + u"</p></body></html>", None))
                    yCoord.setText(QCoreApplication.translate("MainWindow4", f"<html><head/><body><p align=\"center\">{str(y)}</p></body></html>", None))
                    wait(0.05)

        def runStartWorkflow(xCoord, yCoord):
            worker = runStart()
            thread = threading.Thread(target=lambda: worker.run(xCoord, yCoord))
            thread.daemon = True  # this (hopefully) makes it so if you close the window while its running it wont run forever
            thread.start()
            return thread
        def copyxCoord():
            from pyperclip import copy
            copy(str(x))
        self.pushButton_2.clicked.connect(copyxCoord)
        def copyyCoord():
            from pyperclip import copy
            copy(str(y))
        self.pushButton.clicked.connect(copyyCoord)
        self.startButton.clicked.connect(lambda: runStartWorkflow(self.xCoord, self.yCoord))
    # setupUi

    def retranslateUi(self, MainWindow4):
        MainWindow4.setWindowTitle(QCoreApplication.translate("MainWindow4", u"MainWindow", None))
        self.xCoord.setText(QCoreApplication.translate("MainWindow4", u"<html><head/><body><p align=\"center\">null</p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow4", u"X-Coordinate", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow4", u"Y-Coordinate", None))
        self.pushButton.setText("")
        self.yCoord.setText(QCoreApplication.translate("MainWindow4", u"<html><head/><body><p align=\"center\">null</p></body></html>", None))
        self.pushButton_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow4", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Instructions</span></p></body></html>", None))
        self.startButton.setText(QCoreApplication.translate("MainWindow4", u"Start", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow4", u"<html><head/><body><ol style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press the &quot;Start&quot; button</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Move your mouse to the location you want to find the X-Y coordinates of</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press the ` key (Right below the esc key at the top left) to make the coordinates stop changing</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press the copy button next to the X-coordinate </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Paste the X-coordinat"
                        "e into the X-coordinate section </li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Press the copy button next to the Y-Coordinate</li><li style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Paste the Y-Coordinate into the Y-Coordinate section </li></ol></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow4", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">X-Y Coordinate Picker</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow4", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700;\">Coordinates</span></p></body></html>", None))
    # retranslateUi

