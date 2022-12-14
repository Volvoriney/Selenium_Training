import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_payments_reporting_title():

    # Inputs
    user = "bogdan_DSO@zentist.io"
    pwd = "uJN7GdsHvXgEGtLZCF3I"
    url = "https://stage.zentist.io/"

    # Selectors
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit"]')
    MAIN_MENU = (By.CSS_SELECTOR, '[data-testid="main-menu"] div[role="button"]')
    PAYMENTS_REPORTING = (By.XPATH, '//span[text()="Payments Reporting"]')
    PAYMENTS_REPORTING_TITLE = (By.XPATH, '//h1[text()="Payments Reporting"]')

    # Driver setup part
    driver = webdriver.Chrome()

    # Getting stage url
    driver.get(url)

    # Authorization
    driver.find_element(*EMAIL_INPUT).send_keys(user)
    driver.find_element(*PASSWORD_INPUT).send_keys(pwd)
    driver.find_element(*LOGIN_BUTTON).click()
    time.sleep(5)

    # Navigating to Payments Reporting
    driver.find_element(*MAIN_MENU).click()
    driver.find_element(*PAYMENTS_REPORTING).click()
    time.sleep(5)

    # Confirmation by title that I am on correct page
    assert driver.find_element(*PAYMENTS_REPORTING_TITLE).get_attribute("innerText") == "Payments Reporting"

