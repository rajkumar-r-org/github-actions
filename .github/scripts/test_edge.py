import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import sys

class TestWebContent(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = sys.argv[1]  # Get URL from command line argument
        cls.expected_title = sys.argv[2]  # Get expected title from command line argument
        cls.expected_text = sys.argv[3]  # Get expected text from command line argument

        options = Options()
        options.add_argument("--headless")  # Ensure GUI is off for GitHub Actions
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(cls.url)

    def test_title(self):
        self.assertEqual(self.driver.title, self.expected_title)

    def test_content(self):
        paragraphs = self.driver.find_elements_by_tag_name('p')
        self.assertTrue(any(self.expected_text in p.text for p in paragraphs))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=['first-arg-is-ignored'], exit=False)