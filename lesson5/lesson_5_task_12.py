from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))



driver.get("http://the-internet.herokuapp.com/login")
sleep(5)
driver.find_element(By.CSS_SELECTOR, '[type="text"]').send_keys("tomsmith")
sleep(2)

driver.find_element(By.CSS_SELECTOR, '[type="password"]').send_keys("SuperSecretPassword!")
sleep(2)

driver.find_element(By.CLASS_NAME, 'radius').click()
sleep(2)