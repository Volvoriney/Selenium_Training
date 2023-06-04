from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def test_1():
    # Inputs

    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit"]')
    # MAIN_MENU = (By.CSS_SELECTOR, '[data-testid="main-menu"]>div>svg')
    MAIN_MENU = (By.CSS_SELECTOR, '[data-testid="main-menu"] div[role="button"]')
    PAGES = (By.XPATH, '//li[text()="Pages"]')

    # Steps
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(20)

    driver.find_element(*EMAIL_INPUT).send_keys(user)
    driver.find_element(*PASSWORD_INPUT).send_keys(pwd)
    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*MAIN_MENU).click()
    driver.find_element(*PAGES)
    #
    driver.close()
