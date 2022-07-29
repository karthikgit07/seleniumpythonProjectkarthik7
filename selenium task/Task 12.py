from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="E:\\Driver files\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://www.rediff.com/")
driver.maximize_window()
driver.implicitly_wait(30)

main_page=driver.find_element(By.XPATH,"//a[@title='Lightning fast business email hosting']").text
print(main_page)