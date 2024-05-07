# Откройте страницу http://uitestingplayground.com/dynamicid.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

for x in range(1,4):
    driver.get("http://uitestingplayground.com/dynamicid")
    locator_blue = "btn"
    driver.find_element(By.CLASS_NAME, locator_blue).click()
    sleep(5)
    driver.refresh()


