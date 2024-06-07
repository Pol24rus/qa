# Вставить ссылку в комментарии.
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

    # TK_15 (add Link in comment)
    """данный кейс вставить в ТК_14 чтобы работать в одном поле комментарий"""
    # нахожу поле комментария, кликаю сразу в него, не нажимая кнопку Коментировать
    comment_field = driver.find_element(By.XPATH, "(//a[@class='feed-com-add-link'])[1]")
    comment_field.click()
    time.sleep(1)

    """Ищу кнопку Ссылка"""
    # button_link = driver.find_element(By.XPATH, "//span[contains(text(), 'Ссылка')]")
    button_link = driver.find_element(By.XPATH, "//span[@title='Ссылка']")
    button_link.click()
    time.sleep(1)
    """Ищу адресную строку. Ввожу ссылку. И текстовую строку"""
    # text_link = driver.find_element(By.XPATH, "//input[@id='linkidLHE_blogCommentFormblogCommentFormm94n-text']")
    # text_link = driver.find_element(By.ID, "linkidLHE_blogCommentFormblogCommentFormm94n-text")
    # text_link = driver.find_element(By.XPATH, "(//td[@class='bxhtmled-right-c'])[1]")
    text_link = driver.find_element(By.XPATH, "(//td[@class='bxhtmled-right-c']/input)[1]")
    # (//td[@class="bxhtmled-right-c"]/input)[1]
    # time.sleep(1)
    # text_link.send_keys(Keys.ENTER)
    # time.sleep(5)
    text_link.send_keys('Официальный сайт РЛИ ')
    adress_link = driver.find_element(By.XPATH, "(//td[@class='bxhtmled-right-c']/input)[2]")
    # time.sleep(5)
    # # adress_link.click()
    adress_link.send_keys("https://roslesinforg.ru/")
    adress_link.send_keys(Keys.ENTER)
    time.sleep(1)
    """Нажимаю Отправить"""
    # input14_sendKey = driver.find_element(By.XPATH, "//button[@id='lhe_button_submit_blogCommentFormk71n']")
    input15_sendKey = driver.find_element(By.XPATH,"(//div[@class='feed-add-post-buttons --no-wrap']/button[@class='ui-btn ui-btn-sm ui-btn-primary'])[2]")
    input15_sendKey.click()

    """ Проверка по URL. Это будет actual_url
    get_url = driver.current_url
    //body/a[text()[contains(.,'Ссылка')]]
        # contains(text() - метод поиска по части текста
        # пример # user_name = driver.find_element(By.XPATH, "//h4[contains(text(), 'Поладько ')]")"""
    # //html[@class="bx-core bx-win bx-no-touch bx-no-retina bx-chrome"]/body/span[@class="bxhtmled-metion"] - actual
    # //span[@class="bxhtmled-metion"] - actual
    # time.sleep(2)
    # actual_url = driver.find_element(By.XPATH, "(//div[@class='feed-com-text']/div/div/div/a)[1]").text
    # actual_url = driver.find_element(By.XPATH, "(//div[@class='feed-com-main-content feed-com-block-old']/div[2]/div/div/div/a)[1]").text  # вернет Официальный сайт...
    # actual_url = driver.find_element(By.XPATH,
    #                                  "((//div[@class='feed-com-main-content feed-com-block-old']/div[2]/div/div/div/a)[1])[text()[contains(., 'https://roslesinforg.ru/')]]")
    # actual_url = driver.find_element(By.XPATH,
    #                                  "//div[@class='feed-com-main-content feed-com-block-old']/div[2]/div/div/div[text()[contains(.,'https://roslesinforg.ru/')]]")
    # actual_url = driver.find_element(By.XPATH, "(//div[@class='feed-com-main-content feed-com-block-old']/div[2]/div/div/div/a)[1]").get_attribute(name='href') # возвращает ОК
    # получается хватает первый попавшийся аттрибут из класса, а это профиль ОК. То есть или ниже спускаться, или индекс для href использовать
    # actual_url = driver.find_element(By.XPATH, "(//div[@class='feed-com-text']/div/div/div/a)[1]").get_attribute(name='href')  # возвращает ОК
    # driver.find_element(By.XPATH, "//span[contains(text(), 'С сообщением ознакомлен')]") образец

    actual_url = driver.find_element(By.XPATH, "//a[contains(text(), 'Официальный сайт РЛИ')]").get_attribute(name='href')
    # actual_url = driver.find_element(By.XPATH, "//a[contains(text(), 'https://roslesinforg.ru/')]").get_attribute(
    #     name='href')
    print("actual_url - ", actual_url)
    needed_url = "https://roslesinforg.ru/"
    assert actual_url == needed_url
    # # self.assertEqual(needed_text, actual_text, "Не тот текст")



finally:
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    driver.quit()
