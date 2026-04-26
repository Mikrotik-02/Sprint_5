import random
import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def user_data():
    random_number = random.randint(100000, 999999)

    return {
        "name": "Artem",
        "email": f"artemkoval44_{random_number}@yandex.ru",
        "password": "123456"
    }