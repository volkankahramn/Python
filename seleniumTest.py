from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
#HTML Locators
driver = webdriver.Chrome()
driver.get("https://www.google.com/")

#sitenin açılmasını bekle
#sleep(20)
input = driver.find_element(By.NAME,"q")
input.send_keys("Deneme")
sleep(3) 
searchBtn = driver.find_element(By.NAME,"btnK")
searchBtn.click()

