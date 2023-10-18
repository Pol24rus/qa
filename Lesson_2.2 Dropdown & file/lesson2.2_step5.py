from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# прокрутка страницы

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
time.sleep(3)
browser.execute_script("window.scrollBy(0, 100);", button) # scrolling by 100 px
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
time.sleep(4)