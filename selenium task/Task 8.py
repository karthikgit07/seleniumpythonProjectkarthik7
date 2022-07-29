from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="E:\\Driver files\\chromedriver_win32 (1)\\chromedriver.exe")
driver=webdriver.Chrome(service=s)
driver.get("https://register.rediff.com/register/register.php?FormName=user_details")
driver.maximize_window()
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[3]/td[3]/input").send_keys("Karthik Ramachandran")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[7]/td[3]/input").send_keys("karthik07225")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[9]/td[3]/input").send_keys("Admin@123")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[11]/td[3]/input").send_keys("Admin@123")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[14]/td/div/table/tbody/tr/td[3]/input").send_keys("mahi07@rediffmail.com")
driver.find_element(By.XPATH,"/html/body/center/form/div/table[2]/tbody/tr[20]/td/div/table/tbody/tr/td[3]/div[3]/input").send_keys("7010742558")

