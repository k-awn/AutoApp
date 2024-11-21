import os
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
import shutil
def Setup():
    abspath = os.path.dirname(os.path.abspath(__file__))
    FilesPath = os.path.join(abspath, 'Files')
    SettingsPath = os.path.join(abspath, 'Files/Settings')
    WorkflowsPath = os.path.join(abspath, 'Files/Workflows')
    CompactModePath = os.path.join(abspath, 'Files/Settings/compact-mode.txt')
    ChromeDriverPath = os.path.join(abspath, 'Files/Chromedriver')
    ChromeDriverExePath = os.path.join(abspath, 'Files/Chromedriver/chromedriver.exe')
    if not os.path.exists(FilesPath):
        os.mkdir(FilesPath)
    if not os.path.exists(SettingsPath):
        os.mkdir(SettingsPath)
    if not os.path.exists(WorkflowsPath):
        os.mkdir(WorkflowsPath)
    if not os.path.isfile(CompactModePath):
        open(CompactModePath, 'x')
        open(CompactModePath, 'w').write('False')
    if not os.path.exists(ChromeDriverPath):
        os.mkdir(ChromeDriverPath)
    if not os.path.isfile(ChromeDriverExePath):
        temp_driver_path = ChromeDriverManager().install()
        shutil.copy2(temp_driver_path, ChromeDriverExePath)



