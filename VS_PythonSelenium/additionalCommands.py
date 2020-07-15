from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Drivers\\chromedriver.exe')
driver.get("http://gmail.com/")
elem1=driver.find_element_by_xpath("/html/body")
time.sleep(5)
email = 'raykhon.juraeva@gmail.com'
elem1.send_keys(email)

next_btn = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()



