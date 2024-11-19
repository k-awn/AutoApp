import sys 
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets
from WorkflowMakerprev2 import Ui_MainWindow
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
#! Future daniel: make it so the trigger only shows up on the first step and the function on all of the steps after
