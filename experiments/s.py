import sys 
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets
from test3_ui import Ui_MainWindow
# Import your WorkflowMaker (adjust the import path as needed)
from WorkflowMaker import WorkflowMaker


class MainWindow(QtWidgets.QMainWindow):  # Change to QMainWindow
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Add button connection
        self.ui.workflowMakerButton.clicked.connect(self.open_workflow_maker)
    
    def open_workflow_maker(self):
        self.workflow_maker = WorkflowMaker()
        self.workflow_maker.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    logo = QIcon()
    logo.addFile(r'assets\images\AppLogo.ico')
    logo.addFile(r'assets\images\AppLogo.png')
    app.setWindowIcon(logo)
    
    window = MainWindow()  # Create the main window
    window.showMaximized()
    sys.exit(app.exec())
