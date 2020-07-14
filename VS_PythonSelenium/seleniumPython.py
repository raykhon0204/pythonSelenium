from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Drivers\\chromedriver.exe')
driver.get("http://amazon.com/")
print(driver.title)
print(driver.current_url) #return the url of the page
#print(driver.page_source) #html code for the page
driver.close()