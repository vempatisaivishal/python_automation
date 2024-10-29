import pyautogui
import time
import subprocess
import pandas as pd
import pyodbc
import keyboard
def open_chrome():
    print("opening the chrome browser...")
    time.sleep(1)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('Google Chrome', interval=0.1)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)

def open_link(url):
    pyautogui.typewrite(url, interval=0.1)
    time.sleep(3)
    pyautogui.press('enter')
def enter_credentials():
    time.sleep(5)
    pyautogui.typewrite('Venkateshmn@gastrohealth.com')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.typewrite('Marshall$2025')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.press('enter')
def click_ghrx():
    location_ghrx = pyautogui.locateOnScreen('GH_RC.png', confidence=0.6)
    center = pyautogui.center(location_ghrx)
    pyautogui.doubleClick(center)
    time.sleep(2)
def first_enter():
    time.sleep(3)
    pyautogui.hotkey('win', 'e')
    time.sleep(3)
    pyautogui.write('Downloads')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.press('down')
    pyautogui.press('up')
    pyautogui.press('enter')
def credentials_enter(username,password):
    
    try:
        # location_user = pyautogui.locateOnScreen('user.png', confidence=0.8)
        # center = pyautogui.center(location_user)
        # pyautogui.click(center)
        # pyautogui.typewrite(username)
        # time.sleep(5)
        # location_pass = pyautogui.locateOnScreen('pass.png', confidence=0.8)
        # center = pyautogui.center(location_pass)
        # pyautogui.click(center)
        # pyautogui.typewrite(password)
        # time.sleep(5)
        # location_login = pyautogui.locateOnScreen('log.png',confidence=0.8)
        # center = pyautogui.center(location_login)
        # pyautogui.click(center)
        # time.sleep(2)
        keyboard.press("ctrl+a")
        time.sleep(1)
        keyboard.release("ctrl+a")
        pyautogui.typewrite(username)
        time.sleep(2)
        keyboard.press_and_release("tab")
        keyboard.press("ctrl+a")
        time.sleep(1)
        keyboard.release("ctrl+a")
        pyautogui.typewrite(password)
        keyboard.press_and_release("tab")
        keyboard.press_and_release("tab")
        keyboard.press("enter")
        
    except:
        # location_login = pyautogui.locateOnScreen('log.png',confidence=0.8)
        # center = pyautogui.center(location_login)
        # pyautogui.click(center)
        pyautogui.press("enter")
        time.sleep(2)


def location_entry(locations):
    for location in locations:
        try:
            location_loc = pyautogui.locateOnScreen('loc.png', confidence=0.8)
            center = pyautogui.center(location_loc)
            pyautogui.click(center)
            time.sleep(5)
            pyautogui.typewrite(location,interval=0.1)
            #time.sleep(5)
            #pyautogui.moveTo(1220,275)#Point(x=1133, y=338)
            #time.sleep(3)
            #pyautogui.click()
            time.sleep(5)
            # pyautogui.pressEnter()
            # pyautogui.moveTo(1179,249)
            # time.sleep(2)
            # pyautogui.doubleClick()
            # time.sleep(10)
            keyboard.press_and_release("down")
            time.sleep(2)
            keyboard.press_and_release("enter")
            pyautogui.sleep(5)
            location_tot=pyautogui.locateOnScreen('tot1.png', confidence=0.8)
            center = pyautogui.center(location_tot)
            pyautogui.click(center)
            time.sleep(5)
            location_down=pyautogui.locateOnScreen('down.png', confidence=0.8)
            center = pyautogui.center(location_down)
            pyautogui.click(center)
            time.sleep(10)
            location_reports=pyautogui.locateOnScreen('report.png', confidence=0.8)
            center = pyautogui.center(location_reports)
            pyautogui.click(center)
            time.sleep(5)
            location_mytasks=pyautogui.locateOnScreen('mytasks.png', confidence=0.8)
            center = pyautogui.center(location_mytasks)
            pyautogui.click(center)
            time.sleep(5)
        except:
            pass
        

open_chrome()
time.sleep(2)
open_link("https://ghcitrix.cloud.com")
time.sleep(6)
enter_credentials()
time.sleep(8)
click_ghrx()

first_enter()
time.sleep(40)
time.sleep(5)
credentials_enter("Venkateshmn@datamarshall.com", "Marshall$2025")
time.sleep(2)
locations=['LORTON ASC - Inova Ambulatory Surgery Center at LORTON', 'MSC - Inova McLean Surgery Center', 'NVSC - Inova Northern Virginia Surgery Center', 'PWASC - Prince William Ambulatory Surgery Center', 'RSC - RESTON SURGERY CENTER', 'SFASC - Inova Franconia Springfield Ambulatory Surgery Center', 'GHEGC - GHE Gastro Care', 'GHETSEC - GHE Tri State Endoscopy Center', 'FSC - Frederick Surgical Center', 'GDCB - Gastrointestinal Diagnostic Center of Baltimore', 'MDTEC - Maryland Diagnostic and Therapeutic Endo Center', 'GAEC - Gastroenterology Associates Endoscopy Center', 'GHE EDEC - GHE Edmonds Endoscopy Center', 'GHE EGEC - GHE Evergreen Endoscopy Center', 'GHE FEC - GHE Fremont Endoscopy Center', 'GHETCE - GHE Tri Cities Endoscopy Center PLLC', 'BMPSU - Baptist Medical Park Surgery Center', 'TECPEN - The Endoscopy Center of Pensacola', 'ADHEC - Alabama Digestive Health Endoscopy Center', 'GVEC - Grandview Endoscopy Center', 'OSE - Outpatient Services East', 'SASC - Shelby Ambulatory Surgery Center', 'AHSCCLM - AdventHealth Surgery Center Lake Mary', 'AHSCD - AdventHealth Surgery Center Davenport', 'ASC - Atlantic Surgery Center', 'AOC - Atlantis Outpatient Center', 'BAC - Bayside Ambulatory Center', 'BECCS - BHEC Coral Springs', 'CGE - BHEC Flagler', 'GEC - BHEC Galloway North', 'GSC - BHEC Galloway South', 'NPS - BHEC Northpoint', 'BHECPBG - BHEC Palm Beach Gardens', 'BHSFSH - BHEC South Palm', 'BROSLC - Boca Raton OP BROSLC', 'BROSC - Boca Raton OP Surgery and Laser Center', 'BSSC - Broward Specialty Surgical Center', 'CFSC - Central Florida Surgical Center', 'GCEC - Gulf Coast Endoscopy Center South', 'JOSC - Jupiter Outpatient Surgery Center', 'KESC - Kendall Endoscopy Surgery Center', 'KIEC - Kissimmee Endoscopy Center', 'KSC - Kissimmee Surgical Center', 'LSC - Laser and Surgery Center', 'OSS - Outpatient Surgical Services', 'PALMS W SC - Palms W Surgicenter', 'PSC - Parkcreek Surgery Center', 'SLSC - Sand Lake Surgery Center', 'SFSC - South Florida Surgical Center', 'SPSC - Summerport Surgery Center', 'SCCS - Surgery Center at Coral Springs', 'SCOA - Surgery Center Of Aventura', 'TOCBOY - The Outpatient Center of Boynton Beach', 'USC - University Surgery Center', 'VASC - Venture Ambulatory Surgical Center', 'WOSC - Weston Outpatient Surgical Center', 'SCFL - Surgery Center at Ft. Lauderdale']
time.sleep(3)
location_entry(locations)
