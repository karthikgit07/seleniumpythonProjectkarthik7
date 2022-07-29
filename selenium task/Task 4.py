from selenium.webdriver.common.service import Service
from selenium.webdriver.opera import webdriver

s=Service(executable_path:\\Driver files\\E:\Driver files\operadriver_win64\operadriver_win64\operadriver.exe)
driver=webdriver.OperaDriver(Service=s)
driver.get("http://www.youtube.com")
driver.maximize_window()
title=driver.title
print(title)
url=driver.current_url
print(url)
driver.close()