from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"

try: 
    browser = webdriver.Chrome()
    browser.get(link)

    # ! убрать футер
    # foot = browser.find_element(By.TAG_NAME, "footer")
    # browser.execute_script('arguments[0].style.visibility = \'hidden\'', foot)
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
    print("y=",y)
    # ввожу результаты расчета в строку ответа
    x_string = browser.find_element(By.ID, "answer").send_keys(y)
    # #x_string.send_keys(y) #если скролить и скрывать не надо, то можно перенести и вставить в строку выше
    # нахожу чек-бокс
    check_box = browser.find_element(By.CSS_SELECTOR, "label[for=robotCheckbox]").click()
    # #check_box.click() #если скролить и скрывать не надо, то можно перенести и вставить в строку выше
    # нахожу радиокнопку
    radio_btn = browser.find_element(By.ID, "robotsRule")
    # прокрутка страницы
    browser.execute_script("window.scrollBy(0, 100);", radio_btn) # scrolling by 100 px
    radio_btn.click()
    # button Submit
    final_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    final_btn.click()
    # ! копирует число из алерта в консоль
    print("answer=", browser.switch_to.alert.text.split()[-1])

finally:
    time.sleep(5)
    browser.quit()
