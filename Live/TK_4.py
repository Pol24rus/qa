"""Отправка сообщения всем в Живой ленте"""
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.remote.webelement import WebElement

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from datetime import datetime
import unittest


link = "https://intranet-test.roslesinforg.ru/stream/"

try:
    driver = webdriver.Chrome()
    driver.get(link)
    driver.maximize_window()

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
    # ok = driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption")
    ok = driver.find_element(By.XPATH, '(//span[@class="ui-tag-selector-add-button-caption"])[1]')
    ok.click()
    #Ишу и ввожу Всем работникам 
    # element_input = WebDriverWait(driver, 5).until(
    #     EC.element_to_be_clickable((By.CSS_SELECTOR, "div:nth-child(1) > div.ui-selector-item > div.ui-selector-item-titles > div.ui-selector-item-title-box > div.ui-selector-item-title"))
    #     )
    # локатор по CSS

    # убираю выпадушку
    element_input = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//div[text()='Всем работникам']")))
    # поиск по части текста по X-path
    element_input.click()
    # убираю выпадушку
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box"))
        ).click()
    # ищу и нажимаю Отправить. с ожиданием
    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "blog-submit-button-save"))
        )
    button.click()

    # Проверка. находим элемент, содержащий текст
    # actual_text3 = driver.find_element(By.XPATH, '(//div[@class="feed-post-text"])[1]').text
    # поиск по классу
    # actual_text2 = driver.find_element(By.XPATH, "//span[contains(text(), 'С сообщением ознакомлен')]").text
    # поиск по части текста

    # actual_text4 = driver.find_element(By.XPATH, '(//div[@class="feed-post-text-block-inner-inner"]/div[@class="feed-post-text"])[1]/text()[1]').text
    # actual_text4 = driver.find_element(By.XPATH, '//div[@class="feed-post-text"][1]/text()[1]').text
    # в этом месте дает ошибку. проверка поиска для сборного файла import_unittest
    # попробую найти в списке Кому
    actual_text4 = driver.find_element(By.XPATH, '/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/div/div[2]/div/div[4]/div[3]/div[1]/div/div[1]/div[3]/span/span[2]').text

    print("actual text 4 - ", actual_text4)
    needed_text = "Всем работникам"
    assert actual_text4 == needed_text
    # self.assertEqual(needed_text, actual_text4, "Не тот текст")
    print("Good")

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    # driver.quit()
