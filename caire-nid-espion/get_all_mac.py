# With selenium, get all elements of mac address from the website
# and save print it

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

# Open the website

driver = webdriver.Chrome()
driver.get("https://www.macvendorlookup.com/search/apple")
time.sleep(5)

# Get all elements of mac address in <code> tag
macs = driver.find_elements(By.TAG_NAME, "code")

# Keep only the 17 first characters of each mac address
macs_clean = []
for mac in macs:
    m = mac.text[:8]
    # To lower case
    m = m.lower()
    macs_clean.append(m)

# Write it to a file
with open("macs.txt", "w") as f:
    for mac in macs_clean:
        f.write(mac + "\n")

# Close the browser
driver.close()