from selenium import webdriver
import pytest
import time


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption("--language", action="store", default="ru", help="Choose language")


@pytest.fixture(scope="function")
def browser(request):

    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    
    driver = None
    if browser_name == "chrome":
        settings_ch = webdriver.ChromeOptions()
        settings_ch.add_experimental_option("excludeSwitches", ['enable-logging'])
        settings_ch.add_argument("--window-size=1250,950")
        settings_ch.add_experimental_option("prefs", {'intl.accept_languages': browser_language})
        driver = webdriver.Chrome(options=settings_ch)
    elif browser_name == "firefox":
        settings_fp = webdriver.FirefoxOptions()
        settings_fp.set_preference("intl.accept_languages", browser_language)
        driver = webdriver.Firefox(options=settings_fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield driver
    time.sleep(2)
    driver.quit()
