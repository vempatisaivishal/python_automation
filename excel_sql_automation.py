import pyautogui
import time
import subprocess
import pandas as pd
import pyodbc

def open_sql():
    print("opening the sql server management studio...")
    time.sleep(1)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('SQL Server Management Studio 20', interval=0.2)
    time.sleep(3)
    pyautogui.press('enter')
    time.sleep(5)

def add_credits(password):
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('tab')
    time.sleep(2)
    pyautogui.typewrite(password, interval=0.2)
    time.sleep(2)
    pyautogui.press('tab', presses=4)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(4)

def open_tbl():
    pyautogui.moveTo(40, 185)
    time.sleep(2)
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'n')
    time.sleep(2)

def write_query(dbname, tablename):
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

def export_to_excel(server, database, username, password, query, output_file):
    conn_str = (
        f'DRIVER={{ODBC Driver 17 for SQL Server}};'
        f'SERVER={server};'
        f'DATABASE={database};'
        f'UID={username};'
        f'PWD={password}'
    )
    conn = pyodbc.connect(conn_str)
    df = pd.read_sql(query, conn)
    df.to_excel(output_file, index=False)
    print("Query results exported to Excel successfully!")


open_sql()
add_credits('Code@123')
open_tbl()
time.sleep(2)
write_query("Batch_003", "TblVishal")
new_query("select * from TblVishal order by FirstName desc")


export_to_excel(
    server='***********',
    database='Batch_003',
    username='appuser',
    password='**********',
    query='select * from TblVishal order by FirstName desc',
    output_file='query_results.xlsx'
)
