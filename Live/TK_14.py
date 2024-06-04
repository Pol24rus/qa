# Отметить человека в комментарии.
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
    driver.maximize_window()

    # авторизация
    login = driver.find_element(By.ID, 'USER_LOGIN')
    login.send_keys("OK_RLI")
    password = driver.find_element(By.ID, "USER_PASSWORD")
    password.send_keys("OK_RLIOK_RLI")
    button1 = driver.find_element(By.CSS_SELECTOR, "input.btn")
    button1.click()
    # time.sleep(1)
    """данный кейс ставить Желательно после ТК_6 (создать сообщение одному), чтобы находить и редактировать сообщение, а не задачи и тд."""
    # ввожу дату и время, чтобы получить уникальность сообщения
    input_txt = datetime.now()
    # TK_14 (add user in comment)
    # нахожу поле комментария, кликаю сразу в него, не нажимая кнопку Коментировать
    comment_field = driver.find_element(By.XPATH, "(//a[@class='feed-com-add-link'])[1]")
    comment_field.click()
    time.sleep(2)
    """нажимаю кнопку Отметить человека"""
    input14 = driver.find_element(By.XPATH, "(//div[@data-id='mention'])[2]")
    input14.click()
    time.sleep(1)
    """ввожу ФИО в открывшееся поле"""
    # input14_name = driver.find_element((By.XPATH, "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']"))
    # WebDriverWait(driver, 5).until(EC.element_to_be_clickable(input14_name))
    input14_name = driver.find_element(By.XPATH, "//input[@class='ui-tag-selector-item ui-tag-selector-text-box']")  # работает, но нужны паузы
    # input14_name = driver.find_element(By.XPATH, "(//div[@class='ui-tag-selector-container'])[3]")
    # input14_name = driver.find_element(By.XPATH, "(//div[@class='ui-tag-selector-outer-container'])[3]")
    # input14_name = driver.find_element(By.XPATH, "(//div[@class='ui-tag-selector-outer-container']/div)[3]")
    time.sleep(1)
    input14_name.send_keys("Поладько")
    input14_name.send_keys(Keys.RETURN)
    time.sleep(1)
    """Нажимаю Отправить"""
    # input14_sendKey = driver.find_element(By.XPATH, "//button[@id='lhe_button_submit_blogCommentFormk71n']")
    input14_sendKey  = driver.find_element(By.XPATH, "(//div[@class='feed-add-post-buttons --no-wrap']/button[@class='ui-btn ui-btn-sm ui-btn-primary'])[2]")
    input14_sendKey.click()

    # Работает, оставлю на утро. Сменил слипы на 1 сек, не проверял

    # """Нажимаю Загрузить"""
    # # input13_file2 = driver.find_element(By.XPATH, "/html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td["
    # #                                               "2]/table/tbody/tr/td/div/div[2]/div/div[1]/div/div/div["
    # #                                               "3]/form/div[1]/div/div[2]/div[3]/div/div/div/div[1]/div/div["
    # #                                               "1]/div/div/div[1]")
    # input13_file2 = driver.find_element(By.XPATH, "(//div[contains(text(), 'Загрузить')])[2]")
    # # input13_file2.click()
    # # time.sleep(2)
    # # input13_file2.send_keys(Keys.TAB)
    # # time.sleep(2)
    #
    # """Использую"Вы можете просто перетащить файл сюда"""
    # # input13_file3 = driver.find_element(By.XPATH, "//div[@id='disk-uf-file-container-xMknNV']/div/div/div/div[@class='ui-tile-uploader-drop-area']")
    # # input13_file3.click()
    # # //div[@id="disk-uf-file-container-xMknNV"]/div/div/div/div[@class="ui-tile-uploader-drop-area"]
    #
    # """Закомментил строки 56,57и 72. Вместо Клик отправляю файл сразу. 56 и 57 надо оставить"""
    #
    # """Пробовал вложить, использовал пути для файлов. но идет текстом"""
    # # current_dir = os.path.abspath(os.path.dirname('C:/Back/'))
    # # file_path = os.path.join(current_dir, 'Promto.txt')
    # # # file_path = os.path.join(current_dir, 'C:/Back/', 'Promto.txt')
    # # # на след шаге не работает. возможно надо в поле кликнуть
    # # input13_file3.send_keys(file_path)
    # # input13_file2.send_keys(f"{os.getcwd()}/orig.png")  # не работает, текстом вкладывает C:\PycharmProjects\stepik_auto_tests_course\Live\geckodriver.log
    # # input13_file2.send_keys(os.path.join(os.getcwd()) + 'orig.png')
    # # print("current_dir = ", current_dir)
    # input13_file2.send_keys('/back/promto.txt')
    #
    #
    # time.sleep(3)
    # # input13.send_keys(Keys.CONTROL + Keys.ENTER)
    #
    # # driver.switch_to.default_content()

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
