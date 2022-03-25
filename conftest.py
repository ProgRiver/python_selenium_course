# from selenium import webdriver

# import pytest
# import time

# def pytest_addoption(parser):
#     parser.addoption("--language", action="store", default="ru", help="Choose language")


# @pytest.fixture(scope="function")
# def browser(request):
#     """
#     Фикстура объявления браузера и настроек. Передается в тест, как параметр.
#     """
#     language_on_request = request.config.getoption("language")
#     settings = webdriver.ChromeOptions()

#     # Настройки запроса
#     settings.add_experimental_option("prefs", {"intl.accept_languages": language_on_request})
#     # # Настройки терминала (убирает лишнюю информацию)
#     # settings.add_experimental_option('excludeSwitches', ['enable-logging'])

#     driver = webdriver.Chrome(options=settings)
#     yield driver

#     # Установите ожидание закрытия браузера 
#     time.sleep(3)
#     driver.quit()



from selenium import webdriver
import pytest
import time


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):

    settings = webdriver.ChromeOptions()
    settings.add_experimental_option('excludeSwitches', ['enable-logging'])

    browser_name = request.config.getoption("browser_name")
    driver = None
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=settings)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    
    yield driver
    time.sleep(3)
    driver.quit()


# pytest -s -v --browser_name=firefox test_items.py
# pytest -v --browser_name=firefox test_items.py