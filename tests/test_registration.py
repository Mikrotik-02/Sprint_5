from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import REGISTER_URL
from helpers import register_user
from locators import RegisterPageLocators

class TestRegistration:

    def test_registration_with_valid_data_redirects_to_login_page(self, driver, user_data):
        login_title = register_user(driver, user_data)

        assert login_title.text == "Вход"


    def test_registration_with_short_password_shows_error(self, driver, user_data):
        driver.get(REGISTER_URL)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(user_data["name"])
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("12345")
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        password_error = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
        )

        assert password_error.text == "Некорректный пароль"
