import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QFrame, QGridLayout, QWidget)
from PySide6.QtCore import Qt

class ResponsiveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window1")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        frame = QFrame(central_widget)
        frame.setFrameStyle(QFrame.NoFrame)
        layout = QGridLayout(frame)

        button1 = QPushButton("Button 1", frame)
        button2 = QPushButton("Button 2", frame)
        button3 = QPushButton("Button 3", frame)
        button4 = QPushButton("Button 4", frame)
        button5 = QPushButton("Button 5", frame)
        button6 = QPushButton("Button 6", frame)
        button7 = QPushButton("Button 7", frame)
        button8 = QPushButton("Button 8", frame)
        button9 = QPushButton("Button 9", frame)

        button1.setFixedSize(90, 90)
        button2.setFixedSize(90, 90)
        button3.setFixedSize(90, 90)
        button4.setFixedSize(90, 90)
        button5.setFixedSize(90, 90)
        button6.setFixedSize(90, 90)
        button7.setFixedSize(90, 90)
        button8.setFixedSize(90, 90)
        button9.setFixedSize(90, 90)

        layout.addWidget(button1, 0, 0)
        layout.addWidget(button2, 0, 1)
        layout.addWidget(button3, 0, 2)
        layout.addWidget(button4, 1, 0)
        layout.addWidget(button5, 1, 1)
        layout.addWidget(button6, 1, 2)
        layout.addWidget(button7, 2, 0)
        layout.addWidget(button8, 2, 1)
        layout.addWidget(button9, 2, 2)

        layout.setContentsMargins(10, 10, 10, 10)
        layout.setSpacing(10)
        
        main_layout = QGridLayout(central_widget)
        main_layout.addWidget(frame)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        self.setMinimumSize(300, 300)
        self.resize(310, 310)

class SemiResponsiveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window2")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        button1 = QPushButton("Button 1", central_widget)
        button2 = QPushButton("Button 2", central_widget)
        button3 = QPushButton("Button 3", central_widget)
        button4 = QPushButton("Button 4", central_widget)
        button5 = QPushButton("Button 5", central_widget)
        button6 = QPushButton("Button 6", central_widget)
        button7 = QPushButton("Button 7", central_widget)
        button8 = QPushButton("Button 8", central_widget)
        button9 = QPushButton("Button 9", central_widget)

        button1.setGeometry(10, 10, 90, 90)
        button2.setGeometry(110, 10, 90, 90)
        button3.setGeometry(210, 10, 90, 90)
        button4.setGeometry(10, 110, 90, 90)
        button5.setGeometry(110, 110, 90, 90)
        button6.setGeometry(210, 110, 90, 90)
        button7.setGeometry(10, 210, 90, 90)
        button8.setGeometry(110, 210, 90, 90)
        button9.setGeometry(210, 210, 90, 90)

        self.setMinimumSize(100, 100)
        self.resize(310, 310)

class nonResponsiveWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Window3")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        button1 = QPushButton("Button 1", central_widget)
        button2 = QPushButton("Button 2", central_widget)
        button3 = QPushButton("Button 3", central_widget)
        button4 = QPushButton("Button 4", central_widget)
        button5 = QPushButton("Button 5", central_widget)
        button6 = QPushButton("Button 6", central_widget)
        button7 = QPushButton("Button 7", central_widget)
        button8 = QPushButton("Button 8", central_widget)
        button9 = QPushButton("Button 9", central_widget)

        button1.setGeometry(10, 10, 90, 90)
        button2.setGeometry(110, 10, 90, 90)
        button3.setGeometry(210, 10, 90, 90)
        button4.setGeometry(10, 110, 90, 90)
        button5.setGeometry(110, 110, 90, 90)
        button6.setGeometry(210, 110, 90, 90)
        button7.setGeometry(10, 210, 90, 90)
        button8.setGeometry(110, 210, 90, 90)
        button9.setGeometry(210, 210, 90, 90)

        self.setMinimumSize(310, 310)
        self.setMaximumSize(310,310)
def main():
    app = QApplication(sys.argv)
    
    responsive_window = ResponsiveWindow()
    responsive_window.setGeometry(200, 100, 310, 310)
    responsive_window.show()
    
    semi_responsive_window = SemiResponsiveWindow()
    semi_responsive_window.setGeometry(600, 100, 310, 310)
    semi_responsive_window.show()

    non_responsive_window = nonResponsiveWindow()
    non_responsive_window.setGeometry(1000, 100, 310, 310)
    non_responsive_window.show()
    
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
