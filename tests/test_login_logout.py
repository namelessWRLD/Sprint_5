from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


def test_user_login(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru")
    driver.find_element(*LOGIN_REGISTER_BUTTON).click()

    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("dadada@test.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456789")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(USER_NAME_HEADER))
    
    assert driver.find_element(*USER_NAME_HEADER).text == "User."

def test_user_logout(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru")
    driver.find_element(*LOGIN_REGISTER_BUTTON).click()
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys("dadada@test.ru")
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys("123456789")
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(USER_NAME_HEADER))

    WebDriverWait(driver, 5).until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()

    WebDriverWait(driver, 7).until(EC.visibility_of_element_located(LOGIN_REGISTER_BUTTON))

    assert driver.find_element(*LOGIN_REGISTER_BUTTON).is_displayed()
