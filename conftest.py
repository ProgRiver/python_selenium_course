from selenium import webdriver
import pytest
import time


# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata["Platform"] = "Windows 7"


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("Platform", None)


def pytest_html_results_table_header(cells):
    cells.pop()


def pytest_html_results_table_row(cells):
    cells.pop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(report, "duration_formatter", "%M:%S.%f")


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
        raise pytest.UsageError("--browser_name should be chrome or firefox or --language not in page")
    
    yield driver
    time.sleep(1)
    driver.quit()
