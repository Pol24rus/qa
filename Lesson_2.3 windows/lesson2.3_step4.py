from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    # Нажать на кнопку
    fst_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    fst_button.click()

    #принять confirm кнопку в алерте
    confirm = browser.switch_to.alert
    confirm.accept()
    # time.sleep(1)

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    x_element = browser.find_element(By.ID, "input_value") #достаём Х
    x = x_element.text
    answer = calc(x) # считаем функцию
    # print("y=", answer)
    answer_field = browser.find_element(By.ID, "answer") #вводим ответ в строку
    answer_field.send_keys(answer)
    scnd_button = browser.find_element(By.CSS_SELECTOR, "button.btn") # или (By.CSS_SELECTOR, "button, disabled") по значению аргумента #нажимаем вторую кнопку Submit
    scnd_button.click()
   

finally:
    # успеваем скопировать код за 5 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
