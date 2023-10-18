from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
       
    # считать значение от Х, ф-ция определена в начале
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print ("y= ", y)

    # вводим ответ на функцию от Х в текстовое поле
    answer_in_field = browser.find_element(By.ID, "answer")
    answer_in_field.send_keys(y)

    # ищем и кликаем чекбокс
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()

    # radiobutton
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    time.sleep(3)

    # финальная кнопка Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
