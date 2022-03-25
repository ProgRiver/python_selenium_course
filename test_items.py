from selenium.webdriver.common.by import By


def test_element_presence_control(browser):
    browser.get("https://stepik.org/")
    assert browser.find_element(By.CLASS_NAME, "navbar__submenu-toggler"), "[!] Элемент не найден [!]"
