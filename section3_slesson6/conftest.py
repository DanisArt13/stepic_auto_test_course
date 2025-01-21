import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Инициализация драйвера
    driver = webdriver.Chrome()
    yield driver  # Возвращаем драйвер в тест
    driver.quit()  # Закрытие драйвера после теста
