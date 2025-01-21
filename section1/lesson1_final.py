from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def input_data():
    input_first_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your first name"]')
    input_first_name.send_keys("test")
    input_last_name = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your last name"]')
    input_last_name.send_keys("test")
    input_email = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your email"]')
    input_email.send_keys("test")
    input_phone = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your phone:"]')
    input_phone.send_keys("test")
    input_address = browser.find_element(By.CSS_SELECTOR, '[placeholder="Input your address:"]')
    input_address.send_keys("test")
    button_send = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button_send.click()	

def check_result():
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

try:
#сделал в одном тесте проверку обеих ссылок, хоть так и не делают обычно
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/registration2.html")
    input_data()
    check_result()
   
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла