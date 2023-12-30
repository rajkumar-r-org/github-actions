# importing required package of webdriver
from selenium import webdriver
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
# Just Run this to execute the below script

e_serv = Service(EdgeChromiumDriverManager().install())
e_opts=Options()
e_opts.add_argument("--headless")


# Instantiate the webdriver with the executable location of MS Edge web driver
options = webdriver.EdgeOptions(Service= e_serv, options=e_opts)
browser = webdriver.Edge(options=options)
# Simply just open a new Edge browser and go to lambdatest.com
browser.get('https://www.google.com')
print(browser.title)
assert "Google" in browser.title
# closing the browser
print(browser.page_source)
browser.implicitly_wait(5)
browser.quit()
