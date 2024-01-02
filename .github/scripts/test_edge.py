import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

def test_content():
    url = sys.argv[1]  # Get URL from command line argument
    expected_title = sys.argv[2]  # Get expected title from command line argument
    expected_text = sys.argv[3]  # Get expected text from command line argument

    options = Options()
    options.add_argument("--headless")  # Ensure GUI is off for GitHub Actions
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    assert driver.title == expected_title, f"Expected title '{expected_title}', but got '{driver.title}'"

    paragraphs = driver.find_elements_by_tag_name('p')
    assert any(expected_text in p.text for p in paragraphs), f"Expected text '{expected_text}' not found in any <p> element"

    driver.quit()
