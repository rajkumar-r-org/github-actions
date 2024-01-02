from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

url = sys.argv[1]  # Get URL from command line argument
expected_title = sys.argv[2]  # Get expected title from command line argument
expected_text = sys.argv[3]  # Get expected text from command line argument

options = Options()
options.add_argument("--headless")  # Ensure GUI is off for GitHub Actions
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get(url)

# Check if the expected title is in the page title
if expected_title in driver.title:
    print(f"Title check passed: Found '{expected_title}' in the page title.")
else:
    print(f"Title check failed: Did not find '{expected_title}' in the page title.")
    sys.exit(1)  # Exit with a non-zero status code to indicate failure

# Check if the expected text is in the page source
if expected_text in driver.page_source:
    print(f"Content check passed: Found '{expected_text}' in the page source.")
else:
    print(f"Content check failed: Did not find '{expected_text}' in the page source.")
    sys.exit(1)  # Exit with a non-zero status code to indicate failure

driver.quit()
