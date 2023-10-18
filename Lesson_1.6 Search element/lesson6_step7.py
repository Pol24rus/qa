# В этой задаче вам нужно заполнить форму (http://suninjuly.github.io/huge_form.html). 
# С помощью неё отдел маркетинга компании N захотел собрать подробную информацию о пользователях своего продукта. 
# В награду за заполнение формы становится доступен код на скидку. Но маркетологи явно переусердствовали, добавив в форму 100 обязательных полей 
# и ограничив время на ее заполнение.
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Ann")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

