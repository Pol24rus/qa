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
    
    #Ищу и нажимаю Добавить работников, группы или отделы
    ok = driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption")
    ok.click()
    #Ишу и ввожу Всем работникам 
    element_input = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(1) > div.ui-selector-item > div.ui-selector-item-titles > div.ui-selector-item-title-box > div.ui-selector-item-title"))
        )
    # убираю выпадушку
    element_input.click()
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box"))
        ).click()
    # ищу и нажимаю Отправить. с ожиданием
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "blog-submit-button-save"))
        )
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()
