from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helpers import login_user, register_user
from locators import AccountPageLocators, LoginPageLocators, MainPageLocators

class TestLogout:

    def test_logout_from_account_page_redirects_to_login_page(self, driver, user_data):
        register_user(driver, user_data)
        login_user(driver, user_data)

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(AccountPageLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        login_title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE)
        )

        assert login_title.text == "Вход"
