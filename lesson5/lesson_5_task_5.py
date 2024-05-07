# Откройте страницу http://the-internet.herokuapp.com/inputs.
# Введите в поле текст 1000
# Очистите это поле (метод clear).
# Введите в это же поле текст 999


from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

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