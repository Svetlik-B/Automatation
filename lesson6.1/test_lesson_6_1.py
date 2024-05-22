from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys("Иван")
driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys("Петров")
driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys("Ленина, 55-3")
driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys("test@skypro.com")
driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys("+7985899998787")
driver.find_element(By.CSS_SELECTOR, '[name="zip-code"]')
driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys("Москва")
driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys("Россия")
driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys("QA")
driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys("SkyPro")
driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

not_text = driver.find_element(By.CSS_SELECTOR, '[class="alert py-2 alert-danger"]')
color_red = not_text.value_of_css_property("color")

text = driver.find_element(By.CSS_SELECTOR, '[class="alert py-2 alert-success"]')
color_green = text.value_of_css_property("color")

def test_red():
    print(color_red)
    assert color_red == 'rgba(132, 32, 41, 1)'

def test_green():
    print(color_green)
    assert color_green == 'rgba(15, 81, 50, 1)'