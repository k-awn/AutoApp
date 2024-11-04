from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout
import sys
from toggle import CustomToggle

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Custom Toggle Example")
        
        layout = QVBoxLayout()
        self.toggle = CustomToggle()
        layout.addWidget(self.toggle)
        
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())