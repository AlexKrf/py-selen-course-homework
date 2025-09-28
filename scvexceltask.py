import csv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from datetime import datetime
import scv
import openpyxl
import time
options=Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

driver.get("https://www.google.com/")
time.sleep(5)
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

title = driver.title
print("title of the page", title)
screenshot_name = f"screenshot_{timestamp}.png"
driver.save_screenshot("screenshot_name.png")
print("screenshot saved to", screenshot_name)

with open ("google_title.csv", mode='w', newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["page title"])
    writer.writerow([title])

print(f'"google_title.csv was created in {title}"')

workbook = openpyxl.Workbook()
sheet = workbook.active

sheet.append(["Title"])
sheet.append([title])

workbook.save('titles.xlsx')
workbook.close()
print("Title saved in Excel sheet")

with open ("logfile.text", "a") as log_file:
    log_file.write("title"+title+"\n")
    print("logfile saved to logfile.text")

driver.quit()




