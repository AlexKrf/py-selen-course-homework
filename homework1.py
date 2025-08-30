import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
actions = ActionChains(driver)

driver.get("file:///C:/Users/alexander/Downloads/ActionChains.Html")
driver.maximize_window()

#autorization part
username_field = driver.find_element(By.XPATH, "/html/body/main/section[1]/form/input[1]")
email_field = driver.find_element(By.XPATH, "/html/body/main/section[1]/form/input[2]")

username_field.send_keys("alexander")
email_field.send_keys("example.mail@gmail.com")
select_usertype = driver.find_element(By.XPATH, "/html/body/main/section[1]/form/select")
dropdown = Select(select_usertype)
dropdown.select_by_visible_text("בודק")


row1 = driver.find_element(By.XPATH, "/html/body/main/section[3]/div[1]/div[1]")
row2 = driver.find_element(By.XPATH, "/html/body/main/section[3]/div[1]/div[2]")
row3 = driver.find_element(By.XPATH, "/html/body/main/section[3]/div[1]/div[3]")
dropzone = driver.find_element(By.XPATH, "/html/body/main/section[3]/div[2]")

for rows in [row1, row2, row3]:
    actions.drag_and_drop(rows, dropzone).perform()

time.sleep(10)