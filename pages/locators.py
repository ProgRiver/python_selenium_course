from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.ID, "text")
    SEARCH_MICROPHONE = (By.CSS_SELECTOR, "div.input__voice-search")
    BTN_KEYBOARD = (By.CSS_SELECTOR, "div.input__keyboard-button")
    BTN_SEARCH = (By.CSS_SELECTOR, ".button.mini-suggest__button")
    BTN_LOGIN = (By.CSS_SELECTOR, "a.desk-notif-card__login-new-item_enter")


class LoginPageLocators:
    LOGIN_FORM = ()
    INPUT_EMAIL = ()
    BTN_SUBMIT = ()
    