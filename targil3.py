from selenium import webdriver
from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common import actions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
def create_driver():
    driver.get("file:///C:/Users/alexander/Downloads/ActionChainsEx.Html")
    driver.implicitly_wait(5)
    driver.maximize_window()
    return driver, actions
def close_driver(driver):
    driver.quit()

def click_box (driver):
    box = driver.find_element (By.ID, 'click-box')
    ActionChains(driver).click(box).perform()
def double_click_box(driver):
    box = driver.find_element (By.ID, 'double-box')
    ActionChains(driver).double_click(box).perform()
def right_click_box(driver):
    box = driver.find_element (By.ID, 'right-box')
    ActionChains(driver).context_click(box).perform()
def hold_box(driver):
    box = driver.find_element (By.ID, 'hold-box')
    ActionChains(driver).click_and_hold(box).perform()
    time.sleep(2)
def drag_box(driver):
    box = driver.find_element (By.ID, 'drag1')
    dropzone = driver.find_element(By.ID, 'dropzone')
    ActionChains(driver).drag_and_drop(box, dropzone).perform()
def hover_box(driver):
    box = driver.find_element (By.ID, 'hover-target')
    ActionChains(driver).move_to_element(box).perform()
def imput_field (driver):
    field = driver.find_element(By.ID, 'text-input')
    field.clear()
    field.send_keys('hello there')
    field.send_keys(Keys.RETURN)
    time.sleep(2)
def run_test():
    driver, actions = create_driver()
    click_box(driver)
    double_click_box(driver)
    right_click_box(driver)
    hold_box(driver)
    hover_box(driver)
    imput_field(driver)
    driver.quit()
    time.sleep (5)
try:
    run_test()
finally:
    close_driver(driver)