from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")
sleep(2)
nunber = "[type='number']"
entry_field = driver.find_element(By.CSS_SELECTOR, nunber)
entry_field.send_keys("1000")
sleep(2)
entry_field.clear()
sleep(2)
entry_field.send_keys("999")
sleep(2)