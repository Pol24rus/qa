from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/wait1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    # говорим WebDriver искать каждый элемент в течение 5 секунд
    browser.implicitly_wait(5)
  
    button = browser.find_element(By.ID, "verify")
    button.click()
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text
    time.sleep(3)

finally:
    browser.quit()
