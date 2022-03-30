from .pages.main_page import MainPage
import pytest


url = "https://yandex.ru"


def test_guest_sees_page_elements(browser):
    page = MainPage(browser, url)
    page.open()
    page.should_be_all_elements()


# @pytest.mark.skip
def test_guest_sees_button_login(browser):
    try:
        page = MainPage(browser, url)
        page.open()
        page.should_be_button_login()
    except AssertionError:
        pytest.exit(reason="\nНет кнопки перехода на страницу логина")


# @pytest.mark.skip
def test_guest_go_to_login_page(browser):
    page = MainPage(browser, url)
    page.open()
    page.click_button_login_page()
    page.should_be_login_form()
