from selenium import webdriver
from selenium.webdriver.edge.service import Service

s=Service(executable_path="E:\\Driver files\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get('http://www.fb.com')
driver.maximize_window()
title=driver.title
print(title)
url=driver.current_url
print(url)
driver.close()

