import sys 
from PySide6.QtGui import QIcon, QPalette, QColor
from PySide6.QtCore import QCoreApplication, Qt
from PySide6 import QtWidgets
from UIMain import Ui_MainWindow
from WorkflowMaker import Ui_MainWindow2 
from WorkflowRenamer import Ui_MainWindow3
from PySide6.QtCore import Signal
from os.path import isfile
from time import sleep as wait
from setup import Setup
import os
from os import path
import json
from xyPicker import Ui_MainWindow4
from PySide6.QtWidgets import QMessageBox
try:
    import distutils
    import distutils.version
except ImportError:
    from setuptools._distutils import version as distutils_version
    from setuptools import _distutils as distutils

Setup() #? If the user deletes any of the files on accident it will regenerate them. In addition saves me the pain of figuring out how to use --addfiles on PyInstaller

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Main Window')



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
            abspath = os.path.dirname(os.path.abspath(__file__))
            WorkflowRenamePath = os.path.join(abspath, 'Files/Settings/workflowRenamerNum.txt')
            workflowRenameContentPath = os.path.join(abspath, 'Files/Settings/workflowRenamerContent.txt')
            workflowNameTablePath = os.path.join(abspath, 'Files/Settings/workflowNameTable.json')
            text = open(workflowRenameContentPath, 'r').read()
            num = open(WorkflowRenamePath, 'r').read()
            num = int(num)
            if num == 1:
                DataTable = open(workflowNameTablePath, 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow1Name'] = text
                DataFile = open(workflowNameTablePath, 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow1Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">" + text + "</span></p></body></html>", None))
            elif num == 2:
                DataTable = open(workflowNameTablePath, 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow2Name'] = text
                DataFile = open(workflowNameTablePath, 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow2Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">" + text + "</span></p></body></html>", None))
            elif num == 3:
                DataTable = open(workflowNameTablePath, 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow3Name'] = text
                DataFile = open(workflowNameTablePath, 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow3Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">" + text + "</span></p></body></html>", None))
            elif num == 4:
                DataTable = open(workflowNameTablePath, 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow4Name'] = text
                DataFile = open(workflowNameTablePath, 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow4Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">" + text + "</span></p></body></html>", None))
            else:
                print('its the 5th')
                DataTable = open(workflowNameTablePath, 'r')
                data = json.load(DataTable)
                DataTable.close()
                data['Workflow5Name'] = text
                DataFile = open(workflowNameTablePath, 'w')
                compiledData = json.dumps(data)
                DataFile.write(compiledData)
                DataFile.close()
                self.ui.Workflow5Name.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">" + text + "</span></p></body></html>", None))
            print('end')
        WorkflowRenamePath = os.path.join(abspath, 'Files/Settings/workflowRenamerNum.txt')

        open(WorkflowRenamePath, 'w').write(str(num))
        
        wait(0.01)
        print(open(WorkflowRenamePath, 'r').read())
        self.workflow_renamer = WorkflowRenamer()
        self.workflow_renamer.show()
        self.workflow_renamer.rename_completed.connect(rename)
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
    def closeEvent(self, event):
    # Ask for confirmation before closing
        confirmation = QMessageBox.question(self, "Confirmation", "Are you sure you've finished your workflow? (It does not autosave)", QMessageBox.Yes | QMessageBox.No)

        if confirmation == QMessageBox.Yes:
            event.accept()  # Close the app
        else:
            event.ignore()  # Don't close the app

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self)
        self.setWindowTitle('Create Workflow')
        self.ui.CompileButton.clicked.connect(self.checkSignal)
    def checkSignal(self):
        self.compiled.emit()

class WorkflowRenamer(QtWidgets.QMainWindow):
    rename_completed = Signal()  

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow3()
        self.ui.setupUi(self)
        self.setWindowTitle('Rename Workflow')
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
        self.setWindowTitle('Tool: X-Y Coordinate Picker')
     
if __name__ == "__main__":
    import winreg
    original_theme = None

    # Save current theme setting and switch to dark mode
    if sys.platform == "win32":
        try:
            registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
            key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", 0, winreg.KEY_ALL_ACCESS)
            original_theme = winreg.QueryValueEx(key, "AppsUseLightTheme")[0]  # Save original value
            winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, 0)  # Set dark mode
            winreg.CloseKey(key)
        except:
            pass
            
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    
    # Set dark mode for title bar
    try:
        from ctypes import windll, c_int, byref, sizeof
        DWMWA_USE_IMMERSIVE_DARK_MODE = 20
        windll.dwmapi.DwmSetWindowAttribute(
            int(window.winId()),
            DWMWA_USE_IMMERSIVE_DARK_MODE,
            byref(c_int(2)),
            sizeof(c_int)
        )
    except:
        pass

    abspath = os.path.dirname(os.path.abspath(__file__))
    icoPath = os.path.join(abspath, 'Applogo.ico')
    logo = QIcon()
    logo.addFile(icoPath)
    app.setWindowIcon(logo)
    
    window.show()
    
    # Restore original theme when app closes
    try:
        app.aboutToQuit.connect(lambda: restore_theme(original_theme))
    except:
        pass

    def restore_theme(original_value):
        if original_value is not None and sys.platform == "win32":
            try:
                registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
                key = winreg.OpenKey(registry, r"Software\Microsoft\Windows\CurrentVersion\Themes\Personalize", 0, winreg.KEY_ALL_ACCESS)
                winreg.SetValueEx(key, "AppsUseLightTheme", 0, winreg.REG_DWORD, original_value)
                winreg.CloseKey(key)
            except:
                pass

    sys.exit(app.exec())




    