from selenium import webdriver
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from faker import Faker
fake = Faker()


name = fake.first_name()
last_name = fake.last_name()
email = fake.email()
phone_number = fake.phone_number()
question = fake.sentence()+"?"

@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.qaonlineacademy.com/")
    time.sleep(5)
    yield driver
    driver.quit()

def test_search(browser):
    search_field = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="search"]'))
    )
    search_field.send_keys("QA course")
    search_field.send_keys(Keys.ENTER)

    results = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//h1 | //h2 | //p'))
    )
    assert any("QA" in r.text for r in results), "Search results do not contain 'QA'"

def test_book_buttons(browser):
    book_buttons = browser.find_elements(By.XPATH, '//a[@data-hook="book-button-button"]')
    book_buttons[0].click()
    schedule_calendar = WebDriverWait(browser, 10).until(
        EC.presesence_of_element_located(By.XPATH, '//h1[@id]')
    )
    assert schedule_calendar.is_displayed(), "No schedule not displayed"

def test_questions(browser):
    name_field = browser.find_element(By.XPATH, '//input[@aria-label="First name"]')
    name_field.send_keys(name)

    lName_field = browser.find_element(By.XPATH, '//input[@aria-label="Last name"]')
    lName_field.send_keys(last_name)

    country_selector = browser.find_element(By.XPATH, '//button[@data-hook="country-selector-trigger"]')
    country_selector.click()

    israel_selector = browser.find_element(By.XPATH, '//span[@aria-label="Israel"]')
    israel_selector.click()

    phone_field = browser.find_element(By.XPATH, '//input[@aria-label="Phone. Phone"]')
    phone_field.send_keys(phone_number)

    question_field = browser.find_element(By.XPATH, '//input[@aria-label="Ask Your Question"]')
    question_field.send_keys(question)

    submit_button = browser.find_element(By.XPATH, '//button[@data-hook="submit-button"]')
    submit_button.click()



def test_expand_button(browser):
    expand_button_b = browser.find_element(By.XPATH, '//span[@data-testid="stylablebutton-label"]')
    expand_button_b.click()
    programList_button = browser.find_element(By.XPATH, '//a[@href="https://www.qaonlineacademy.com/challenges"]')
    programList_button.click()
    assert "challenges" in browser.current_url

    # search_field = '//input[@type="search"]'
    # book_buttons = '//a[@data-hook="book-button-button"]'
    # name_field = '//input[@aria-label="First name"]'
    # lName_field = '//input[@aria-label="Last name"]'
    # email_field = '//input[@aria-label="email"]'
    # phone_field = '//input[@aria-label="Phone. Phone"]'
    # question_field = '//input[@aria-label="Ask Your Question"]'
    # submit_button = '//button[@data-hook="submit-button"]'
    # expand_button_b = '//span[@data-testid="stylablebutton-label"]'
    # programList_button = '//a[@href="https://www.qaonlineacademy.com/challenges"]'