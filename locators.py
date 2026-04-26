from selenium.webdriver.common.by import By


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, "//form/fieldset[1]//input")
    EMAIL_INPUT = (By.XPATH, "//form/fieldset[2]//input")
    PASSWORD_INPUT = (By.XPATH, "//form/fieldset[3]//input")
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")
    PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")


class LoginPageLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")
