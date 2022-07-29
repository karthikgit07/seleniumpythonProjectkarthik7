import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="E:\\Driver files\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("http://www.flipkart.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input").send_keys("9952221587")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input").send_keys("karthik@07")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input").send_keys("iphone")
time.sleep(5)
list_1=driver.find_elements(By.XPATH,"/html/body/div/div/div[1]/div[1]/div[2]/div[2]/form/ul/li")
time.sleep(5)
print(len(list_1))
time.sleep(10)

for i in list_1:
    print(i.text)
    if i.text == "iphone 13 pro max":
        i.click()
        break
time.sleep(10)

driver.execute_script("window.scrollBy(0,1300)")
driver.find_element(By.XPATH,"/html/body/div/div/div[3]/div[1]/div[2]/div[6]/div/div/div/a").click()


