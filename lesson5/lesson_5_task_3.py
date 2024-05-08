# Откройте страницу http://uitestingplayground.com/classattr.
# Кликните на синюю кнопку.
# Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# for x in range(1,4):
driver.get("http://uitestingplayground.com/classattr")
locator_blue2 = "btn-primary"
driver.find_element(By.CLASS_NAME, locator_blue2).click()
sleep(2)
driver.switch_to.alert.accept()
driver.refresh()

    

