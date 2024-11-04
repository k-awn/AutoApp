import sys 
from PySide6 import QtCore as qtc
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets
from PySide6 import QtGui as qtg

from test3_ui import Ui_MainWindow

class MainWindow(QtWidgets.QWidget, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    logo = QIcon()
    logo.addFile(r'assets\images\AppLogo.ico')
    logo.addFile(r'assets\images\AppLogo.png')
    app.setWindowIcon(logo)
    ex = Ui_MainWindow()
    w = QtWidgets.QMainWindow()
    ex.setupUi(w)
    w.showMaximized()
    sys.exit(app.exec())
    

'''
        self.HomepageButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.WorkflowButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 1))
        self.ToolsButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 2))
        self.SettingsButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 3))
        self.stackedWidget.setCurrentIndex(0)   
        def on_button_clicked():
            print('skibidi')     
        self.printButton.clicked.connect(on_button_clicked)
'''

#last line isnt working wtf 