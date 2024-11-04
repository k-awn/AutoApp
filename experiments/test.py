import sys
from PySide6.QtCore import QThread, Signal, QObject
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import sleep as wait
class SeleniumWorker(QObject):
    finished = Signal()

    def run(self):
        self.chrome_stress_test()
        self.finished.emit()

    def chrome_stress_test(self):
        options = uc.ChromeOptions()
        prefs = {'credentials_enable_service': False,
                 'profile.password_manager_enabled': False}
        options.add_experimental_option('prefs', prefs)
        
        driver = uc.Chrome(options=options)
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0,0)")
        driver.get('https://www.supremacy1914.com')
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'didomi-notice-agree-button'))
        )
        driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        username = 'k4wn_'
        password = 'D@n1el092009'
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'loginbox_login_input'))
        )

        driver.find_element(By.ID, 'loginbox_login_input').send_keys(username)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'loginbox_password_input'))
        )
        driver.find_element(By.ID, 'loginbox_password_input').send_keys(password)
        driver.find_element(By.ID, 'loginbutton_cont').click()
        wait(1)
        driver.close()
        wait(1)
        options2 = uc.ChromeOptions()
        prefs = {'credentials_enable_service': False,
                'profile.password_manager_enabled': False}
        options2.add_experimental_option('prefs',prefs)
        driver = uc.Chrome(options=options2)
        driver.maximize_window()
        driver.execute_script("window.scrollTo(0,0)")
        driver.get('https://www.supremacy1914.com')
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'didomi-notice-agree-button'))
        )
        driver.find_element(By.ID, 'didomi-notice-agree-button').click()
        username = 'k4wn_'
        password = 'D@n1el092009'
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.ID, 'loginbox_login_input'))
        )

        driver.find_element(By.ID, 'loginbox_login_input').send_keys(username)
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'loginbox_password_input'))
        )
        driver.find_element(By.ID, 'loginbox_password_input').send_keys(password)
        driver.find_element(By.ID, 'loginbutton_cont').click()
        wait(1)
        driver.close()
        wait(1)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chrome Stress Test")
        self.setGeometry(100, 100, 300, 100)

        layout = QVBoxLayout()
        self.button = QPushButton("Run Chrome Stress Test")
        self.button.clicked.connect(self.run_stress_test)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.thread = None
        self.worker = None

    def run_stress_test(self):
        if self.thread is None:
            self.button.setEnabled(False)
            self.thread = QThread()
            self.worker = SeleniumWorker()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            self.thread.finished.connect(self.on_thread_finish)
            self.thread.start()
        else:
            print("Test is already running")

    def on_thread_finish(self):
        self.thread = None
        self.worker = None
        self.button.setEnabled(True)
        print("Chrome Stress Test completed")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
