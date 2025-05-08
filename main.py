from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-gpu')

driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=options)

driver.get("https://example.com")
print("Page title:", driver.title)

time.sleep(2)
driver.quit()