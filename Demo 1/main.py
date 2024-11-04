import sys 
from PySide6 import QtCore as qtc
from PySide6.QtGui import QIcon
from PySide6 import QtWidgets
from PySide6 import QtGui as qtg
from functools import partial

from Demo2_ui import Ui_MainWindow


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

'''
        self.HomepageButton.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.WorkflowButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 1))
        self.ToolsButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 2))
        self.SettingsButton.clicked.connect(partial(self.stackedWidget.setCurrentIndex, 3))
        self.stackedWidget.setCurrentIndex(0)   
        def on_button_clicked():
            print('skibidi')     
        self.printButton.clicked.connect(on_button_clicked)
        def she_skibidi_my_toilet_until_i_rizz():
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
            self.pushButton_2.clicked.connect(she_skibidi_my_toilet_until_i_rizz)
'''

#last line isnt working wtf 