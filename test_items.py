from selenium.webdriver.common.by import By


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_in_page(browser):
    browser.get(link)
    assert browser.find_elements(By.CLASS_NAME, "btn-add-to-basket"), "[*] There is no button on the page [*]"

# pytest --language=es test_items.py