from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/cats.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)

    browser.find_element(By.ID, "button")
  
    time.sleep(3)

finally:
    browser.quit()
