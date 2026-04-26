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
    EMAIL_INPUT = (By.XPATH, "//form/fieldset[1]//input")
    PASSWORD_INPUT = (By.XPATH, "//form/fieldset[2]//input")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class MainPageLocators:
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    ACCOUNT_LINK = (By.XPATH, "//a[.//p[text()='Личный Кабинет']]")
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    LOGO_LINK = (By.XPATH, "//a[.//*[name()='svg' and @width='290' and @height='50']]")
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    ACTIVE_BUNS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current')][.//span[text()='Булки']]",
    )
    ACTIVE_SAUCES_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current')][.//span[text()='Соусы']]",
    )
    ACTIVE_FILLINGS_TAB = (
        By.XPATH,
        "//div[contains(@class, 'tab_tab_type_current')][.//span[text()='Начинки']]",
    )


class ForgotPasswordPageLocators:
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class AccountPageLocators:
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    PROFILE_DESCRIPTION = (
        By.XPATH,
        "//p[text()='В этом разделе вы можете изменить свои персональные данные']",
    )
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    LOGO_LINK = (By.XPATH, "//a[.//*[name()='svg' and @width='290' and @height='50']]")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
