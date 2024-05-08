# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
# Пять раз кликните на кнопку Add Element
# Соберите со страницы список кнопок Delete
# Выведите на экран размер списка.

from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

add_Element = "button"
for x in range(1,6):
    driver.find_element(By.CSS_SELECTOR, add_Element).click()

locator_Delete = "elements"
list = driver.find_elements(By.ID, locator_Delete)
count = len(list)
print(count)

