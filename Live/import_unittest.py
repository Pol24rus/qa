# тест включает ТКейсы №№2, 3
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from datetime import datetime
import unittest

link = "https://intranet-test.roslesinforg.ru/stream/"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
g = Service()
driver = webdriver.Chrome(options=options, service=g)
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
input_txt = datetime.now()  #переменная, вставляю в текст, чтобы текст был разный


class TestAbs(unittest.TestCase):
    def test_abs1(self):
        input1_3 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner")  #работает, клик в поле
        input1_3.click()
        # текст сообщения
        iframe1: WebElement = driver.find_element(By.CSS_SELECTOR,
                                                  "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled"
                                                  "-iframe-cnt > iframe")
        driver.switch_to.frame(iframe1)
        input2_1 = driver.find_element(By.TAG_NAME, "body")
        input2_1.send_keys("Тест сообщение двум, от ", str(input_txt))
        input2_2 = input2_1.text
        # print("input =", input2_2)
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
        time.sleep(1)
        element_input.click()
        # клик в Отправить
        button = driver.find_element(By.ID, "blog-submit-button-save")
        button.click()
        time.sleep(3)
        # находим элемент, содержащий текст
        actual_text = driver.find_element(By.XPATH, '(//*[@class="feed-post-text"])[1]').text
        # needed_text = "22Тест сообщение двум, от ",str(input_txt)  # ответ приходит со скобками и запятой,
        # отличается. Видимо из-за того, что в 45-й строке отправляется текст со значением (value)
        """Для сравнения брал переменную (текст) который вкладывал в поле (стр 46), и сравнивал с тем, что прочел в
        Живой ленте. Корректно ли это? С другой стороны, вкладывать это одно, но не факт что оно же и возьмется потом
        с итоговой страницы"""
        # print("выходное значение (сообщение двоим =", input2_2)
        needed_text = input2_2
        self.assertEqual(needed_text, actual_text, "Не тот текст")

    def test_abs2(self):
        # TK_3
        driver.find_element(By.ID, "feed-add-post-form-link-text").click()
        # нахожу "Важное сообщение" три варианта локаторов, CSS, X-Path, кастомный X-Path.
        # В последнем можно пробовать ставить индекс = 21
        # driver.find_element(By.CSS_SELECTOR, "span.menu-popup-item.menu-popup-no-icon.feed-add-post-form-important.feed-add-post-form-important-more > span.menu-popup-item-text").click()
        # driver.find_element(By.XPATH, '//*[@id="popup-window-content-menu-popup-feed-add-post-form-popup"]/div/div/span[3]/span[2]').click()
        driver.find_element(By.XPATH, '(//span[@class="menu-popup-item-text"])[3]').click()
        # текст сообщения
        iframe1: WebElement = driver.find_element(By.CSS_SELECTOR,
                                                  "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
        driver.switch_to.frame(iframe1)
        input3_1 = driver.find_element(By.TAG_NAME, "body")
        input3_1.send_keys("Тест на Важное сообщение от ", str(input_txt))
        # input3_2 = input3_1.text
        # print("input =", input3_2)
        driver.switch_to.default_content()

        #driver.implicitly_wait(5) # не работает
        #Ищу и нажимаю Кому
        ok = driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption")  #ok Обозначал ранее
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
        element_input.click()  # клик в выпадушку, чтобы убрать его
        time.sleep(1)
        # нажимаю Отправить
        button = driver.find_element(By.ID, "blog-submit-button-save")
        button.click()

        # driver.find_element(By.XPATH, '//div[@class ="feed-important-icon"]')  # зеленая иконка "i" что важное

        # находим элемент, содержащий текст
        actual_text2 = driver.find_element(By.XPATH, '//span[@class="feed-imp-post-footer-message"]').text
        # print("actual text 2 - ", actual_text2)
        needed_text = "С сообщением ознакомлен"
        self.assertEqual(needed_text, actual_text2, "Не тот текст")


if __name__ == "__main__":
    unittest.main()
    # print("All tests passed!")

# не забываем оставить пустую строку в конце файла
