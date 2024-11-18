#New start
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import sleep as wait
from pyautogui import typewrite, click


def response():
	print("hotkey pressed")
	click(x=500, y=500)

keyboard.add_hotkey("]", response, suppress=True, trigger_on_release=True) 
keyboard.wait("esc")