from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # тест отрабатывает на обоих страницах
  
    input1 = browser.find_element(By.CSS_SELECTOR, ".first_class > input")
    input1.send_keys("Pol")
    # input1 = browser.find_element(By.CSS_SELECTOR, ".first_block > .first_class > input")
    # input1.send_keys("Pol")
    input2 = browser.find_element(By.CSS_SELECTOR, ".second_class > .second")
    input2.send_keys("24rus")
    # input3 для версии 1, где три поля обязательных, срабатывает и на 2-й 
    input3 = browser.find_element(By.CSS_SELECTOR, ".third_class > .third")
    input3.send_keys("Smolensk")

    time.sleep(2)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()