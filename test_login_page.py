from .pages.login_page import LoginPage
import pytest
import time


def test_user_sees_the_elements(browser):
    page = LoginPage(browser, "https://yandex.ru")
    page.open()
    page.click_button_login_page()
    page.should_be_elements_in_login_form()


def test_guest_go_to_registration(browser):
    reg = LoginPage(browser, "https://passport.yandex.by/auth/welcome")
    reg.open()
    reg.click_button_register_new_user()
    reg.should_be_register_form()


@pytest.mark.skip(reason="Маркировка теста для просмотра отчета")
def test_user_go_to_login(browser):
    page = LoginPage(browser, "https://passport.yandex.by/auth/welcome")
    page.open()
    page.user_enter_id_name()
    page.click_button_submit()
    time.sleep(1)
    page.user_enter_password()
    page.click_button_submit()
