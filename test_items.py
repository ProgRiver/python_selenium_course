from selenium.webdriver.common.by import By


def test_add_to_cart_button_in_page(browser):
    browser.get("https://stepik.org/")
    assert browser.find_element(By.CLASS_NAME, "navbar__submenu-toggler"), "[!] Элемент не найден [!]"
