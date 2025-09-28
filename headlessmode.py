from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=2560, 1440")

driver.get("google.com")
search_bar = driver.find_element(By.XPATH, '//*[@id="input"]')
search_bar.send_keys("python")
driver.save_screenshot("python_search_headless.png")
driver.close()
