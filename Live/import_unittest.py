# тест включает ТКейсы №№2, 3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import datetime
from datetime import datetime
import unittest


link = "https://intranet-test.roslesinforg.ru/stream/"
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
input_txt = datetime.now() #переменная, вставляю в текст, чтобы текст был разный
# print("data=", input_txt)

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        
        input1_3 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner") #работает, клик в поле
        input1_3.click()
        # текст сообщения
        iframe1: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
        driver.switch_to.frame(iframe1)
        input2_1 = driver.find_element(By.TAG_NAME, "body")
        input2_1.send_keys("Тест сообщение двум, от ", str(input_txt))
        driver.switch_to.default_content()

        #Ищу и нажимаю Добавить ещё
        ok = driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption")
        ok.click()
        # ищу и ввожу Поладько и Отдел кадров
        element_input = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box"))
            )
        time.sleep(1)
        element_input.send_keys("Поладько")
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(1)
        element_input.send_keys("Отдел")
        time.sleep(1)
        element_input.send_keys(Keys.ENTER)
        time.sleep(2)
        # убираю Всем работникам
        # driver.find_element(By.CSS_SELECTOR, "div.ui-tag-selector-tag-remove").click()
        button = driver.find_element(By.ID, "blog-submit-button-save")
        button.click()
        # находим элемент, содержащий текст
        welcome_text = driver.find_element(By, "h1").text
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        needed_text = "Тест сообщение двум, от ", str(input_txt)        
        self.assertEqual(welcome_text, needed_text, "No text")

    # def test_abs2(self):
    #     # TK_3
    #     driver.find_element(By.ID, "feed-add-post-form-link-text").click()
    #     # нахожу "Важное сообщение"
    #     driver.find_element(By.CSS_SELECTOR, "span.menu-popup-item.menu-popup-no-icon.feed-add-post-form-important.feed-add-post-form-important-more > span.menu-popup-item-text").click()
    #     # текст сообщения
    #     iframe1: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
    #     driver.switch_to.frame(iframe1)
    #     # ? почему не видит input из 1-й функции ?
    #     input2_2 = driver.find_element(By.TAG_NAME, "body")
    #     input2_2.send_keys("Тест на Важное сообщение от ", str(input_txt))
    #     driver.switch_to.default_content()
    #
    #     #driver.implicitly_wait(5) # не работает
    #     #Ищу и нажимаю Добавить ещё
    #     ok = driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption") #ok Обозначал ранее
    #     ok.click()
    #     # ищу и ввожу Поладько и Отдел кадров
    #     element_input = WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box"))
    #         )
    #     time.sleep(1)
    #     element_input.send_keys("Поладько")
    #     time.sleep(1)
    #     element_input.send_keys(Keys.ENTER)
    #     time.sleep(1)
    #     element_input.send_keys("Отдел")
    #     time.sleep(1)
    #     element_input.send_keys(Keys.ENTER)
    #     # убираю Всем работникам
    #     driver.find_element(By.CSS_SELECTOR, "div.ui-tag-selector-tag-remove").click()
    #
    #     button = driver.find_element(By.ID, "blog-submit-button-save")
    #     button.click()

        if __name__ == "__main__":
            unittest.main()
            # print("All tests passed!")



# не забываем оставить пустую строку в конце файла