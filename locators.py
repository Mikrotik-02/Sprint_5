from selenium.webdriver.common.by import By


class RegisterPageLocators:
    # Поле "Имя" на странице регистрации
    NAME_INPUT = (By.XPATH,".//label[text()='Имя']/following-sibling::input")
    # Поле "Email" на странице регистрации
    EMAIL_INPUT = (By.XPATH,".//label[text()='Email']/following-sibling::input")
    # Поле "Пароль" на странице регистрации
    PASSWORD_INPUT = (By.XPATH,".//label[text()='Пароль']/following-sibling::input")
    # Кнопка "Зарегистрироваться" на странице регистрации
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")
    # Ссылка "Войти" на странице регистрации
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")
    # Сообщение об ошибке "Некорректный пароль" на странице регистрации
    PASSWORD_ERROR = (By.XPATH, ".//p[text()='Некорректный пароль']")


class LoginPageLocators:
    # Заголовок страницы входа
    LOGIN_TITLE = (By.XPATH, ".//h2[text()='Вход']")
    # Поле "Email" на странице входа
    EMAIL_INPUT = (By.XPATH,".//label[text()='Email']/following-sibling::input")
    # Поле "Пароль" на странице входа
    PASSWORD_INPUT = (By.XPATH,".//label[text()='Пароль']/following-sibling::input")
    # Кнопка "Войти" на странице входа
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")


class MainPageLocators:
    # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    # Ссылка "Личный Кабинет" в шапке
    ACCOUNT_LINK = (By.CSS_SELECTOR, "a[href='/account']")
    # Ссылка "Конструктор" в шапке
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    # Логотип Stellar Burgers в шапке
    LOGO_LINK = (By.XPATH, "//div[contains(@class, 'logo')]//a")
    # Заголовок конструктора на главной странице
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']")
    # Кнопка "Оформить заказ" на главной странице после входа
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    # Вкладка "Булки" в конструкторе
    BUNS_TAB = (By.XPATH, ".//span[text()='Булки']")
    # Вкладка "Соусы" в конструкторе
    SAUCES_TAB = (By.XPATH, ".//span[text()='Соусы']")
    # Вкладка "Начинки" в конструкторе
    FILLINGS_TAB = (By.XPATH, ".//span[text()='Начинки']")
    # Активная вкладка "Булки" в конструкторе
    ACTIVE_BUNS_TAB = (By.XPATH,".//*[contains(@class, 'tab_tab_type_current') and .//span[text()='Булки']]",)
    # Активная вкладка "Соусы" в конструкторе
    ACTIVE_SAUCES_TAB = (By.XPATH,".//*[contains(@class, 'tab_tab_type_current') and .//span[text()='Соусы']]",)
    # Активная вкладка "Начинки" в конструкторе
    ACTIVE_FILLINGS_TAB = (By.XPATH,".//*[contains(@class, 'tab_tab_type_current') and .//span[text()='Начинки']]",)


class ForgotPasswordPageLocators:
    # Ссылка "Войти" на странице восстановления пароля
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href='/login']")


class AccountPageLocators:
    # Ссылка "Профиль" в личном кабинете
    PROFILE_LINK = (By.XPATH,".//a[@href='/account/profile']")
    # Описание раздела профиля в личном кабинете
    PROFILE_DESCRIPTION = (By.XPATH,".//p[text()='В этом разделе вы можете изменить свои персональные данные']")
    # Ссылка "Конструктор" в шапке из личного кабинета
    CONSTRUCTOR_LINK = (By.XPATH, "//a[.//p[text()='Конструктор']]")
    # Логотип Stellar Burgers в шапке из личного кабинета
    LOGO_LINK = (By.XPATH, "//div[contains(@class, 'logo')]//a")
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, ".//button[normalize-space()='Выход']")
