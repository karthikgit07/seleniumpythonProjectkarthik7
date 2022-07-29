from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s=Service(executable_path="E:\\Driver files\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get('http://www.instagram.com')
driver.maximize_window()
title=driver.title
print(title)
url=driver.current_url
print(url)
driver.close()
