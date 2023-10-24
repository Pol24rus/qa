from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from datetime import datetime


link = "https://intranet-test.roslesinforg.ru/stream/"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # авторизация
    login = driver.find_element(By.ID, "USER_LOGIN")
    login.send_keys("OK_RLI")
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys("OK_RLIOK_RLI")
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    #time.sleep(1)

    input_txt = datetime.now()
    # print("data=", input_txt)

    input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner") # клик в поле
    input1.click()
    # текст сообщения
    iframe1: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
    driver.switch_to.frame(iframe1)
    input2 = driver.find_element(By.TAG_NAME, "body")
    input2.send_keys("Отправка сообщения всем работникам \nТест от ", str(input_txt))
    driver.switch_to.default_content() 
    
    # ищу и нажимаю Отправить. с ожиданием
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "blog-submit-button-save"))
        )
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
