import sys 
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets
from UIMain import Ui_MainWindow
from WorkflowMaker import Ui_MainWindow2 
from WorkflowRenamer import Ui_MainWindow3
from PySide6.QtCore import Signal
from os.path import isfile
from time import sleep as wait
import threading
from setup import Setup
from os import path
import json
from xyPicker import Ui_MainWindow4
Setup() #? If the user deletes any of the files on accident it will regenerate them. In addition saves me the pain of figuring out how to use --addfiles on PyInstaller

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_workflow_maker)
        self.ui.OpenTool.clicked.connect(self.open_xy_picker)
        self.ui.RenameWorkflow1.clicked.connect(lambda: self.open_workflow_renamer(1))
        self.ui.RenameWorkflow2.clicked.connect(lambda: self.open_workflow_renamer(2))
        self.ui.RenameWorkflow3.clicked.connect(lambda: self.open_workflow_renamer(3))
        self.ui.RenameWorkflow4.clicked.connect(lambda: self.open_workflow_renamer(4))
        self.ui.RenameWorkflow5.clicked.connect(lambda: self.open_workflow_renamer(5))
        self.ui.DeleteWorkflow1.clicked.connect(self.Check)
        self.ui.DeleteWorkflow2.clicked.connect(self.Check)
        self.ui.DeleteWorkflow3.clicked.connect(self.Check)
        self.ui.DeleteWorkflow4.clicked.connect(self.Check)
        self.ui.DeleteWorkflow5.clicked.connect(self.Check)
        self.ui.WorkflowsButton.clicked.connect(self.Check)
    def open_workflow_renamer(self, num):
        def rename():
            print('start')
            text = open(r'Product-Draft\Files\Settings\workflowRenamerContent.txt', 'r').read()
            num = open(r'Product-Draft\Files\Settings\workflowRenamerNum.txt', 'r').read()
            num = int(num)
            if num == 1:
                DataTable = open(r'Product-Draft/Files/Settings/WorkflowNameTable.json', 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow1Name'] = text
                DataFile = open('Product-Draft/Files/Settings/WorkflowNameTable.json', 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow1Name.setText(text)
            elif num == 2:
                DataTable = open(r'Product-Draft/Files/Settings/WorkflowNameTable.json', 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow2Name'] = text
                DataFile = open('Product-Draft/Files/Settings/WorkflowNameTable.json', 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow2Name.setText(text)
            elif num == 3:
                DataTable = open(r'Product-Draft/Files/Settings/WorkflowNameTable.json', 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow3Name'] = text
                DataFile = open('Product-Draft/Files/Settings/WorkflowNameTable.json', 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow3Name.setText(text)
            elif num == 4:
                DataTable = open(r'Product-Draft/Files/Settings/WorkflowNameTable.json', 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow4Name'] = text
                DataFile = open('Product-Draft/Files/Settings/WorkflowNameTable.json', 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow4Name.setText(text)
            else:
                print('its the 5th')
                DataTable = open(r'Product-Draft/Files/Settings/WorkflowNameTable.json', 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow5Name'] = text
                DataFile = open('Product-Draft/Files/Settings/WorkflowNameTable.json', 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow5Name.setText(text)
            print('end')
        open(r'Product-Draft\Files\Settings\workflowRenamerNum.txt', 'w').write(str(num))
        
        wait(0.01)
        print(open(r'Product-Draft\Files\Settings\workflowRenamerNum.txt', 'r').read())
        self.workflow_renamer = WorkflowRenamer()
        self.workflow_renamer.rename_completed.connect(rename)
        self.xy_picker = xyPicker()
    def open_xy_picker(self):
        self.xy_picker = xyPicker()  # Create an instance
        self.xy_picker.show()


    def open_workflow_maker(self):  
        self.workflow_maker = WorkflowMaker()
        self.workflow_maker.show()
        self.workflow_maker.compiled.connect(self.Check)
    def Check(self):
            wait(0.01)
            abspath = path.dirname(path.abspath(__file__))
            Workflow1Exists = isfile(path.join(abspath, 'Files/workflows/workflow1.py'))
            Workflow22Exists = isfile(path.join(abspath, 'Files/workflows/workflow2.py'))
            Workflow3Exists = isfile(path.join(abspath, 'Files/workflows/workflow3.py'))
            Workflow4Exists = isfile(path.join(abspath, 'Files/workflows/workflow4.py'))
            Workflow5Exists = isfile(path.join(abspath, 'Files/workflows/workflow5.py'))
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
    compiled = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.ui.CompileButton.clicked.connect(self.checkSignal)
    def checkSignal(self):
        self.compiled.emit()

class WorkflowRenamer(QtWidgets.QMainWindow):
    rename_completed = Signal()  

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.ui.saveButton.clicked.connect(self.on_save) 
        self.rename_completed.connect(self.close)

    def on_save(self):
        if len(str(self.ui.workflowNameInput.text())) > 0:
            self.rename_completed.emit()

class xyPicker(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow4()
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