import os
import undetected_chromedriver as uc
from webdriver_manager.chrome import ChromeDriverManager
import shutil
import json
def Setup():
    abspath = os.path.dirname(os.path.abspath(__file__))
    FilesPath = os.path.join(abspath, 'Files')
    SettingsPath = os.path.join(abspath, 'Files/Settings')
    WorkflowsPath = os.path.join(abspath, 'Files/Workflows')
    CompactModePath = os.path.join(abspath, 'Files/Settings/compact-mode.txt')
    ChromeDriverPath = os.path.join(abspath, 'Files/Chromedriver')
    ChromeDriverExePath = os.path.join(abspath, 'Files/Chromedriver/chromedriver.exe')
    WorkflowRenamePath = os.path.join(abspath, 'Files/Settings/workflowRenamerNum.txt')
    workflowRenameContentPath = os.path.join(abspath, 'Files/Settings/workflowRenamerContent.txt')
    workflowNameTablePath = os.path.join(abspath, 'Files/Settings/workflowNameTable.json')
    if not os.path.exists(FilesPath):
        os.mkdir(FilesPath)
    if not os.path.exists(SettingsPath):
        os.mkdir(SettingsPath)
    if not os.path.exists(WorkflowsPath):
        os.mkdir(WorkflowsPath)
    if not os.path.isfile(CompactModePath):
        open(CompactModePath, 'x')
        open(CompactModePath, 'w').write('False')
    if not os.path.isfile(WorkflowRenamePath):
        open(WorkflowRenamePath, 'x')
    if not os.path.exists(ChromeDriverPath):
        os.mkdir(ChromeDriverPath)
    if not os.path.isfile(workflowRenameContentPath):
        open(workflowRenameContentPath, 'x')
    if not os.path.isfile(ChromeDriverExePath):
        temp_driver_path = ChromeDriverManager().install()
        shutil.copy2(temp_driver_path, ChromeDriverExePath)
    if not os.path.isfile(workflowNameTablePath):
        File = open('Product-Draft/Files/Settings/WorkflowNameTable.json', 'w')
        File.close()
        DataFile = open('Product-Draft/Files/Settings/WorkflowNameTable.json', 'w')
        names = {
            "Workflow1Name": "Workflow1",
            "Workflow2Name": "Workflow2",
            "Workflow3Name": "Workflow3",
            "Workflow4Name": "Workflow4",
            "Workflow5Name": "Workflow5",
        }
        compiledNames = (json.dumps(names))
        DataFile.write(compiledNames)
        DataFile.close()



