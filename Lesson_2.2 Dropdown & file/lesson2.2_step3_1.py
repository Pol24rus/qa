from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def sum(x1, y1):
    return str(x1 + y1)

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск цифры 1
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text
    # перевод числа 1 из строки в число
    x1 = int(x)
    print("x1 = ",x1)
    # поиск цифры 2
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    y1 = int(y)
    print("y1=", y1)
    # получить сумму и перевести число в строку
    # z = str(y1 + x1) # это работает
    z = sum(x1, y1)
    print("z=", z)

    # ищем выпадающее меню, кликаем (открываем его)
    # browser.find_element(By.ID, "dropdown").click() # это работает
    # ищу по другому поиску
    select = Select(browser.find_element(By.TAG_NAME, "select")) # можно и так (By.ID, "dropdown")
    select.select_by_visible_text(z) # это работает
    # #select.select_by_value(z) # это работает
 
    # поиск кнопки Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn") #работает
    button.click()

    # select.select_by_visible_text("text") 
    # select.select_by_index(index)

finally:
    time.sleep(5)
    browser.quit()
