from .pages.main_page import MainPage
import pytest


url = "https://yandex.by"


def test_guest_sees_page_elements(browser):
    page = MainPage(browser, url)
    page.open()
    page.should_be_all_elements()


def test_guest_sees_button_login(browser):
    try:
        page = MainPage(browser, url)
        page.open()
        page.should_be_button_login()
    except AssertionError:
        pytest.exit(reason="\nНет кнопки перехода на страницу логина")


def test_guest_go_to_login_page(browser):
    page2 = MainPage(browser, url)
    page2.open()
    page2.click_button_login_page()
