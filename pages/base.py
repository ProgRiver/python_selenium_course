from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators
from .locators import LoginPageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url


    def open(self):
        self.browser.get(self.url)


    def is_element_present(self, method, locator):
        try:
            self.browser.find_element(method, locator)
        except NoSuchElementException:
            return False
        return True


    def click_button_login_page(self):
        self.browser.find_element(*MainPageLocators.BTN_LOGIN).click()

    
    def should_be_login_form(self):
        """Проверка наличия формы логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "[!] Форма не найдена [!]"
