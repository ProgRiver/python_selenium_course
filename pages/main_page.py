from .base import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def should_be_all_elements(self):
        self.should_be_search_input()
        self.should_be_search_microphone()
        self.should_be_button_keyboard()
        self.should_be_button_search()


    def should_be_search_input(self):
        """Наличие строки ввода для поиска"""
        assert self.is_element_present(*MainPageLocators.SEARCH_INPUT), "[!] Элемент не найден [!]"


    def should_be_search_microphone(self):
        """Наличие кнопки поиска через микрофон"""
        assert self.is_element_present(*MainPageLocators.SEARCH_MICROPHONE), "[!] Элемент не найден [!]"


    def should_be_button_keyboard(self):
        """Наличие кнопки клавиатуры"""
        assert self.is_element_present(*MainPageLocators.BTN_KEYBOARD), "[!] Элемент не найден [!]"


    def should_be_button_search(self):
        """Наличие кнопки поиска"""
        assert self.is_element_present(*MainPageLocators.BTN_SEARCH), "[!] Элемент не найден [!]"
    

    def should_be_button_login(self):
        """Наличие кнопки перехода на страницу логина"""
        assert self.is_element_present(*MainPageLocators.BTN_LOGIN), "[!] Элемент не найден [!]"
