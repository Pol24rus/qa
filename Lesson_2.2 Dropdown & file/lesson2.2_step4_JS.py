from selenium import webdriver
import time

browser = webdriver.Chrome()

# browser.execute_script("alert('Robots at work');")
# time.sleep(3)
#browser.execute_script("document.title='Script executing';")
#browser.execute_script('document.title="Script executing";') # такой формат тоже можно
browser.execute_script("document.title='Script executing';alert('Robots at work');") # объединяет два предыдущих действия в одной строке
time.sleep(5)