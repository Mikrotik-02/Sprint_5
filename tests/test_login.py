from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import FORGOT_PASSWORD_URL, MAIN_URL, REGISTER_URL
from helpers import login_user, register_user
from locators import (
    ForgotPasswordPageLocators,
    LoginPageLocators,
    MainPageLocators,
    RegisterPageLocators,
)
class TestLogin:

    def test_login_from_main_page_login_account_button(self, driver, user_data):
        register_user(driver, user_data)
        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.LOGIN_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )

        order_button = login_user(driver, user_data)

        assert order_button.text == "Оформить заказ"


    def test_login_from_account_link(self, driver, user_data):
        register_user(driver, user_data)
        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )

        order_button = login_user(driver, user_data)

        assert order_button.text == "Оформить заказ"


    def test_login_from_registration_page_login_link(self, driver, user_data):
        register_user(driver, user_data)
        driver.get(REGISTER_URL)

        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )

        order_button = login_user(driver, user_data)

        assert order_button.text == "Оформить заказ"


    def test_login_from_forgot_password_page_login_link(self, driver, user_data):
        register_user(driver, user_data)
        driver.get(FORGOT_PASSWORD_URL)

        driver.find_element(*ForgotPasswordPageLocators.LOGIN_LINK).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )

        order_button = login_user(driver, user_data)

        assert order_button.text == "Оформить заказ"
