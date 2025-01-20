#New start
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import sleep as wait
import pyautogui
from os import _exit, path
from os.path import abspath, join
from pathlib import Path
import sys

def response():
	print("hotkey pressed")
	if hasattr(sys, "getframe"):
		current_file = sys._getframe().f_code.co_filename
	chromedriverPath = join(Path(current_file).parent.parent, "Chromedriver/chromedriver.exe")
	options2 = uc.ChromeOptions()
	prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
	options2.add_experimental_option("prefs",prefs)
	driver = uc.Chrome(options=options2, driver_executable_path=chromedriverPath)
	driver.maximize_window()
	driver.get("https://google.com")
response()