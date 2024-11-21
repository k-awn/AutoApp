import sys 
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets
from test3_ui import Ui_MainWindow
from WorkflowMaker import Ui_MainWindow2 
from os.path import isfile
import time
import threading

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_workflow_maker)
        self.ui.DeleteWorkflow1.clicked.connect(self.Check)
        self.ui.DeleteWorkflow2.clicked.connect(self.Check)
        self.ui.DeleteWorkflow3.clicked.connect(self.Check)
        self.ui.DeleteWorkflow4.clicked.connect(self.Check)
        self.ui.DeleteWorkflow5.clicked.connect(self.Check)
    def open_workflow_maker(self):  
        self.workflow_maker = WorkflowMaker()
        self.workflow_maker.show()
    def Check(self):
            time.sleep(0.2)
            Workflow1Exists = isfile(r'Demo2\workflows\workflow1.py')
            Workflow22Exists = isfile(r'Demo2\workflows\workflow2.py')
            Workflow3Exists = isfile(r'Demo2\workflows\workflow3.py')
            Workflow4Exists = isfile(r'Demo2\workflows\workflow4.py')
            Workflow5Exists = isfile(r'Demo2\workflows\workflow5.py')
            if Workflow1Exists is True:
                self.ui.Workflow1.show()
            else:
                self.ui.Workflow1.hide()
            if Workflow22Exists is True:
                self.ui.Workflow2.show()
            else:
                self.ui.Workflow2.hide()
            if Workflow3Exists is True:
                self.ui.Workflow3.show()
            else:
                self.ui.Workflow3.hide()
            if Workflow4Exists is True:
                self.ui.Workflow4.show()
            else:
                self.ui.Workflow4.hide()
            if Workflow5Exists is True:
                self.ui.Workflow5.show()
            else:
                self.ui.Workflow5.hide()
class WorkflowMaker(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    logo = QIcon()
    logo.addFile(r'assets\images\AppLogo.ico')
    logo.addFile(r'assets\images\AppLogo.png')
    app.setWindowIcon(logo)
    window = MainWindow()
    window.showMaximized()
    sys.exit(app.exec())