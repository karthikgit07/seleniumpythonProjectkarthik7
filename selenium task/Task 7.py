from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path='E:\\Driver files\\chromedriver_win32 (1)\\chromedriver.exe')
driver=webdriver.Chrome(service=s)
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[starts-with(@name,'nam')]").send_keys("Karthik")
driver.find_element(By.XPATH,"//input[starts-with(@name,'log')]").send_keys("karthik07225")
driver.find_element(By.XPATH,"//input[starts-with(@name,'btnc')]").click()
driver.find_element(By.XPATH,"//input[starts-with(@name,'pass')]").send_keys("admin@123")
driver.find_element(By.XPATH,"//input[starts-with(@name,'con')]").send_keys("admin@123")
driver.find_element(By.XPATH,"//input[starts-with(@name,'alt')]").send_keys("mahi07@rediffmail.com")
driver.find_element(By.XPATH,"//input[starts-with(@id,'mobno')]").send_keys("7010742553")
