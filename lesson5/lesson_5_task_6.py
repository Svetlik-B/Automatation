# Откройте страницу http://the-internet.herokuapp.com/login.
# В поле username введите значение tomsmith
# В поле password введите значение 
# SuperSecretPassword!
# Нажмите кнопку Login

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/login")
sleep(5)
username = '[type="text"]'
enter_name = driver.find_element(By.CSS_SELECTOR, username)
enter_name.send_keys("tomsmith")
password = '[type="password"]'
sleep(2)

enter_password = driver.find_element(By.CSS_SELECTOR, password)
enter_password.send_keys("SuperSecretPassword!")
sleep(2)

login = 'radius'
driver.find_element(By.CLASS_NAME, login).click()
sleep(2)