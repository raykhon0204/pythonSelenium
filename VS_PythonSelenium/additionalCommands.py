from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(executable_path='C:\\Program Files (x86)\\Drivers\\chromedriver.exe')
driver.get("http://gmail.com/")
time.sleep(5)
UserCreate = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[2]/div/div/span/span')
#elem1=driver.find_element_by_name("identifier")

#elem1.send_keys(email)
#next_btn = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/div[2]').click()
UserCreate.click()
menu = driver.find_element_by_class_name('XvhY1d')
time.sleep(3)
menu.find_element_by_xpath('/html/body/div[1]/div[1]/div[2]/div[2]/div/div/span[1]').click()
time.sleep(5)
first = 'test'
last = 'test1'
userName = 'esmatest056'
passwrd = 'Test123456!'

firstName = driver.find_element_by_xpath("//input[@name='firstName']").send_keys(first)
lastName = driver.find_element_by_id('lastName').send_keys(last)
user = driver.find_element_by_id('username').send_keys(userName)
passWord = driver.find_element_by_name('Passwd').send_keys(passwrd)
confirmPass = driver.find_element_by_name('ConfirmPasswd').send_keys(passwrd)
time.sleep(5)
nextButton = driver.find_element_by_id('accountDetailsNext')
nextButton.click()
time.sleep(3)
phoneNumber = driver.find_element_by_id('phoneNumberId').send_keys('347-401-8159')

goNext = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()

