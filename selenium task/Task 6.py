import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path='E:\\Driver files\\chromedriver_win32 (1)\\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://demo.guru99.com/test/newtours/register.php")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@name='firstName']").send_keys("Karthik")
driver.find_element(By.XPATH,"//input[@name='lastName']").send_keys("Ramachandran")
driver.find_element(By.XPATH,"//input[@name='phone']").send_keys("7010742551")
driver.find_element(By.XPATH,"//input[@id='userName']").send_keys("krkarthik07@gmail.com")
driver.find_element(By.XPATH,"//input[@name='address1']").send_keys("26 Lingappan palayam street,pilliyar palayam")
driver.find_element(By.XPATH,"//input[@name='city']").send_keys("Kanchipuram")
driver.find_element(By.XPATH,"//input[@name='state']").send_keys("Tamilnadu")
driver.find_element(By.XPATH,"//input[@name='postalCode']").send_keys("631501")
driver.find_element(By.XPATH,"//select[@name='country']").send_keys("India")
driver.find_element(By.XPATH,"//input[@id='email']").send_keys("krkarthik07@gmail.com")
driver.find_element(By.XPATH,"//input[@name='password']").send_keys("kar1234")
driver.find_element(By.XPATH,"//input[@name='confirmPassword']").send_keys("kar1234")
time.sleep(10)
driver.close()