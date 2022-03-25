from selenium.webdriver.common.by import By


link = "https://stepik.org/"


def test_add_to_cart_button_in_page(browser):
    browser.get(link)
    # assert 1 == 1
    assert browser.find_element(By.CLASS_NAME, "navbar__submenu-toggler"), "[!] Элемент не найден [!]"


# pytest --language=es test_items.py

# pytest --language=fr test_items.py
# "Ajouter au panier"

# pytest --language=de test_items.py
# "In Warenkorb legen"