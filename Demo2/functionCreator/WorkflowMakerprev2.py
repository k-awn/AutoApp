# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'WorkflowMakerUvvzUc.ui'
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
    QSpacerItem, QStackedWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(665, 630)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
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

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 9, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 2)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.scrollArea = QScrollArea(self.centralwidget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 645, 159))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.LabelLayout = QGridLayout()
        self.LabelLayout.setObjectName(u"LabelLayout")
        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.LabelLayout.addItem(self.verticalSpacer_3, 99999, 0, 1, 1)


        self.verticalLayout.addLayout(self.LabelLayout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout.addWidget(self.scrollArea, 3, 0, 1, 2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 0, 1, 1)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.trigSettings.setCurrentIndex(0)
        self.funcSettings.setCurrentIndex(0)
        orderedMethod = {}
        QMetaObject.connectSlotsByName(MainWindow)
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
            trigIndex = str(self.triggerDropDown.currentIndex())
            indexKey = {
                0 : 'Hotkey',
                1 : 'Set Interval'
            }
            trigName = indexKey.get(int(trigIndex))
            count = self.LabelLayout.count() - 1
            if trigIndex == '0':
                hotkey = self.textEdit.toPlainText()
                if len(hotkey) == 0:
                    return
                orderedMethod[count] = {'type': 'Hotkey', 'hotkey': hotkey}
                additionalContent = ('hotkey=' + hotkey)
            elif trigIndex == '1':
                interval = self.textEdit_2.toPlainText()
                if len(interval) == 0:
                    return
                orderedMethod[count] = {'type': 'Interval', 'interval': interval}
                additionalContent = ('interval=' + interval)
            self.label = QLabel(trigName + ' ' + additionalContent)
            self.label.setObjectName(u"step" + str(count))
            self.LabelLayout.addWidget(self.label, count, 0, 1, 1)
            print(orderedMethod)
        def AddFunction():
            funcIndex = str(self.functionDropDown.currentIndex())
            count = self.LabelLayout.count() - 1

            #! FuncIndex = 0
            indexKey = {
                0 : 'Open Browser',
                1 : 'Click Button',
                2 : 'Click on Screen',
                3 : 'Typewrite',
                4 : 'Wait' 
            }
            if funcIndex == '0':
                url = self.textEdit_3.toPlainText()
                if len(url) == 0:
                    return
                orderedMethod[count] = {'type': 'Open Browser', 'url': url}
                additionalContent = ('url=' + url)
            if funcIndex == '1':
                xPath = self.xPathInput.toPlainText()
                if len(xPath) == 0:
                    return
                orderedMethod[count] = {'type': 'Click Button', 'xpath': xPath}
                additionalContent = ('xPath=' + xPath)
            if funcIndex == '2':
                xCoord = self.xCoordInputClick.toPlainText()
                yCoord = self.yCoordInputClick.toPlainText()
                if len(xCoord) == 0 or len(yCoord) == 0:
                    return
                orderedMethod[count] = {'type':'Click on Screen', 'xcoord': xCoord, 'ycoord': yCoord}
                additionalContent = ('xCoord=' + xCoord + ' yCoord=' + yCoord)
            if funcIndex == '3':
                content = self.contentInput.toPlainText()
                if len(content) == 0:
                    return
                orderedMethod[count] = {'type': 'Typewrite', 'content': content}
                additionalContent = ('content=' + content)
            if funcIndex == '4':
                duration = self.textEdit_4.toPlainText()
                if len(duration) == 0:
                    return
                orderedMethod[count] = {'type': 'Wait', 'duration': duration}
                additionalContent = ('duration=' + duration)
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
            values = len(orderedMethod)
            writeText = open(r'Demo2\functionCreator\function.py', 'w')
            writeText.write('#New start')
            writeText.write('\n' + 'import keyboard' + '\n' + 'from selenium.webdriver.common.by import By' + '\n' + 'from selenium.webdriver.support import expected_conditions as EC' + '\n' + 'import undetected_chromedriver as uc' + '\n' + 'from time import sleep as wait' + '\n' + 'from pyautogui import typewrite, click' + '\n') #? All the imports are here!
            writeText.write('\n\n' + 'def response():' + '\n\t' + 'print("hotkey pressed")')
            if values > 1:
                for i in range(values-1):
                    realnum = i+1
                    #! all the functions go here
                    prevVersion = open(r'Demo2\functionCreator\function.py', 'r')
                    prevText = prevVersion.read()
                    writeText.write(prevText + '\n\t')
                    if orderedMethod[realnum]['type'] == 'Open Browser':
                        #? The below code is barely readable due to the amount of lines required. \n\t means new line, new tab.
                        writeText.write('options2 = uc.ChromeOptions()\n\tprefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}\n\toptions2.add_experimental_option("prefs",prefs)\n\tdriver = uc.Chrome(options=options2, driver_executable_path="Demo2/functionCreator/chromedriver.exe")\n\tdriver.maximize_window()\n\t') #TODO: Make driver.maximize_window optional (might not do this), also these are the settings
                        writeText.write(f'driver.get("{orderedMethod[realnum]['url']}")') #! this is the line that opens the browser at the specified url
                    elif orderedMethod[realnum]['type'] == 'Click Button':
                        writeText.write(f'driver.find_element(By.XPATH, "{orderedMethod[realnum]['xpath']}").click()') #TODO: Try to make a tutorial especially for this 
                    elif orderedMethod[realnum]['type'] == 'Click on Screen':
                        writeText.write(f'click(x={str(orderedMethod[realnum]['xcoord'])}, y={str(orderedMethod[realnum]['ycoord'])})')
                    elif orderedMethod[realnum]['type'] == 'Typewrite':
                        writeText.write(f'typewrite("{orderedMethod[realnum]['content']}",interval=0.01)') #!Add interval later on
                    elif orderedMethod[realnum]['type'] == 'Wait':
                        writeText.write(f'wait({orderedMethod[realnum]['duration']})')
            #!Hotkeys come aftr because it refers to the function where all the functions are sooo
            try:
                if orderedMethod[0]['type'] == 'Hotkey':
                    hotkey = orderedMethod[0]['hotkey']
                    writeText.write(f'\n\nkeyboard.add_hotkey("{hotkey}", response, suppress=True, trigger_on_release=True) ') #TODO: Make trigger on release an option  
                    writeText.write('\nkeyboard.wait("esc")')
                    #! My genius idae: since you only have one hotkey you must do hotkey then def response and everything else goes into response !!! screw readability
            except:
                print('The list is empty')
                
            
            #writes content (function input) into function.py
            #prevVersion = open(r'Demo2\functionCreator\function.py', 'r')
            #prevText = prevVersion.read()
            #prevVersion.close()
        
        self.pushButton_3.clicked.connect(Compile)
        self.pushButton_2.clicked.connect(AddFunction)
        self.pushButton.clicked.connect(AddTrigger)
        self.pushButton.clicked.connect(Check)
        self.pushButton_2.clicked.connect(Check)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trigger Selected:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Trigger", None))
        self.triggerDropDown.setItemText(0, QCoreApplication.translate("MainWindow", u"Hotkey", None))
        self.triggerDropDown.setItemText(1, QCoreApplication.translate("MainWindow", u"Set interval", None))

        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your hotkey here", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Hotkey", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Interval:", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Write your interval here", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Create Trigger</span></p></body></html>", None))
        self.functionDropDown.setItemText(0, QCoreApplication.translate("MainWindow", u"Open Browser ", None))
        self.functionDropDown.setItemText(1, QCoreApplication.translate("MainWindow", u"Click Button(Browser)", None))
        self.functionDropDown.setItemText(2, QCoreApplication.translate("MainWindow", u"Click On Screen", None))
        self.functionDropDown.setItemText(3, QCoreApplication.translate("MainWindow", u"Typewrite", None))
        self.functionDropDown.setItemText(4, QCoreApplication.translate("MainWindow", u"Wait", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Browser URL", None))
        self.textEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your browser URL here", None))
        self.xPathLabel.setText(QCoreApplication.translate("MainWindow", u"XPath:", None))
        self.xPathInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type the XPath to the button here (Find in inspect element)", None))
        self.yCoordLabel.setText(QCoreApplication.translate("MainWindow", u"Y-Coordinate", None))
        self.xCoordLabel.setText(QCoreApplication.translate("MainWindow", u"X-Coordinate", None))
        self.yCoordInputClick.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your Y-Coordinate here", None))
        self.xCoordInputClick.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your X-Coordinate here", None))
        self.contentInput.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your content here", None))
        self.contentLabel.setText(QCoreApplication.translate("MainWindow", u"Content", None))
        self.textEdit_4.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Type your wait duration here", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Wait Duration", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Add Function", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Function Selected:", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:700;\">Create Function</span></p></body></html>", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Compile Code", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Item List</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:700;\">Workflow Creator</span></p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"This is the part where I say where your code has been saved", None))
    # retranslateUi