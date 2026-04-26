from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import login_user, register_user
from locators import AccountPageLocators, MainPageLocators


def test_click_on_account_link_redirects_to_account_page(driver, user_data):
    register_user(driver, user_data)
    login_user(driver, user_data)

    driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()

    description = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AccountPageLocators.PROFILE_DESCRIPTION)
    )

    assert description.text == "В этом разделе вы можете изменить свои персональные данные"


def test_click_on_constructor_redirects_to_main_page(driver, user_data):
    register_user(driver, user_data)
    login_user(driver, user_data)
    driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AccountPageLocators.PROFILE_DESCRIPTION)
    )
    driver.find_element(*AccountPageLocators.CONSTRUCTOR_LINK).click()

    constructor_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
    )

    assert constructor_title.text == "Соберите бургер"


def test_click_on_logo_redirects_to_main_page(driver, user_data):
    register_user(driver, user_data)
    login_user(driver, user_data)
    driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(AccountPageLocators.PROFILE_DESCRIPTION)
    )
    driver.find_element(*AccountPageLocators.LOGO_LINK).click()

    constructor_title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE)
    )

    assert constructor_title.text == "Соберите бургер"
