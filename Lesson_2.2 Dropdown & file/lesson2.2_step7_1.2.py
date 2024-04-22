import os # модуль для работы с ОС
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_name = "2023_09_22-28.txt"                             # имя файла, который будем загружать на сайт
file_path = os.path.join(current_dir, '2023_09_22-27.txt')           # добавляем к этому пути имя файла (получаем путь к file_example.txt)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)                                # отправляем файл

print(os.path.abspath(os.path.dirname(__file__)))

time.sleep(4)