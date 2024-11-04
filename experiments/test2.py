import sys
import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
from time import sleep as wait

class SeleniumWorker:
    def run(self):
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

def run_stress_test():
    print("run_stress_test: Creating and starting thread")
    worker = SeleniumWorker()
    thread = threading.Thread(target=worker.run)
    thread.start()
    print("run_stress_test: Stress test started in background")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("MainWindow: Initializing")
        self.setWindowTitle("Stress Test App")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()
        self.button = QPushButton("Start Stress Test")
        self.button.clicked.connect(self.on_button_click)
        layout.addWidget(self.button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        print("MainWindow: Initialization complete")

    def on_button_click(self):
        print("MainWindow: Button clicked")
        run_stress_test()

if __name__ == "__main__":
    print("Main: Starting application")
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    print("Main: Entering event loop")
    sys.exit(app.exec())
