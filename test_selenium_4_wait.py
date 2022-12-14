import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_1():
    # Inputs
    user = "biller+demo@zentist.io"
    pwd = "ZVBJsGT2juVRm$WXirZbLLXLj"
    url = "https://stage.zentist.io/"

    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit"]')
    # MAIN_MENU = (By.CSS_SELECTOR, '[data-testid="main-menu"]>div>svg')
    MAIN_MENU = (By.CSS_SELECTOR, '[data-testid="main-menu"] div[role="button"]')
    PAGES = (By.XPATH, '//li[text()="Pages"]')

    # Driver setup part
    driver = webdriver.Chrome()

    # Steps
    driver.get(url)
    # driver.implicitly_wait(20)
    timeout_main = 20

    try:
        element = WebDriverWait(driver, timeout_main).until(
            expected_conditions.visibility_of_element_located(EMAIL_INPUT)
        )
        element.send_keys(user)
        time.sleep(5)
        # driver.find_element(*PASSWORD_INPUT).send_keys(pwd)
        # driver.find_element(*LOGIN_BUTTON).click()

        # driver.find_element(*MAIN_MENU).click()
        # driver.find_element(*PAGES)
    finally:
        driver.close()
        driver.quit()
