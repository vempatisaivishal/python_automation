import pyautogui
import time
import subprocess
import pandas as pd
import pyodbc
import os
import shutil
def open_explorer():
    print("Opening the File Explorer...")
    time.sleep(1)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('File Explorer', interval=0.1)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
def this_pc():
    pyautogui.hotkey('F11')
    time.sleep(2)
    location_pc = pyautogui.locateOnScreen('image.png', confidence=0.9)
    center = pyautogui.center(location_pc)
    pyautogui.doubleClick(center)
    time.sleep(2)
    location_os = pyautogui.locateOnScreen('os_c.png', confidence=0.9)
    center1 = pyautogui.center(location_os)
    pyautogui.doubleClick(center1)
    time.sleep(2)
    location_user = pyautogui.locateOnScreen('Users.png', confidence=0.9)
    center2 = pyautogui.center(location_user)
    pyautogui.doubleClick(center2)
    time.sleep(2)
    location_vishal = pyautogui.locateOnScreen('name.png', confidence=0.9)
    center3 = pyautogui.center(location_vishal)
    pyautogui.doubleClick(center3)
    time.sleep(2)
    location_pdf = pyautogui.locateOnScreen('open_file.png', confidence=0.9)
    center4 = pyautogui.center(location_pdf)
    pyautogui.doubleClick(center4)
    time.sleep(2)
    location_output = pyautogui.locateOnScreen('output.png', confidence=0.9)
    center5 = pyautogui.center(location_output)
    pyautogui.click(center5)
    time.sleep(2)
    pyautogui.hotkey('ctrl','c')
    time.sleep(1)
    pyautogui.hotkey('backspace')
def create_and_paste():
    new_folder_path = r'C:\Users\Saivishal.Vempati\copy_paste'
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
        time.sleep(2)
        location_copy=pyautogui.locateOnScreen('copy_paste.png', confidence=0.9)
        center6=pyautogui.center(location_copy)
        pyautogui.doubleClick(center6)
        time.sleep(1)
        pyautogui.hotkey('ctrl','v')
    else:
        time.sleep(2)
        location_copy=pyautogui.locateOnScreen('copy_paste.png', confidence=0.9)
        center6=pyautogui.center(location_copy)
        pyautogui.doubleClick(center6)
        time.sleep(2)
        pyautogui.hotkey('ctrl','v')
        
open_explorer()
time.sleep(3)
this_pc()
time.sleep(2)
create_and_paste()
'''
os
dbms
cn
sql
oops 1
oops 2
react
javascript
projects
puzzles
html
css
github
'''
