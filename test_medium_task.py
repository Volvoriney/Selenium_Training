from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from datetime import timedelta, date, datetime


def test_recieved_on_filter():
    # Inputs

    # Selectors
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-testid="email"]')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '[data-testid="password"]')
    LOGIN_BUTTON = (By.CSS_SELECTOR, '[data-testid="submit"]')
    MAIN_MENU = (By.CSS_SELECTOR, '[data-testid="main-menu"] div[role="button"]')
    PAYMENTS_REPORTING = (By.XPATH, '//span[text()="Payments Reporting"]')
    RECEIVED_ON_START_DATE = (By.CSS_SELECTOR, '[data-testid="calendar-field-1"]')
    RECEIVED_ON_SORTING = (By.XPATH, '//span[text()="Received on"]')
    TRANSACTION_LIST_RECEIVED_DATE = (By.CSS_SELECTOR, '[data-testid="received-on"]')

    # Timeout Value
    main_timeout = 10

    # Calculate 15 days ago date
    today = date.today()
    half_month_ago = today - timedelta(days=15)
    half_of_month_ago_formatted = half_month_ago.strftime("%m/%d/%Y")

    def get_element_on_visibility(selector):
        return WebDriverWait(driver, main_timeout).until(
        expected_conditions.visibility_of_element_located(selector)
    )

    # Driver setup part
    driver = webdriver.Chrome()

    # Getting stage url
    driver.get(url)

    # Authorization
    email_input = get_element_on_visibility(EMAIL_INPUT)
    email_input.send_keys(user)
    password = get_element_on_visibility(PASSWORD_INPUT)
    password.send_keys(pwd)
    login_button = get_element_on_visibility(LOGIN_BUTTON)
    login_button.click()

    # Navigate to Payments Reporting
    main_menu = get_element_on_visibility(MAIN_MENU)
    main_menu.click()
    payments_reporting_bar = get_element_on_visibility(PAYMENTS_REPORTING)
    payments_reporting_bar.click()

    # Change start date
    recieved_start_date = get_element_on_visibility(RECEIVED_ON_START_DATE)
    recieved_start_date.click()
    recieved_start_date.send_keys(Keys.COMMAND, "a")
    recieved_start_date.send_keys(Keys.DELETE)
    recieved_start_date.send_keys(half_of_month_ago_formatted)
    recieved_start_date.send_keys(Keys.ESCAPE)

    # Change sorting of list by Recived On asc to see earliest records by date range
    received_on_sorting = get_element_on_visibility(RECEIVED_ON_SORTING)
    received_on_sorting.click()

    # Getting values from transactions list
    first_transaction_date = get_element_on_visibility(TRANSACTION_LIST_RECEIVED_DATE).get_attribute("innerText")

    # Making date format from got string
    transaction_date = datetime.strptime(first_transaction_date, '%b %d, %Y').date()

    # Check if earliest records are getting into range
    assert transaction_date >= half_month_ago
