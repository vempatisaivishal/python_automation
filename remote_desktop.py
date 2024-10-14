import pyautogui
import time
import subprocess

def open_remote_desktop():
    subprocess.Popen(['mstsc'])
    time.sleep(2)

def enter_credentials(username, password):
    pyautogui.typewrite(username) 
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite(password)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('left')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(5)
    
    

def open_chrome():
    pyautogui.press('win')
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.typewrite('http://appstaging.datamarshall.com/q-revoptima/')
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(3)
def place_coordinates():
    pyautogui.moveTo(1047,587)
    time.sleep(2)
    pyautogui.typewrite("vishaltest@dm.com")
    time.sleep(2)
    pyautogui.moveTo(1056,587)
    time.sleep(2)
    pyautogui.click(button=1)
    time.sleep(1)
    pyautogui.moveTo(1042,642)
    time.sleep(2)
    pyautogui.typewrite("Pass@1234")
    time.sleep(2)
    pyautogui.press('enter')
    
    

if __name__ == "__main__":
    open_remote_desktop()
    enter_credentials('172.21.72.116', 'Marshall$25')  
    open_chrome()
    place_coordinates()
