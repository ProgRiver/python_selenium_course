from .pages.main_page import MainPage
import pytest
import sys


def test_control(browser):
    page = MainPage(browser, "https://yandex.by")
    page.open()
    page.should_be_all_elements()
    page.should_be_button_login()
    # page.click_button_login_page()
    # page.result()


# @pytest.mark.skipif(reason="нет элемента")
# @pytest.mark.skip(reason="пропуск теста")
def test_control_2(browser):
    page2 = MainPage(browser, "https://yandex.by")
    page2.open()
    page2.click_button_login_page()


# def test_control(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()
#     page.should_be_button_login()


# @pytest.mark.skipif(1 == 1, reason="[!] First test_control FAILED [!]")
# def test2(browser):
#     link = "http://selenium1py.pythonanywhere.com/"
#     page = MainPage(browser, link)
#     page.open()