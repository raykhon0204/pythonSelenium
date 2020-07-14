from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Drivers\\chromedriver.exe')
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title) 
driver.get("http://amazon.com/")
time.sleep(6)
print(driver.title)
driver.back()
time.sleep(6)

print(driver.title)
driver.forward()
time.sleep(6)

print(driver.title)