# Перейдите на сайт: http://uitestingplayground.com/textinput.
# Укажите в поле ввода текст SkyPro.
# Нажмите на синюю кнопку.
# Получите текст кнопки и выведите в консоль (SkyPro).

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/textinput")

entry_field = driver.find_element(By.CSS_SELECTOR, "#newButtonName")
entry_field.send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()


updating = driver.find_element(By.CSS_SELECTOR, ".form-group")
txt = updating.find_element(By. CSS_SELECTOR, "#updatingButton").text
print(txt)