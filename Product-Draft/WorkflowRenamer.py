# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WorkflowRenamerZWwKMW.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)
from time import sleep as wait
class Ui_MainWindow3(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 125)
        MainWindow.setMinimumSize(QSize(500, 125))
        MainWindow.setMaximumSize(QSize(500, 125))
        self.MainThing = QWidget(MainWindow)
        self.MainThing.setObjectName(u"MainThing")
        self.MainThing.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout = QGridLayout(self.MainThing)
        self.gridLayout.setObjectName(u"gridLayout")
        self.instructionsText = QLabel(self.MainThing)
        self.instructionsText.setObjectName(u"instructionsText")
        self.instructionsText.setMaximumSize(QSize(16777215, 50))

        self.gridLayout.addWidget(self.instructionsText, 0, 0, 1, 2)

        self.workflowNameInput = QLineEdit(self.MainThing)
        self.workflowNameInput.setObjectName(u"workflowNameInput")
        self.workflowNameInput.setMaxLength(15)

        self.gridLayout.addWidget(self.workflowNameInput, 1, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 0, 1, 2)

        self.saveButton = QPushButton(self.MainThing)
        self.saveButton.setObjectName(u"saveButton")

        self.gridLayout.addWidget(self.saveButton, 2, 0, 1, 2)

        MainWindow.setCentralWidget(self.MainThing)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        QMetaObject.connectSlotsByName(MainWindow)
        wait(0.1)
        numFile = open(r'Product-Draft\Files\Settings\workflowRenamerNum.txt', 'r')
        workflowNum = numFile.read()
        numFile.close()
        print(workflowNum)
        def writeContent():
            content = self.workflowNameInput.text()
            if len(content) >= 0:            
                contentFile = open(r'Product-Draft\Files\Settings\workflowRenamerContent.txt', 'w')
                contentFile.write(str(content))
                contentFile.close()
            else:
                self.workflowNameInput.setPlaceholderText('Name must have atleast 1 character')
        self.saveButton.clicked.connect(writeContent)
        self.instructionsText.setText(QCoreApplication.translate("MainWindow", f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Edit the name of Workflow {workflowNum}</span></p></body></html>", None))
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.instructionsText.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Edit the name of Workflow</span></p></body></html>", None))
        self.workflowNameInput.setText("")
        self.workflowNameInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Workflow name here (1-20 characters)", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

