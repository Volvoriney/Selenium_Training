from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def test_1():
    # Inputs

    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit"]')
    # MAIN_MENU = (By.CSS_SELECTOR, '[data-testid="main-menu"]>div>svg')
    MAIN_MENU = (By.CSS_SELECTOR, '[data-testid="main-menu"] div[role="button"]')
    PAGES = (By.XPATH, '//li[text()="Pages"]')

    # Driver setup part
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')  # Last I checked this was necessary.
    driver = webdriver.Chrome(chrome_options=options)

    # Steps
    driver.get(url)
    driver.implicitly_wait(20)

    driver.find_element(*EMAIL_INPUT).send_keys(user)
    driver.find_element(*PASSWORD_INPUT).send_keys(pwd)
    driver.find_element(*LOGIN_BUTTON).click()

    driver.find_element(*MAIN_MENU).click()
    driver.find_element(*PAGES)

    driver.close()
