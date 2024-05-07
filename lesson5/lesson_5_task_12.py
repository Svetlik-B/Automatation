from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
sleep(1)
username = '[type="text"]'
enter_name = driver.find_element(By.CSS_SELECTOR, username)
enter_name.send_keys("tomsmith")
password = '[type="password"]'
sleep(1)

enter_password = driver.find_element(By.CSS_SELECTOR, password)
enter_password.send_keys("SuperSecretPassword!")
sleep(1)

login = 'radius'
driver.find_element(By.CLASS_NAME, login).click()

