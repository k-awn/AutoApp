#New start
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import sleep as wait
from pyautogui import typewrite, click
from os import _exit


def response():
	print("hotkey pressed")
	options2 = uc.ChromeOptions()
	prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
	options2.add_experimental_option("prefs",prefs)
	driver = uc.Chrome(options=options2, driver_executable_path="Demo2/functionCreator/chromedriver.exe")
	driver.maximize_window()
	driver.get("https://google.com")

keyboard.add_hotkey("]", response, suppress=True, trigger_on_release=True, timeout=1) 
keyboard.wait("esc")
_exit(0)