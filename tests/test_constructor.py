from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data import MAIN_URL
from locators import MainPageLocators

class TestConstructor:

    def test_click_on_buns_tab_makes_buns_tab_active(self, driver):
        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SAUCES_TAB)
        )
        driver.find_element(*MainPageLocators.BUNS_TAB).click()

        active_buns_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_BUNS_TAB)
        )

        assert active_buns_tab.text == "Булки"


    def test_click_on_sauces_tab_makes_sauces_tab_active(self, driver):
        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.SAUCES_TAB).click()

        active_sauces_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_SAUCES_TAB)
        )

        assert active_sauces_tab.text == "Соусы"


    def test_click_on_fillings_tab_makes_fillings_tab_active(self, driver):
        driver.get(MAIN_URL)

        driver.find_element(*MainPageLocators.FILLINGS_TAB).click()

        active_fillings_tab = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ACTIVE_FILLINGS_TAB)
        )

        assert active_fillings_tab.text == "Начинки"
