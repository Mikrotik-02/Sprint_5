from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import REGISTER_URL
from locators import LoginPageLocators, MainPageLocators, RegisterPageLocators


def register_user(driver, user_data):
    driver.get(REGISTER_URL)

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(user_data["name"])
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
    )


def login_user(driver, user_data):
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    return WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )
