# screenshot_domains.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# Read your domains
with open("domains.txt", "r") as f:
    domains = [line.strip() for line in f.readlines()]

# Set up Selenium headless Chrome
options = Options()
options.add_argument("--headless")  # Don't open a GUI window
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

service = Service(executable_path="/usr/bin/chromedriver")
driver = webdriver.Chrome(service=service, options=options)

for domain in domains:
    url = "http://" + domain  # Force HTTP (unless challenge uses HTTPS)
    try:
        driver.get(url)
        time.sleep(2)  # wait for page to load
        filename = domain.replace('.', '_') + ".png"
        driver.save_screenshot(filename)
        print(f"[+] Screenshot saved: {filename}")
    except Exception as e:
        print(f"[-] Failed to load {url}: {e}")

driver.quit()
