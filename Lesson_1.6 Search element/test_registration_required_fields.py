from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    first_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    first_name.send_keys("Ivan")\

    second_name = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    second_name.send_keys("Kuplinov")

    email = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    email.send_keys("kivan@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()
