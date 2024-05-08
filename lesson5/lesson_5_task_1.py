# Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
# Пять раз кликните на кнопку Add Element
# Соберите со страницы список кнопок Delete
# Выведите на экран размер списка.

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(5)

locator_Add_Element = "button"
for x in range(1,6):
    driver.find_element(By.TAG_NAME, locator_Add_Element).click()
sleep(10)

locator_Delete = "added-manually"
list = driver.find_elements(By.CLASS_NAME, locator_Delete)
count = len(list)
print(count)