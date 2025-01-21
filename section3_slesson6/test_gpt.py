import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# Список URL-адресов для тестирования
urls = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
]

    
@pytest.mark.parametrize("url", urls)
def test_authorization(driver, url):
    # Открытие страницы урока
    driver.get(url)

    # Дожидаемся появления кнопки 'Войти'
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ember471"))
    )
    login_button.click()

    # Ввод логина и пароля
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "id_login_email"))
    )
    password_input = driver.find_element(By.ID, "id_login_password")

    # Замените 'YOUR_EMAIL' и 'YOUR_PASSWORD' на свои данные
    email_input.send_keys("st.w0lf@mail.ru")
    password_input.send_keys("Volchara13")

    # Нажимаем на кнопку "Войти"
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".sign-form__btn.button_with-loader"))
    )
    submit_button.click()

    # Ожидаем, что поп-ап с авторизацией исчезнет
    WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.CSS_SELECTOR, ".modal-dialog"))
    )

    print("Успешная авторизация!")

    # Выполнение расчета
    answer = math.log(int(time.time()))
    # Заполнение поля с class "textarea "
    answer_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "textarea"))
    )
    answer_input.send_keys(str(answer))

    # Нажимаем на кнопку "Отправить"
    send_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    )
    send_button.click()
    
    
    # Ожидание и вывод сообщения об успешной отправке
    print("Ответ успешно отправлен!")

