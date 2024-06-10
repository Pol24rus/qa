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
    # ввожу дату и время, чтобы получить уникальность сообщения
    input_txt = datetime.now()
    # TK_14 (add user in comment)
    """данный кейс ставить Желательно после ТК_6 (создать сообщение одному), чтобы находить и редактировать сообщение, а не задачи и тд."""
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
    time.sleep(2)
    input14_name.send_keys("Поладько")
    time.sleep(1)
    input14_name.send_keys(Keys.ENTER)
    # comment_field.send_keys(" - Отмеченный сотрудник")  # не получится просто так текст вставить, там фрейм.
    time.sleep(1)
    """Нажимаю Отправить"""
    # input14_sendKey = driver.find_element(By.XPATH, "//button[@id='lhe_button_submit_blogCommentFormk71n']")
    input14_sendKey = driver.find_element(By.XPATH, "(//div[@class='feed-add-post-buttons --no-wrap']/button[@class='ui-btn ui-btn-sm ui-btn-primary'])[2]")
    input14_sendKey.click()

    # Работает, оставлю на утро. Сменил слипы на 1 сек, не проверял


    """ Проверка по ФИО. Это будет actual_text
    # пример # user_name = driver.find_element(By.XPATH, "//h4[contains(text(), 'Поладько ')]")
    # требуемый текст, как описать только часть требуемого текста?"""
    # //html[@class="bx-core bx-win bx-no-touch bx-no-retina bx-chrome"]/body/span[@class="bxhtmled-metion"] - actual
    # //span[@class="bxhtmled-metion"] - actual
    time.sleep(2)

    """надо менять поиск, менять селектор"""

    # actual_text = driver.find_element(By.XPATH, "//span[contains(text(), 'Поладько')]").text
    # actual_text = driver.find_element(By.XPATH, "//a[@id='bp_o67oBGjY']")
    # //div[@class="feed-com-main-content feed-com-block-old"]/div[2]/div/div/div/a - находит 5 элементов
    # actual_text = driver.find_element(By.XPATH, "//div[@class='feed-com-main-content feed-com-block-old']/div[2]/div/div/div/a[@id='bp_uF314qst']")
    # id в предыдущей строке каждый раз создается новый
    # actual_text = driver.find_element(By.XPATH,
    #                                   "//div[@class='feed-com-main-content feed-com-block-old']/div[2]/div/div/div/a[@href='/company/personal/user/26538/']") # находит 4 элемента
    # actual_text = driver.find_element(By.XPATH,
    #                                   "//div[@class='feed-com-block-cover']/div/div/div[2]/div[2]/div/div/div/a[@class='blog-p-user-name']")
    # actual_text = driver.find_element(By.XPATH, "//html/body/table/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/table/tbody/tr/td/div/div[2]/div/div[4]/div[3]/div[1]/div/div[3]/div[1]/div/div[3]/div[3]/div[1]/div[1]/div[2]/div[2]/div[1]/div/div/a")
    actual_text = driver.find_element(By.XPATH, "//div[@class='feed-post-block feed-post-block-files feed-post-block-separator feed-post-block-pin feed-post-block-has-bottom']/div[3]/div/div/div/div/div/div[2]/div[2]/div/div/div/a").text
    print("actual_text - ", actual_text)
    needed_text = "Поладько Дмитрий "
    # # (//div[@class="feed-post-text"])[1]
    assert actual_text == needed_text
    # self.assertEqual(needed_text, actual_text, "Не тот текст")


finally:
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла
