from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators


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
    

    # def res_element(self):
    #     assert self.is_element_present(*MainPageLocators.LOGIN_LINK)