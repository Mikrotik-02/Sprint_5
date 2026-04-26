from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import REGISTER_URL
from locators import LoginPageLocators, RegisterPageLocators


def test_registration_with_valid_data_redirects_to_login_page(driver, user_data):
    driver.get(REGISTER_URL)

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(user_data["name"])
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    login_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
    )

    assert login_title.text == "Вход"


def test_registration_with_short_password_shows_error(driver, user_data):
    driver.get(REGISTER_URL)

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(user_data["name"])
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys("12345")
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    password_error = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR)
    )

    assert password_error.text == "Некорректный пароль"
