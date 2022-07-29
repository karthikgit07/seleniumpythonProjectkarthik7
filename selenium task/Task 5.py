import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

s=Service(executable_path='E:\\Driver files\\edgedriver_win64\\msedgedriver.exe')
driver=webdriver.Edge(service=s)
driver.get("https://demo.guru99.com/test/newtours/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,'Register here').click()
driver.find_element(By.NAME,'firstName').send_keys('Karthik')
driver.find_element(By.NAME,'lastName').send_keys('Ramachandran')
driver.find_element(By.NAME,'phone').send_keys('7010742551')
driver.find_element(By.ID,'userName').send_keys('krkarthik07@gmail.com')
driver.find_element(By.NAME,'address1').send_keys('26 Lingappan palayam street,Pilliyar palayam')
driver.find_element(By.NAME,'city').send_keys('Kanchipuram')
driver.find_element(By.NAME,'state').send_keys('Tamilnadu')
driver.find_element(By.NAME,'postalCode').send_keys('631501')
driver.find_element(By.NAME,'country').send_keys('India')
driver.find_element(By.NAME,'email').send_keys('krkarthik07@gmail.com')
driver.find_element(By.NAME,'password').send_keys('kar@123')
driver.find_element(By.NAME,'confirmPassword').send_keys('kar@123')
time.sleep(15)
driver.close()
