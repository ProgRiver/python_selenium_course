from .base import BasePage
from .locators import LoginPageLocators


text_info = "[!] Элемент не найден [!]"


class LoginPage(BasePage):
    def should_be_elements_in_login_form(self):
        self.should_be_email_input()
        self.should_be_button_submit()
        self.should_be_button_register()
        self.should_be_providers_block()


    def should_be_email_input(self):
        """Поле для ввода телефона или почты"""
        assert self.is_element_present(*LoginPageLocators.INPUT_EMAIL), f"{text_info}"


    def should_be_button_submit(self):
        """Кнопка отправки логина"""
        assert self.is_element_present(*LoginPageLocators.BTN_SUBMIT), f"{text_info}"


    def should_be_button_register(self):
        """Кнопка регистрации нового пользователя"""
        assert self.is_element_present(*LoginPageLocators.BTN_REGISTER), f"{text_info}"


    def should_be_providers_block(self):
        """Список провайдеров для входа"""
        assert self.is_element_present(*LoginPageLocators.BLOCK_PROVIDERS), f"{text_info}"