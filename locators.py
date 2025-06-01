from selenium.webdriver.common.by import By

# Кнопки и навигация
LOGIN_REGISTER_BUTTON = (By.XPATH, "//button[contains(text(),'Вход и регистрация')]")
NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Нет аккаунта')]")
LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")
PLACE_AD_BUTTON = (By.XPATH, "//button[contains(text(),'Разместить объявление')]")

# Поля формы регистрации (обновлены по placeholder)
REG_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Введите Email']")
REG_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
REG_REPEAT_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Повторите пароль']")
CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(),'Создать аккаунт')]")

# Поля авторизации
LOGIN_EMAIL_INPUT = (By.XPATH, "//input[@placeholder='Введите Email']")
LOGIN_PASSWORD_INPUT = (By.XPATH, "//input[@placeholder='Пароль']")
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(),'Войти')]")

# Подтверждение входа
USER_NAME_HEADER = (By.XPATH, "//h3[contains(@class, 'profileText') and contains(@class, 'name')]")
PROFILE_HEADER = (By.XPATH, "//h1[contains(text(), 'Мой профиль')]")


# Ошибки
EMAIL_ERROR = (By.XPATH, "//form//span[contains(text(), 'Ошибка')]")
EXISTING_USER_ERROR = (By.XPATH, "//form//span[contains(text(), 'Ошибка')]")

# Модальное окно (для неавторизованных)
AUTH_REQUIRED_MODAL = (By.CLASS_NAME, "popUp_shell__LuyqR")

# Форма объявления
AD_TITLE_INPUT = (By.NAME, "name")
AD_DESCRIPTION_INPUT = (By.XPATH, "//textarea[@name='description' and @placeholder='Описание товара']")
AD_PRICE_INPUT = (By.NAME, "price")
AD_CATEGORY_DROPDOWN = (By.XPATH, "//form//button[contains(@class, 'dropDownMenu_arrowUp')]")
AD_CATEGORY_OPTION = (By.XPATH, "//button[span[text()='Садоводство']]")
AD_CITY_DROPDOWN = (By.XPATH, "//form//button[contains(@class, 'dropDownMenu_arrowUp')]")
CITY_OPTION_SPB = (By.XPATH, "//button[span[text()='Санкт-Петербург']]")
AD_STATE_RADIO = (By.XPATH, "//label[contains(text(), 'Новый')]")
PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(),'Опубликовать')]")

# Профиль
MY_ADS_SECTION = (By.XPATH, "//h1[text()='Мои объявления']/ancestor::div[contains(@class, 'profilePage_listningBlock')]")
PROFILE_BUTTON = (By.XPATH, "//*[@id='root']//div[contains(@class, 'header_shell')]//div[contains(@class, 'flexRow')]/button")
PUBLISHED_AD = (By.XPATH, "//div[contains(., 'Новый велосипед') and contains(., '5000')]")
PAGINATION_BUTTON = (By.XPATH, "//button[contains(., '›') or contains(., '>')]")


# Профиль (новые локаторы)
PROFILE_ADS_SECTION = (By.XPATH, "//div[contains(@class, 'profilePage_listningBlock__Fi6E5')]//h1[contains(text(), 'Мои объявления')]/ancestor::div[contains(@class, 'profilePage_listningBlock__Fi6E5')]")
ADS_CARD = (By.XPATH, "//div[contains(@class, 'card')]")
ADS_TITLE = (By.XPATH, ".//div[@class='description']//h2")
ADS_CITY = (By.XPATH, ".//div[@class='description']//h3")
ADS_PRICE = (By.XPATH, ".//div[@class='price']//h2")
PAGINATION_NEXT_BTN = (By.XPATH, "//button[contains(@class, 'arrowButton--right')]")