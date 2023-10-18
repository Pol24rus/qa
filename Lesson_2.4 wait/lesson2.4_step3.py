from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/wait1.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(2)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")
    static_message = "Verification was successful!"
   
    assert static_message == message.text, "Сообщение в алерте не то, что надо"

    # assert "successful" in message.text

finally:
    time.sleep(3)
    browser.quit()