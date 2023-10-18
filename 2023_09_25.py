import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config #для локального запуска #to remote only!
from selene import browser
# from selene.support.shared import browser #to remote only!
from dotenv import load_dotenv #to remote only!
import pytest

from urllib import request

# from webdriver_manager.core.os_manager import ChromeType

from webdriver_manager.chrome import ChromeDriverManager

from utils import attach


# -----LOCAL's setting---------------------------------------------
'''
@pytest.fixture(scope="session", autouse=True)
def browser_management():    
    browser.config.base_url = 'https://arivistika.ru'
    browser.config.timeout = 10
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1280
    browser.config.window_height = 720
    
    # browser.config.driver_options = driver_options
    # browser.config.hold_browser_open = True
    # driver_options.add_argument('--headless') #!
    driver_options = webdriver.ChromeOptions()

    yield 

    # ATTACH's
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()
'''

# ----------------------------------------------------------------------
# Selenium3:
#  driver = webdriver.Chrome(ChromeDriverManager(version="114.0.5735.90").install(), options=options)

# Selenium4:
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(
#     version="114.0.5735.90").install()), options=options)


DEFAULT_BROWSER_VERSION = "100.0"

def pytest_addoption(parser):
    parser.addoption(
        '--browser_version',
        default='100.0'
    )

@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

# фикстура удаленного запуска:
@pytest.fixture(scope='function', autouse=True)
def setup_browser(request):
    browser_version = request.config.getoption('--browser_version')
    browser_version = browser_version if browser_version != "" else DEFAULT_BROWSER_VERSION

    #capabilites Selenoid:
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version, #"100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True #!
        }
}
    # options.addArguments("--disable-features=VizDisplayCompositor");

    options.capabilities.update(selenoid_capabilities)
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    driver = webdriver.Remote(
        # command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub", #see file .env
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",  # see params here
        options=options
    )

    # browser = Browser(Config(driver)) #ЛОКАЛЬНЫЙ запуск драйвера Хром
    browser.config.driver = driver  #УДАЛЕННЫЙ запуск драйвера Хром
    browser.config.timeout = 10
    driver.get('https://arivistika.ru') #to loginpage test only!
    browser.config.base_url = 'https://arivistika.ru'
    browser.config.window_width = 1280
    browser.config.window_height = 1024

    yield browser

    # ATTACHs
    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()