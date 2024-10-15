from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
url = "https://ui.vision/demo/webtest/frames/"
driver.get(url)
driver.fullscreen_window()
time.sleep(1)
def frame_1(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH,'//*[@id="id1"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        print(f"Filled {input_name} with value: {input_value}")
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        driver.switch_to.default_content()

def frame_2(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH,'//*[@id="id2"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        print(f"Filled {input_name} with value: {input_value}")
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        driver.switch_to.default_content()
def frame_3(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH, '//*[@id="id3"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        print(f"Filled {input_name} with value: {input_value}")
        
        
        r = driver.find_element(By.XPATH, '/html/body/center/iframe')
        driver.switch_to.frame(r)

        
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="i5"]'))).click()
        
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="i22"]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[1]/div[1]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[2]/div[3]').click()
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div[1]/div[1]/div/span').click()
        time.sleep(2)
        z=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        z.clear()
        z.send_keys("hey hello")
        time.sleep(2)
        ab=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[2]/div[3]/div/div/div[2]/div/div[1]/div[2]/textarea')
        ab.clear()
        ab.send_keys("oh hi")
        time.sleep(2)
        driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div[1]/div[3]/div[1]/div[1]/div[2]/span').click()
        time.sleep(2)
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        driver.switch_to.default_content()

def frame_4(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH,'//*[@id="id4"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        print(f"Filled {input_name} with value: {input_value}")
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        driver.switch_to.default_content()
def frame_5(frame_src, input_name, input_value):
    driver.switch_to.frame(driver.find_element(By.XPATH, f'//frame[@src="{frame_src}"]'))
    try:
        input_field = driver.find_element(By.XPATH,'//*[@id="id5"]/div/input')
        input_field.clear()
        input_field.send_keys(input_value)
        time.sleep(1)
        driver.find_element(By.XPATH,'/html/body/center/a').click()
        time.sleep(1)
        print(f"Filled {input_name} with value: {input_value}")
    except Exception as e:
        print(f"Error filling input {input_name}: {e}")
    finally:
        pass
frame_1("frame_1.html", "mytext1", "Value for mytext1")
time.sleep(1)
frame_2("frame_2.html", "mytext2", "Value for myText2")
time.sleep(1)
frame_3("frame_3.html", "mytext3", "Value for myText3")
time.sleep(1)
frame_4("frame_4.html", "mytext4", "Value for myText4")
time.sleep(1)
frame_5("frame_5.html", "mytext5", "Value for myText5")
time.sleep(2)
driver.quit()
