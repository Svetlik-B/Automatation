# Перейдите на сайт: https://bonigarcia.dev/selenium-webdriver-java/loading-images.html.
# Дождитесь загрузки всех картинок.
# Подсказка
# Это хитрая задачка. Вы можете дождаться появления 4-й картинки или текста Done.
# Получите значение атрибута src у 3-й картинки.
# Выведите значение в консоль.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

wait = WebDriverWait(driver, 10)
wait.until(
    EC.text_to_be_present_in_element ( (By.CSS_SELECTOR,
"#text"), "Done!"))

src = driver.find_element(By.CSS_SELECTOR, "[src='img/award.png']")
png = src.get_attribute("src")

print(png)


