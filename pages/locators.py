from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_INPUT = (By.ID, "text")
    SEARCH_MICROPHONE = (By.CSS_SELECTOR, "div.input__voice-search")
    BTN_KEYBOARD = (By.CSS_SELECTOR, "div.input__keyboard-button")
    BTN_SEARCH = (By.CSS_SELECTOR, ".button.mini-suggest__button")
    BTN_LOGIN = (By.CSS_SELECTOR, "a.desk-notif-card__login-new-item_enter")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".passp-auth-content")
    REGISTER_FORM = (By.CSS_SELECTOR, ".registration__block")
    INPUT_EMAIL = (By.ID, "passp-field-login")
    INPUT_PASSWORD = (By.ID, "passp-field-passwd")
    BTN_SUBMIT = (By.ID, "passp:sign-in")
    BTN_REGISTER = (By.ID, "passp:exp-register")
    BTN_CANCEL = (By.CSS_SELECTOR, ".Button2_view_pseudo")
    BLOCK_PROVIDERS = (By.CSS_SELECTOR, ".AuthSocialBlock-providers")
