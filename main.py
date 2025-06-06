from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query = "mobile phone under 20000"
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=NZN6KNCSII19&sprefix=Mobile%2Caps%2C320&ref=nb_sb_ss_ts-doa-p-region-agnostic_2_6")
    elems = driver.find_elements(By.CLASS_NAME, "sg-col-20-of-24")
    print(f"{len(elems)} items found")
    for elem in elems:
        print(elem.text)

# print(element.get_attribute("outerHTML"))

time.sleep(2)
driver.close()