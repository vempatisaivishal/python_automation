import pyautogui
import time
import subprocess
import pandas as pd
import pyodbc

def open_medics():
    print("opening the medics premier...")
    time.sleep(1)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('Medics Premier', interval=0.1)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)

def click_medics():
    try:
        location_exit= pyautogui.locateOnScreen('screen1.png')
        location_cross= pyautogui.locateOnScreen('screen2.png')
        
    except Exception:
        print(Exception)
        location_cross=False
        
    finally:
        pass
    if location_cross:
        center_cross= pyautogui.locateOnScreen('screen2.png')
        pyautogui.click(center_cross)
        time.sleep(2)
        center_cancel=pyautogui.locateOnScreen('screen3.png')
        pyautogui.click(center_cancel)
        time.sleep(2)
        if location_exit:
            center = pyautogui.center(location_exit)
            pyautogui.click(center)
    elif location_exit:
        center = pyautogui.center(location_exit)
        pyautogui.click(center)
    else:
        print("Image not found on the screen.")

open_medics()
time.sleep(2)
click_medics()
