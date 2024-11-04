from PySide6.QtWidgets import QApplication, QTextEdit, QVBoxLayout, QWidget, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.text_edit = QTextEdit(self)
        self.check_button = QPushButton("Check Content", self)
        self.check_button.clicked.connect(self.check_content)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.check_button)
        self.setLayout(layout)

    def check_content(self):
        # Get the plain text content
        plain_text = self.text_edit.toPlainText()
        print("Plain Text Content:", plain_text)

        # Get the HTML content
        html_content = self.text_edit.toHtml()
        print("HTML Content:", html_content)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec()
