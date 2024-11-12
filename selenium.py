from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pandas as pd
from openpyxl import load_workbook


driver_path = r"C:\Users\Saivishal.Vempati\automation\chromedriver.exe" 
service = Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)


url = "https://www.w3schools.com/python/python_ref_keywords.asp"
driver.get(url)

file_name_element = driver.find_element(By.TAG_NAME, 'h1')
file_name_1 = driver.find_element(By.TAG_NAME, 'h1').text
filename_2 = file_name_element.find_element(By.TAG_NAME, 'span').text
filename = file_name_1

rows = driver.find_elements(By.TAG_NAME, 'tr')
data = []


for row in rows:
    columns = row.find_elements(By.TAG_NAME, 'td')
    if len(columns) == 2:  
        col1 = columns[0].text.strip()
        col2 = columns[1].text.strip()
        data.append([col1, col2])


df = pd.DataFrame(data, columns=['Keyword', 'Description'])
excel_filename = f'{filename}.xlsx'
df.to_excel(excel_filename, index=False)


workbook = load_workbook(excel_filename)
sheet = workbook.active

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
for column in sheet.columns:
    max_length = 0
    column = [cell for cell in column]
    for cell in column:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 2)
    sheet.column_dimensions[column[0].column_letter].width = adjusted_width


workbook.save(excel_filename)


driver.quit()
#https://medium.com/@rajshashwatcodes/most-important-algorithms-for-interview-28ece84f8251
