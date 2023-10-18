from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # поиск цифр
    a_element = browser.find_element(By.ID, "num1")
    a = a_element.text
    b_element = browser.find_element(By.ID, "num2")
    b = b_element.text
    x = str(int(a) + int(b))
    print("a=",a, "b=",b, "x=",x)
    
    select = Select(browser.find_element(By.TAG_NAME, "select")) # можно и так (By.ID, "dropdown")
    select.select_by_value(x)
    
    # поиск кнопки Submit
    button = browser.find_element(By.CSS_SELECTOR, "button.btn") #работает
    button.click()
 
finally:
    time.sleep(5)
    browser.quit()
