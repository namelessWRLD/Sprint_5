import random
import string
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def generate_email():
    return "user_" + ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)) + "@test.com"


class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()

        email = generate_email()
        driver.find_element(*REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REG_PASSWORD_INPUT).send_keys("ValidPass123")
        driver.find_element(*REG_REPEAT_PASSWORD_INPUT).send_keys("ValidPass123")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(USER_NAME_HEADER))
        assert driver.find_element(*USER_NAME_HEADER).text == "User."

    def test_registration_invalid_email(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()

        driver.find_element(*REG_EMAIL_INPUT).send_keys("invalid-email")
        driver.find_element(*REG_PASSWORD_INPUT).send_keys("12345678")
        driver.find_element(*REG_REPEAT_PASSWORD_INPUT).send_keys("12345678")

        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EMAIL_ERROR))
        assert driver.find_element(*EMAIL_ERROR).text == "Ошибка"

    def test_registration_existing_user(self, driver):
        driver.get("https://qa-desk.stand.praktikum-services.ru/")
        driver.find_element(*LOGIN_REGISTER_BUTTON).click()
        driver.find_element(*NO_ACCOUNT_BUTTON).click()

        driver.find_element(*REG_EMAIL_INPUT).send_keys("dadada@test.ru")
        driver.find_element(*REG_PASSWORD_INPUT).send_keys("123456789")
        driver.find_element(*REG_REPEAT_PASSWORD_INPUT).send_keys("123456789")
        driver.find_element(*CREATE_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 5).until(EC.visibility_of_element_located(EXISTING_USER_ERROR))
        assert driver.find_element(*EXISTING_USER_ERROR).text == "Ошибка"
	