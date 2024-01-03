import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from bs4 import BeautifulSoup

def pytest_addoption(parser):
    parser.addoption("--url", action="store")
    parser.addoption("--title", action="store")
    parser.addoption("--element", action="store")

@pytest.fixture
def url(request):
    return request.config.getoption("--url")

@pytest.fixture
def title(request):
    return request.config.getoption("--title")

@pytest.fixture
def element(request):
    return request.config.getoption("--element")

@pytest.fixture
def browser():
    opts = Options()
    opts.add_argument("headless")
    chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver = webdriver.Chrome(service=chrome_service, options=opts)
    driver.implicitly_wait(5)

    yield driver

def test_get_title(browser, url, title):
    browser.get(url)
    try:
        assert title == browser.title
    finally:
        browser.quit()

def test_get_element(browser, url, element):
    browser.get(url)
    try:
        elements = browser.page_source
        soup = BeautifulSoup(elements, 'html.parser')
        assert soup.text.find(element) != -1
    finally:
        browser.quit()
