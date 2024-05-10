# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
# В модальном окне нажмите на кнопку Сlose

from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(2)
footer_close = "modal-footer"
driver.find_element(By.CLASS_NAME, footer_close).click()
sleep(2)