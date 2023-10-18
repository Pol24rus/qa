import os # модуль для работы с ОС
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

current_dir = os.path.abspath(os.path.dirname('C:/Users/poladko.dv/Documents/2023/2023_09/'))    # получаем путь к директории текущего исполняемого файла 
print(os.path.join(current_dir, 'C:/Users/poladko.dv/Documents/2023/2023_09/', '2023_09_15-22.txt'))
# file_name = "2023_09_15-22.txt"                             # имя файла, который будем загружать на сайт
file_path = os.path.join('C:/Users/poladko.dv/Documents/2023/2023_09/', '2023_09_15-22.txt')           # добавляем к этому пути имя файла (получаем путь к file_example.txt)
element = browser.find_element(By.CSS_SELECTOR, "[type='file']")
element.send_keys(file_path)                                # отправляем файл
time.sleep(4)

print(os.path.abspath(os.path.abspath('C:/Users/poladko.dv/Documents')))

time.sleep(4)
#путь к файлу, который лeжит не в директории с исполняемым файлом