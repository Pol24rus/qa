# добавить файлв комментарий
import os

import self
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
# import datetime
from datetime import datetime

link = "https://intranet-test.roslesinforg.ru/stream/"

try:
    driver = webdriver.Chrome()
    driver.get(link)

    # авторизация
    login = driver.find_element(By.ID, 'USER_LOGIN')
    login.send_keys("OK_RLI")
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys("OK_RLIOK_RLI")
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    # time.sleep(1)
    """данный кейс ставить Желательно после ТК_5 (редактирование сообщения), чтобы находить и редактировать сообщение, а не задачи и тд."""
    """Для редактирования необходимо открывать фрейм (?) """
    # ввожу дату и время, чтобы получить уникальность сообщения
    input_txt = datetime.now()
    # TK_13 (add file in comment)
    # нахожу поле комментария, кликаю сразу в него, не нажимая кнопку Коментировать
    comment_field = driver.find_element(By.XPATH, "(//a[@class='feed-com-add-link'])[1]")
    comment_field.click()

    # iframe13: WebElement = driver.find_element(By.XPATH, "//iframe[@class='bx-editor-iframe']")
    # driver.switch_to.frame(iframe13)
    # # input13 = driver.find_element(By.XPATH, "//body[@contenteditable='true']")
    # # input13.send_keys("Adding file")
    # # input13.send_keys()
    # driver.switch_to.default_content()

    """Попробовать использовать: element = browser.find_element(By.CSS_SELECTOR, "[type='file']")"""
    """если не найду способ вложить файл, то как вариант открыть окно выбора вкладываемого файла изайти в историю, 
    там перебрать стрелкой вниз. Попробовать тупо ввести любой символ, потом стрелкой перебрать историю, авось?"""
    """Ещё один фрейм? - нет, не получилось открыть"""
    # iframe13_2: WebElement = driver.find_element(By.XPATH, "(//iframe[@class='bx-editor-iframe'])[2]")
    # driver.switch_to.frame(iframe13_2)
    time.sleep(2)
    """нажимаю кнопку Файл"""
    # input13_file1 = driver.find_element(By.XPATH, "(//div[@id='mpf-file-blogCommentFormsp1g]/span')")  # не работает
    # input13_file1 = driver.find_element(By.XPATH, "(//div[@id='mpf-file-blogCommentFormsp1g]/i')")  # не работает
    # input13_file1 = driver.find_element(By.ID, "bx-b-uploadfile-blogCommentFormsp1g")  # не работает
    input13_file1 = driver.find_element(By.XPATH, "(//div[@data-id='file'])[2]")
    input13_file1.click()

    """Пробовал вложить, использовал пути для файлов. но идет текстом"""
    current_dir = os.path.abspath(os.path.dirname('C:/Back/'))
    file_path = os.path.join(current_dir, 'Promto.txt')
    # file_path = os.path.join(current_dir, 'C:/Back/', 'Promto.txt')
!   # на след шаге не работает. возможно надо в поле кликнуть
    input13_file1.send_keys(file_path)
    # input13.send_keys(f"{os.getcwd()}\orig.png")  # не работает, текстом вкладывает C:\PycharmProjects\stepik_auto_tests_course\Live\geckodriver.log
    # input13.send_keys(os.path.join(os.getcwd()) + 'orig.png')
    # print("current_dir = ", current_dir)
    # input13.send_keys('/back/promto.txt')



    time.sleep(3)
    input13.send_keys(Keys.CONTROL + Keys.ENTER)

    driver.switch_to.default_content()

    # comment_field.send_keys("Adding file")  # не работает. Фрейм? - да
    # comment_field.send_keys(Keys.RETURN)

    # (//a[@class="feed-com-add-link"])[1]
    # original_text = driver.find_element(By.XPATH, '(//div[@class="feed-post-right-top-corner"]/div)[1]')
    # original_text.click()
    # time.sleep(1)
    # # original_text.send_keys(Keys.DOWN)  # не работает
    # # original_text.send_keys(Keys.ARROW_DOWN)
    # edit_field = driver.find_element(By.XPATH, '//div[@class="popup-window"]/div/div/div/a[2]')
    # time.sleep(2)
    # edit_field.click()
    #
    # iframe1: WebElement = driver.find_element(By.CSS_SELECTOR,
    #                                           "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm."
    #                                           "bxhtmled-iframe-cnt > iframe")
    # driver.switch_to.frame(iframe1)
    # input5 = driver.find_element(By.TAG_NAME, "body")
    # input5.send_keys("Edited ")
    # input5_1 = input5.text
    # input5.send_keys(Keys.CONTROL + Keys.ENTER)
    # driver.switch_to.default_content()
    # # нажимаю кнопку Отправить, заменил поиск кнопки нажатием Ctrl+Enter выше
    # # send_key = (driver.find_element(By.ID, 'blog-submit-button-save'))
    # # send_key.click()
    #
    # """ создам переменную, буду искать новый, отредактированный текст по части предложения. Это будет actual_text
    # # contains(text() - метод поиска по части текста
    # # пример # user_name = driver.find_element(By.XPATH, "//h4[contains(text(), 'Password for all ')]")
    # # требуемый текст, как описать только часть требуемого текста?"""
    #
    # time.sleep(2)
    # actual_text = driver.find_element(By.XPATH, "//div[contains(text(), 'Edited')]").text
    # # print("input5_1 - ", input5_1)
    # # print("actual_text - ", actual_text)
    # # (//div[@class="feed-post-text"])[1]
    # assert actual_text == input5_1



finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
