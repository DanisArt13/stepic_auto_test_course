import time
from selenium.webdriver.common.by import By
import pytest

def test_add_to_cart_button_exists(browser):
    
    url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(url)

    time.sleep(30)  

    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    
    assert add_to_cart_button.is_displayed(), "Кнопка 'Добавить в корзину' не найдена"
    
