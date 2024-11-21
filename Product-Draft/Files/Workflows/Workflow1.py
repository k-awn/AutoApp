#New start
import keyboard
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
from time import sleep as wait
from pyautogui import typewrite, click
from os import _exit
from os.path import abspath, join
from pathlib import Path

def response():
	print("hotkey pressed")

keyboard.add_hotkey("]", response, suppress=True, trigger_on_release=True, timeout=1) 
keyboard.wait("esc")
_exit(0)