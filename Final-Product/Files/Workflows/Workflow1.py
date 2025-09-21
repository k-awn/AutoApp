#New start
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import sleep as wait
import pyautogui
<<<<<<< HEAD
from os import _exit, path
from os.path import abspath, join

def response():
	print("hotkey pressed")
	absolutepath = abspath(WORKFLOW_PATH)
	parent_dir = path.dirname(absolutepath)
	grand_parent_dir = path.dirname(parent_dir)
	chromedriverPath = join(grand_parent_dir, "Chromedriver/chromedriver.exe")
	options2 = uc.ChromeOptions()
	prefs = {"credentials_enable_service": False, "profile.password_manager_enabled": False}
	options2.add_experimental_option("prefs",prefs)
	driver = uc.Chrome(options=options2, driver_executable_path=chromedriverPath)
	driver.maximize_window()
	driver.get("https://accounts.google.com/InteractiveLogin/signinchooser?continue=https%3A%2F%2Fclassroom.google.com&passive=true&ifkv=AXH0vVv5pygPAsgvdIn-WTMz1syNik0yfBrj6coT3kxQDwvWt1otNzoxsI8sGd-pektMfgnU-eVt&ddm=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
	x, y = pyautogui.locateCenterOnScreen("C:/Users/danie/Downloads/signinUser.png", confidence=0.7) 
	pyautogui.click(x, y)
	pyautogui.typewrite("daniel.emmer@vischool.lt",interval=0)
	x, y = pyautogui.locateCenterOnScreen("C:/Users/danie/Downloads/nextButton.png", confidence=0.7) 
	pyautogui.click(x, y)
	wait(6)
	pyautogui.typewrite("D@n!el092009",interval=0)
	x, y = pyautogui.locateCenterOnScreen("C:/Users/danie/Downloads/nextButton.png", confidence=0.7) 
	pyautogui.click(x, y)
	wait(10)
	x, y = pyautogui.locateCenterOnScreen("C:/Users/danie/Downloads/cancelButton.png", confidence=0.7) 
	pyautogui.click(x, y)
	with pyautogui.hold("ctrl"): 
		pyautogui.press("t") 
	pyautogui.typewrite("docs.google.com", interval=0)
	pyautogui.press("enter")
	with pyautogui.hold("ctrl"): 
		pyautogui.press("t") 
	pyautogui.typewrite("https://vilnius.managebac.com/login", interval=0)
	pyautogui.press("enter")
	wait(2)
	pyautogui.typewrite("daniel.emmer@vischool.lt",interval=0)
	x, y = pyautogui.locateCenterOnScreen("C:/Users/danie/Downloads/passField.png", confidence=0.7) 
	pyautogui.click(x, y)
	pyautogui.typewrite("D@n1el092009VIS",interval=0)
	x, y = pyautogui.locateCenterOnScreen("C:/Users/danie/Downloads/signinButton.png", confidence=0.7) 
	pyautogui.click(x, y)
=======
from os import _exit
from os.path import abspath, join
from pathlib import Path

def response():
	print("hotkey pressed")
>>>>>>> af825f51d5eebea912ec688448ed75049b8a3f72
response()