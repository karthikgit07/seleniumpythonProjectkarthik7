from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

s=Service(executable_path="E:\\Driver files\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"//a[starts-with(@id,'u_0_0')]").click()
driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Karthik")
driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("Ram")
driver.find_element(By.XPATH,"//input[@name='reg_email__']").send_keys("9952221500")
driver.find_element(By.XPATH,"//input[@autocomplete='new-password']").send_keys("Admin@123")
day=driver.find_element(By.ID,"day")
sel=Select(day)
sel.select_by_value("11")
birth_month=driver.find_element(By.NAME,"birthday_month")
sel=Select(birth_month)
sel.select_by_value("3")
year=driver.find_element(By.ID,"year")
sel=Select(year)
sel.select_by_value("1995")
driver.find_element(By.XPATH,"//input[@value='2']").click()


