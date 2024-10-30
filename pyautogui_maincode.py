import pyautogui
import time
import subprocess
import pandas as pd
import pyodbc
import keyboard
import os
from datetime import datetime
start=time.time()
def count_files_in_folder(folder_path):
    file_count = 0
    for root, dirs, files in os.walk(folder_path):
        file_count += len(files)
    return file_count
def open_chrome():
    print("opening the chrome browser...")
    time.sleep(1)
    pyautogui.press('win')
    time.sleep(1)
    pyautogui.typewrite('Google Chrome')
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(3)
def open_link(url):
    pyautogui.typewrite(url)
    time.sleep(3)
    pyautogui.press('enter')
def enter_credentials():
    time.sleep(5)
    pyautogui.typewrite('Venkateshmn@gastrohealth.com')
    pyautogui.press('enter')
    time.sleep(5)
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
        keyboard.press("enter")
        time.sleep(2)
def location_entry(locations):
    for location in locations:
        try:
            location_loc = pyautogui.locateOnScreen('loc.png', confidence=0.8)
            center = pyautogui.center(location_loc)
            pyautogui.click(center)
            time.sleep(5)
            pyautogui.typewrite(location)

            time.sleep(3)

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
            time.sleep(5)
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
def all_download():
    time.sleep(5)
    pyautogui.click()
    down=pyautogui.locateCenterOnScreen('downloads.png',confidence=0.8)
    time.sleep(3)
    pyautogui.click(down)
    keyboard.press_and_release("tab")
    time.sleep(2)
    keyboard.press_and_release("right")
    time.sleep(2)
    keyboard.press_and_release("enter")
    time.sleep(2)
    keyboard.press("ctrl+a")
    time.sleep(5)
    keyboard.release("ctrl+a")
    time.sleep(3)
    keyboard.press("ctrl+c")
    time.sleep(3)
    keyboard.release("ctrl+c")
def paste(destination_folder):
    os.startfile(destination_folder)
    time.sleep(2)
    keyboard.press_and_release("enter")
    time.sleep(5)
    keyboard.press_and_release("ctrl+v")
l = ['LORTON ASC - Inova Ambulatory Surgery Center at LORTON', 'MSC - Inova McLean Surgery Center', 'NVSC - Inova Northern Virginia Surgery Center', 'PWASC - Prince William Ambulatory Surgery Center', 'RSC - RESTON SURGERY CENTER', 'SFASC - Inova Franconia Springfield Ambulatory Surgery Center', 'GHEGC - GHE Gastro Care', 'GHETSEC - GHE Tri State Endoscopy Center', 'FSC - Frederick Surgical Center', 'GDCB - Gastrointestinal Diagnostic Center of Baltimore', 'MDTEC - Maryland Diagnostic and Therapeutic Endo Center', 'GAEC - Gastroenterology Associates Endoscopy Center', 'GHE EDEC - GHE Edmonds Endoscopy Center', 'GHE EGEC - GHE Evergreen Endoscopy Center', 'GHE FEC - GHE Fremont Endoscopy Center', 'GHETCE - GHE Tri Cities Endoscopy Center PLLC', 'BMPSU - Baptist Medical Park Surgery Center', 'TECPEN - The Endoscopy Center of Pensacola', 'ADHEC - Alabama Digestive Health Endoscopy Center', 'GVEC - Grandview Endoscopy Center', 'OSE - Outpatient Services East', 'SASC - Shelby Ambulatory Surgery Center', 'AHSCCLM - AdventHealth Surgery Center Lake Mary', 'AHSCD - AdventHealth Surgery Center Davenport', 'ASC - Atlantic Surgery Center', 'AOC - Atlantis Outpatient Center', 'BAC - Bayside Ambulatory Center', 'BECCS - BHEC Coral Springs', 'CGE - BHEC Flagler', 'GEC - BHEC Galloway North', 'GSC - BHEC Galloway South', 'NPS - BHEC Northpoint', 'BHECPBG - BHEC Palm Beach Gardens', 'BHSFSH - BHEC South Palm', 'BROSLC - Boca Raton OP BROSLC', 'BROSC - Boca Raton OP Surgery and Laser Center', 'BSSC - Broward Specialty Surgical Center', 'CFSC - Central Florida Surgical Center', 'GCEC - Gulf Coast Endoscopy Center South', 'JOSC - Jupiter Outpatient Surgery Center', 'KESC - Kendall Endoscopy Surgery Center', 'KIEC - Kissimmee Endoscopy Center', 'KSC - Kissimmee Surgical Center', 'LSC - Laser and Surgery Center', 'OSS - Outpatient Surgical Services', 'PALMS W SC - Palms W Surgicenter', 'PSC - Parkcreek Surgery Center', 'SLSC - Sand Lake Surgery Center', 'SFSC - South Florida Surgical Center', 'SPSC - Summerport Surgery Center', 'SCCS - Surgery Center at Coral Springs', 'SCOA - Surgery Center Of Aventura', 'TOCBOY - The Outpatient Center of Boynton Beach', 'USC - University Surgery Center', 'VASC - Venture Ambulatory Surgical Center', 'WOSC - Weston Outpatient Surgical Center', 'SCFL - Surgery Center at Ft. Lauderdale']
time.sleep(3)
import glob
import datetime
def rename(locations):
    directory = r"C:\Users\Saivishal.Vempati\gastro_folders"
    report_files = [
        (filename, os.path.getmtime(os.path.join(directory, filename)))
        for filename in os.listdir(directory)
        if  filename.endswith(".csv")
    ]
    report_files.sort(key=lambda x: x[1])
    print(report_files)
    i = 0
    region = ''
    for index, (filename, _) in enumerate(report_files):
        if index < len(locations):
            file_path = os.path.join(directory, filename)
            datemodified = datetime.datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%m%d%Y')
            temp = 'Gl rCX'
            temp1 = 'GHC'
            if(i<7):
                region = 'VA'
            if(i>6 and i<9):
                region = 'OH'
            if(i>8 and i<12):
                region = 'MD'
            if(i>11 and i<17):
                region = 'WA'
            if(i>16 and i<19):
                region = 'FLN'
            if(i>18 and i<23):
                region = 'AL'
            if(i>22 and i<58):
                region = 'FL'
            new_filename = f"{temp1}_{region}_{locations[index]}_{temp}_{datemodified}.csv"
            new_file_path = os.path.join(directory, new_filename)
            os.rename(file_path, new_file_path)
            print(f"Renamed: {filename} to {new_filename}")
        else:
            print(f"Warning: No location for {filename}")
        i+=1
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
path=r'C:\Users\Saivishal.Vempati\gastro_folders'
time.sleep(5)
all_download()
time.sleep(5)
paste(path)
time.sleep(5)
time_taken=True
while time_taken:
    if count_files_in_folder(path)==len(locations):
        rename(l)
        time_taken=False
time.sleep(3)
directory = r"C:\Users\Saivishal.Vempati\gastro_folders"
output_directory = r"C:\Users\Saivishal.Vempati\gastro_folders_xlsx"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)
report_files = [
    (filename, os.path.getmtime(os.path.join(directory, filename)))
    for filename in os.listdir(directory)
    if filename.endswith(".csv")
]
for filename, _ in report_files:
    csv_path = os.path.join(directory, filename)
    excel_path = os.path.join(output_directory, filename.rstrip('.csv') + '.xlsx')
    read_file = pd.read_csv(csv_path)
    read_file.to_excel(excel_path, index=False, header=True)
end=time.time()
print(f"It took this much time {end-start}")
