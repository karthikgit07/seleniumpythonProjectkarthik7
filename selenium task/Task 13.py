import time

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

s=Service(executable_path="E:\\Driver files\\edgedriver_win64\\msedgedriver.exe")
driver=webdriver.Edge(service=s)
driver.get("https://www.amazon.in/ap/signin?openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.in%2Fgp%2Fyourstore%2Fhome%3Fpath%3D%252Fgp%252Fyourstore%252Fhome%26signIn%3D1%26useRedirectOnSuccess%3D1%26action%3Dsign-out%26ref_%3Dnav_AccountFlyout_signout&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[1]/input[1]").send_keys("7010742551")
driver.find_element(By.ID,"continue").click()
driver.find_element(By.NAME,"password").send_keys("karthik@07")
driver.find_element(By.ID,"signInSubmit").click()
search=driver.find_element(By.XPATH,"//input[@id='twotabsearchtextbox']")
time.sleep(5)
search.click()
time.sleep(5)
search.send_keys("samsung mobile")
time.sleep(5)
list=driver.find_elements(By.XPATH,"/html/body/div[1]/header/div/div[2]/div/div[2]/div")
time.sleep(5)
print(len(list))
time.sleep(5)

for i in list:
    print(i.text)
    if i.text == "samsung mobiles under 15,000+":
        i.click()
        break


driver.execute_script("window.scrollBy(0,1000)")
driver.find_element(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[3]/div[2]/div[6]/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span").click()

parent_window=driver.current_window_handle
child_window=driver.current_window_handle

for i in range(len(child_window)):
    if child_window == parent_window:
       driver.switch_to.window(child_window)
       driver.execute_script("window.scrollBy(0,2000)")
       driver.find_element(By.NAME,"submit.add-to-cart").click()
