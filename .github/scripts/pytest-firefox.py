from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def test_url_title():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://dotnetappgithubactions.azurewebsites.net/")
    print("Title: ", driver.title)
