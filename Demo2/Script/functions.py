import threading
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import keyboard 
import pyautogui
from time import sleep as wait
#! BUTTONHTML
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

def runSeleniumWorker():
    print("Seleniumworker - creating and starting thread")
    worker = SeleniumWorker()
    thread = threading.Thread(target=worker.run)
    thread.start()
    print("Seleniumworker - started in background")
#! ButtonHotkey

class TypeWorker:
    def run(self,content,hotkey):
        def response():
            pyautogui.typewrite(content, interval=0.01)
            wait(1)
        hotkey = keyboard.add_hotkey(hotkey=hotkey, callback=response, suppress=True, trigger_on_release=True)
        keyboard.wait('esc')
        keyboard.remove_hotkey(hotkey)
        quit()
        
def runTypeWorker(content, hotkey):
    print("Typeworker - creating and starting thread")
    worker = TypeWorker()
    thread = threading.Thread(target=worker.run, args=(content, hotkey))
    thread.start()
    print("Typeworker - started in background")

class ClickWorker:
    def run(self, x, y, hotkey):
        def response():
            pyautogui.click(int(x), int(y))
            wait(1)
        hotkey = keyboard.add_hotkey(hotkey, callback=response, suppress=True, trigger_on_release=True)
        keyboard.wait('esc')
        keyboard.remove_hotkey(hotkey)
        quit()


def runClickWorker(x,y,hotkey):
    print("ClickWorker - creating and starting thread")
    worker = ClickWorker()
    thread = threading.Thread(target=worker.run, args=(x, y, hotkey))
    thread.start()
    print('ClickWorker - started in background')