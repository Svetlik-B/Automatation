from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://www.saucedemo.com/")
driver.find_element(By.CSS_SELECTOR, '[name="user-name"]').send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, '[name="login-button"]').click()
driver.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-backpack"]').click()
driver.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
driver.find_element(By.CSS_SELECTOR, '[name="add-to-cart-sauce-labs-onesie"]').click()
driver.find_element(By.CSS_SELECTOR, '#shopping_cart_container').click()
driver.find_element(By.CSS_SELECTOR, '#checkout').click()
driver.find_element(By.CSS_SELECTOR, '[data-test="firstName"]').send_keys("Olga")
driver.find_element(By.CSS_SELECTOR, '[data-test="lastName"]').send_keys("Ivanova")
driver.find_element(By.CSS_SELECTOR, '[data-test="postalCode"]').send_keys("341234")
driver.find_element(By.CSS_SELECTOR, '[data-test="continue"]').click()
txt = driver.find_element(By. CSS_SELECTOR, '[data-test="total-label"]').text

def test_txt():
    assert txt == 'Total: $58.29'