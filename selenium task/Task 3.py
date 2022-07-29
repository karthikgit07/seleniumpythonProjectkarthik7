from selenium import webdriver
from selenium.webdriver.firefox.service import Service

s=Service(executable_path="E:/Driver files/geckodriver-v0.31.0-win64/geckodriver.exe")
driver=webdriver.Firefox(service=s)
driver.get('http://www.gmail.com')
driver.maximize_window()
title=driver.title
print(title)
url=driver.current_url
print(url)
driver.close()