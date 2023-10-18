from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    #находим кнопку. Но срабатывает (и советуют) эту строку ставить перед ожиданием. Когда ставим после ожидания, то долго очень идет
    button = browser.find_element(By.ID, "book") 
    # говорим Selenium проверять в течение 10 секунд, пока текст не станет $100
    price = WebDriverWait(browser, 10).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    button.click()

    x_element = browser.find_element(By.ID, "input_value") #достаём Х
    x = x_element.text
    y = calc(x) # считаем функцию
    browser.find_element(By.ID, "answer").send_keys(y) #вводим ответ в строку
    # прокрутка страницы
    browser.execute_script("window.scrollBy(0, 100)") # scrolling by 100 px
    browser.find_element(By.ID, "solve").click() 
    # печатаем сообщение из алерта в терминал
    #alert_obj = browser.switch_to.alert
    #msg = alert_obj.text
    #print(msg)
    print((browser.switch_to.alert).text) # То же что в предыдущих строках, только без объявления переменной
finally:
    time.sleep(5)
    browser.quit()
