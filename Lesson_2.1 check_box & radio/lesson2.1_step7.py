from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # 2. Найти элемент-картинку, который является изображением сундука с сокровищами.
    # picture_elem = browser.find_element(By.ID, "treasure")
    # 3. Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
    x_element = browser.find_element(By.ID, "treasure")
    x = x_element.get_attribute("valuex")
    # x_checked = x_element.get_attribute("valuex")
    # x = x_checked
    print("x = ", x)
    # 4. Посчитать математическую функцию от x (сама функция остаётся неизменной)
    y = calc(x)
    print ("y= ", y)
    # 5. Ввести ответ в текстовое поле.
    answer_in_field = browser.find_element(By.ID, "answer")
    answer_in_field.send_keys(y)
    # 6. Отметить checkbox "I'm the robot".
    option1 = browser.find_element(By.ID, "robotCheckbox")
    option1.click()
    # 7. Выбрать radiobutton "Robots rule!".
    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    time.sleep(2)
    # 8. Нажать на кнопку "Submit".
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
