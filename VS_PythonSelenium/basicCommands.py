from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#Chrome
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Drivers\\chromedriver.exe')
driver.get("http://demo.automationtesting.in/Windows.html")
print(driver.title)
print(driver.current_url)

driver.find_element_by_xpath('/html/body/div[1]/div/div/div/div[2]/div[1]/a/button').click()
time.sleep(5)

driver.quit()
