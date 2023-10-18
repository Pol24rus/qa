from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import os 

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, "firstname") # "div > input:nth-child(2)" Тоже работает
    input1.send_keys("Pol")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("24Rus")
    input3 = browser.find_element(By.CSS_SELECTOR, "input:nth-child(6)") # локатор по детям
    input3.send_keys("pol24rus@ya.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, '2023_09_22-28.txt')  # добавляем к этому пути имя файла (получаем путь к file_example.txt)
    element = browser.find_element(By.ID, "file")
    element.send_keys(file_path)                                # отправляем файл

    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
