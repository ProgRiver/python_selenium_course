from .pages.login_page import LoginPage
import pytest


url = "https://yandex.ru"


def test_user_go_to_login(browser):
    page = LoginPage(browser, url)
    page.open()
    page.click_button_login_page()
    