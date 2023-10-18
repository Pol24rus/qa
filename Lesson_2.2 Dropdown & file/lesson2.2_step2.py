from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # browser.find_elements(By.TAG_NAME, "select").click()
    # browser.find_elements(By.CSS_SELECTOR, "[value='16']").click()

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value("1") # ищем элемент с текстом "Python"

    # select.select_by_visible_text("text") 
    # select.select_by_index(index)

finally:
    time.sleep(5)
    browser.quit()