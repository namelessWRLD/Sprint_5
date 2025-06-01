import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestAdCreation:
    def test_create_ad_unauthorized(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*PLACE_AD_BUTTON).click()
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LOGIN_EMAIL_INPUT))
        assert driver.current_url.endswith("/login"), "Переход на страницу логина не выполнен"

    def test_create_ad_authorized(self, driver):
        # Авторизация
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("dadada@test.ru")
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456789")
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_HEADER))

        # Создание объявления
        driver.find_element(*PLACE_AD_BUTTON).click()
        driver.find_element(*AD_TITLE_INPUT).send_keys("Новый велосипед")
        driver.find_element(*AD_DESCRIPTION_INPUT).send_keys("Почти не использовался")
        driver.find_element(*AD_PRICE_INPUT).send_keys("5000")
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AD_CATEGORY_DROPDOWN))[0].click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AD_CATEGORY_OPTION)).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(AD_CITY_DROPDOWN))[1].click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(CITY_OPTION_SPB)).click()
        driver.find_element(*AD_STATE_RADIO).click()
        driver.find_element(*PUBLISH_BUTTON).click()

        # Переход в профиль
        WebDriverWait(driver, 10).until(
            lambda d: d.find_element(*PROFILE_BUTTON).is_displayed() and d.find_element(*PROFILE_BUTTON).is_enabled()
        )
        driver.find_element(*PROFILE_BUTTON).click()

        # Ожидание загрузки профиля
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(PROFILE_HEADER))

        # Скролл к блоку объявлений
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(MY_ADS_SECTION))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", driver.find_element(*MY_ADS_SECTION))

        # Ожидание загрузки карточек
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(ADS_CARD))
        WebDriverWait(driver, 10).until(
            lambda d: d.find_elements(*ADS_CARD) or "Здесь пока ничего нет" in d.page_source
        )
        cards = driver.find_elements(*ADS_CARD)
        assert cards, "Карточки не появились — блок пустой"

        # Поиск нужной карточки по всем страницам
        found = False
        prev_first_title = ""

        while True:
            cards = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located(ADS_CARD))

            for card in cards:
                try:
                    title_el = card.find_element(*ADS_TITLE)
                    price_el = card.find_element(*ADS_PRICE)
                    city_el = card.find_element(*ADS_CITY)

                    title = title_el.text.strip().lower()
                    price = price_el.text.strip().replace(" ", "").replace("₽", "")
                    city = city_el.text.strip().lower()
                    normalized_city = re.sub(r"\W+", "", city)

                    if (
                        title == "новый велосипед" and
                        price == "5000" and
                        normalized_city == "санктпетербург"
                    ):
                        found = True
                        break
                except:
                    continue

            if found:
                break

            try:
                prev_first_title = cards[0].find_element(*ADS_TITLE).text
            except:
                prev_first_title = ""

            try:
                next_btn = WebDriverWait(driver, 3).until(EC.element_to_be_clickable(PAGINATION_NEXT_BTN))
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", next_btn)
                next_btn.click()
                WebDriverWait(driver, 5).until(
                    lambda d: d.find_elements(*ADS_TITLE) and
                              d.find_elements(*ADS_TITLE)[0].text != prev_first_title
                )
            except:
                break

        assert found, "❌ Объявление не найдено ни на одной странице"