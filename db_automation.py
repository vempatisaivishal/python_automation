import pyautogui
import time
import subprocess
def open_sql():
    print("opening the sql server management studio...")
    time.sleep(1)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('SQL Server Management Studio 20',interval=0.2)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(5)
def add_credits(password):
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.typewrite(password,interval=0.2)
    time.sleep(2)
    pyautogui.press('tab',presses=4)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)
def open_tbl():
    pyautogui.moveTo(40,185)
    time.sleep(2)
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey('ctrl','n')
    time.sleep(2)
    # pyautogui.scroll(-1500)
    # time.sleep(2)
    # pyautogui.moveTo(59,889)
    # time.sleep(2)
    # pyautogui.click()
    # time.sleep(4)
    # pyautogui.moveTo(77,817)
    # time.sleep(2)
    # pyautogui.click()
    # time.sleep(3)
    # pyautogui.moveTo(159,921)
    # time.sleep(2)
    # pyautogui.click(button="right")
    # time.sleep(3)
    # pyautogui.moveTo(251,630)
    # time.sleep(2)
    # pyautogui.click()
    # time.sleep(2)
def write_query(dbname,tablename):
    pyautogui.write(f"use {dbname};")
    time.sleep(2)
    pyautogui.press('enter')
    pyautogui.write(f"select * from {tablename};")
    pyautogui.press('enter')
    pyautogui.hotkey('f5')
def new_query(n_q):
    pyautogui.write(f'{n_q};')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.hotkey('f5')    
    
        
open_sql()    
add_credits('Code@123')    
open_tbl()
time.sleep(2)
write_query("Batch_003","TblVishal")
new_query(
    '''select * from TblVishal order by FirstName desc''' 
)
#Batch_003
#TblVishal
