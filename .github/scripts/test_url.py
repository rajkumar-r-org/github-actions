import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType
from selenium.webdriver.chrome.options import Options

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
website = sys.argv[1]
driver.get(website)
time.sleep(pause) #For pages that may take time to fully load

title = sys.argv[2]  # Get expected title from command line argument
expected_string = sys.argv[3]  # Get expected tag from command line argument

try:
    assert title in driver.title
    print("Test 1: Passed - {title}")
except AssertionError:
    print(f"Test 1: Failed - {title}")

try:
    #elements = driver.pagesource
    assert expected_string in driver.pagesource
    print(f"Test 2: Passed - Expected string {expected_string}")
except AssertionError:
    print(f"Test 2: Failed - Expected string {expected_string}")

driver.quit()
