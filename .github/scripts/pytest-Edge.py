import pytest
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.edge.options import Options


@pytest.fixture
def browser():

    opts = Options()
    opts.add_argument("headless")
    driver = webdriver.Edge(options = opts)
    driver.implicitly_wait(5)

    yield driver

    # For cleanup, quit the driver
    driver.quit()


def test_get_title(browser):
    browser.get("https://dotnetappgithubactions.azurewebsites.net/")

    assert 'Web App - Unavailable' == browser.title

    elements=browser.page_source
    print(browser.title)

    assert  'currently stopped' in elements
    print('Web App is Stopped')
