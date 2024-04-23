from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
import datetime
from datetime import datetime
import os


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

    input1 = driver.find_element(By.ID, "microoPostFormLHE_blogPostForm_inner") #работает, клик в поле
    #input1 = driver.find_element(By.ID, "feed-add-post-form-tab-message") #вариант Любы (нажатие на кнопку) перестал работать
    input1.click()
    # текст сообщения
    iframe1: WebElement = driver.find_element(By.CSS_SELECTOR, "#bx-html-editor-iframe-cnt-idPostFormLHE_blogPostForm.bxhtmled-iframe-cnt > iframe")
    driver.switch_to.frame(iframe1)
    input2 = driver.find_element(By.TAG_NAME, "body")
    # input2.send_keys("Тест сообщение двум, от ", str(input_txt))
    driver.switch_to.default_content()
    time.sleep(5)

    #driver.implicitly_wait(3)
    """нажимаю скрепку и открываю окно для загрузки файла"""
    element_file = driver.find_element(By.ID, "bx-b-uploadfile-blogPostForm")  # клик на скрепку
    element_file.click()
    """Нажимаю загрузить"""
    input3 = driver.find_element(By.CSS_SELECTOR, "#disk-uf-file-container-Ny1b1Y > div > div > div > div.disk-user-field-panel > div > div:nth-child(1) > div > div > div.disk-user-field-panel-card-icon")
    input3.click()
    """определяю файл и загружаю его"""
    current_dir = os.path.abspath(
        os.path.dirname('/Users/poladko.dv/'))  # получаем путь к директории текущего исполняемого файла
    file_name = "life.txt"
    file_path = os.path.join(current_dir, file_name)  # добавляем к этому пути имя файла
    input3.send_keys(file_path)  # отправляем файл
    time.sleep(4)



    # time.sleep(3)
    # element_file = driver.find_element(By.ID, "bx-b-uploadfile-blogPostForm")  # кнопка Файл
    # element_file.click()

    # driver.implicitly_wait(5)
    #Ищу и нажимаю Добавить ещё
    ok = driver.find_element(By.CSS_SELECTOR, ".ui-tag-selector-add-button-caption")
    ok.click()
    # ищу и ввожу Поладько и Отдел кадров
    # но это неправильно работает. выбирает не ОК, а что попадается.
    #element_input = driver.find_element(By.CSS_SELECTOR, "div:nth-child(11) > div.ui-selector-item > div.ui-selector-item-titles > div.ui-selector-item-title-box > div.ui-selector-item-title")
    #element_input.click()
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
    # убираю Всем работникам
    #driver.find_element(By.CSS_SELECTOR, "div.ui-tag-selector-tag-remove").click() #теперь её нет в строке
    driver.find_element(By.CSS_SELECTOR, "input.ui-tag-selector-item.ui-tag-selector-text-box").click()

    button = driver.find_element(By.ID, "blog-submit-button-save")
    button.click()

finally:
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    driver.quit()

# не забываем оставить пустую строку в конце файла