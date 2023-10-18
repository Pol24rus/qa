from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.remote.webelement import WebElement


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

    input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner") #работает, клик в поле
    #input1 = driver.find_element(By.ID, "feed-add-post-form-tab-message") #вариант Любы (нажатие на кнопку) перестал работать
    input1.click()

    iframe1: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
    driver.switch_to.frame(iframe1)
    
    input2 = driver.find_element(By.TAG_NAME, "body")
    input2.send_keys("Test test? tesT \ новый текст 2")

    driver.switch_to.default_content()

    

    button = driver.find_element(By.ID, "blog-submit-button-save")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла