# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# import time

# driver_path = r"C:\Users\Saivishal.Vempati\automation\chromedriver.exe"
# service = Service(executable_path=driver_path)
# options = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=service, options=options)

# url = "https://www.bing.com/search?pglt=2083&q=latestest+medics+premier&cvid=ac0c865cb0be4188b166b3e4e8d8370f&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTEzODU3ajBqMagCCLACAQ&FORM=ANSPA1&PC=DCTS"
# driver.get(url)
# time.sleep(2)


# driver.find_element(By.XPATH, '//*[@id="b_results"]/li[2]/div[3]/ul[1]/li[1]/h3').click()
# time.sleep(2)


# original_window = driver.current_window_handle


# all_windows = driver.window_handles


# for window in all_windows:
#     if window != original_window:
#         driver.switch_to.window(window)
#         break

# content = driver.find_element(By.TAG_NAME, 'body').text
# print(content)
# time.sleep(6)

# driver.switch_to.window(original_window)

# time.sleep(6)
# driver.quit()
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

driver_path = r"C:\Users\Saivishal.Vempati\automation\chromedriver.exe"
service = Service(executable_path=driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
url = "https://www.bing.com/search?pglt=2083&q=latestest+medics+premier&cvid=ac0c865cb0be4188b166b3e4e8d8370f&gs_lcrp=EgZjaHJvbWUyBggAEEUYOdIBCTEzODU3ajBqMagCCLACAQ&FORM=ANSPA1&PC=DCTS"
driver.get(url)

time.sleep(2)


folder_path = r"C:\Users\Saivishal.Vempati\medical_websites_info"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

xpaths = [
    '//*[@id="b_results"]/li[2]/div[3]/ul[1]/li[1]/h3',
    '//*[@id="b_results"]/li[2]/div[3]/ul[2]/li[1]/h3',
    '//*[@id="b_results"]/li[2]/div[3]/ul[2]/li[2]/h3',
]


for xpath in xpaths:
    driver.find_element(By.XPATH, xpath).click()
    time.sleep(2)
    
    original_window = driver.current_window_handle
    all_windows = driver.window_handles
    
    for window in all_windows:
        if window != original_window:
            driver.switch_to.window(window)
            break
    heading=driver.find_element(By.TAG_NAME, "h1").text
    heading=driver.find_elements(By.TAG_NAME, "h1")[0].text
    content = driver.find_element(By.TAG_NAME, 'body').text
    file_name = f"{heading}.txt".replace(" ", "_").replace("/", "_")
    file_path = os.path.join(folder_path, file_name)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    #print(content)
    time.sleep(6)
    
    driver.close()
    driver.switch_to.window(original_window)
    time.sleep(2)

driver.quit()
