from selenium import webdriver
import pytest
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
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
    search_field = browser.find_element(By.XPATH, '//input[@type="search"]')
    search_field.send_keys("QA course")
    search_field.send_keys(Keys.ENTER)

def test_book_buttons(browser):
    book_buttons = browser.find_elements(By.XPATH, '//a[@data-hook="book-button-button"]')
    book_buttons[0].click()

def test_questions(browser):
    name_field = browser.find_element(By.XPATH, '//input[@aria-label="First name"]')
    name_field.send_keys(name)
    lName_field = browser.find_element(By.XPATH, '//input[@aria-label="Last name"]')
    lName_field.send_keys(last_name)
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