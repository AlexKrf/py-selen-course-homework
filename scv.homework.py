import csv

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import pytest

loginContainer = "//div[@id='login-container']"
registerContainer = "//div[@id='register-container']"
toggle = "//p"
button = "//button"

data =[
    ["username","password"],
    ["user1","password1"],
    ["user2","password2"],
    ["user3","password3"]
]
with open("users.scv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print("Data written to users.scv")

driver = webdriver.Chrome()
driver.get("file:///C:/Users/alexander/Downloads/login.html")
driver.maximize_window()

with open("users.scv", "r", newline="") as file:
    reader = csv.reader(file)
    next(reader)

    #driver.find_element(By.XPATH, loginContainer + toggle).click()

    for row in reader:
        username, password = row
        driver.find_element(By.XPATH, loginContainer + toggle).click()
        driver.find_element(By.ID, "register-username").clear()
        driver.find_element(By.ID, "register-username").send_keys(username)
        driver.find_element(By.ID, "register-password").clear()
        driver.find_element(By.ID, "register-password").send_keys(password)
        driver.find_element(By.XPATH, registerContainer+button).click()
        #time.sleep(2)
        alert = driver.switch_to.alert
        alert.accept()
        driver.find_element(By.ID, "login-username").clear()
        driver.find_element(By.ID, "login-username").send_keys(username)
        driver.find_element(By.ID, "login-password").clear()
        driver.find_element(By.ID, "login-password").send_keys(password)
        driver.find_element(By.XPATH, loginContainer + button).click()
        alert = driver.switch_to.alert
        alert.accept()

        #time.sleep (2)
