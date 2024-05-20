from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.find_element(By.CSS_SELECTOR, '#delay').clear()
driver.find_element(By.CSS_SELECTOR, '#delay').send_keys("4")
bt_7 = driver.find_element(By.XPATH,"//span[contains(., '7')]").click()
plus = driver.find_element(By.XPATH,"//span[contains(., '+')]").click()
bt_8 = driver.find_element(By.XPATH,"//span[contains(., '8')]").click()
sum = driver.find_element(By.XPATH,"//span[contains(., '=')]").click()
driver.find_element(By.CSS_SELECTOR,".screen")
wait = WebDriverWait(driver, 5)
wait.until(EC.text_to_be_present_in_element ((By.CSS_SELECTOR,".screen"), "15"))
result = driver.find_element(By. CSS_SELECTOR, ".screen").text
time = driver.find_element(By.CSS_SELECTOR, '#delay')
info_time = time.get_attribute("value")

def test_calculator():
    assert result == "15" and info_time == '4'
