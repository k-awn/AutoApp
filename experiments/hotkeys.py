
# Keyboard module in Python 
import keyboard 
import pyautogui
from time import sleep as wait
# press ctrl+shift+z to print "Hotkey Detected" 
def response():
    pyautogui.typewrite('chairs', interval=0.01)
    wait(1)
keyboard.add_hotkey(']', response, suppress=True, trigger_on_release=True) 

keyboard.wait('esc')    