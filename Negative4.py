import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.edge.options import Options as Edge_Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ChromeSoraTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36")
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_page_load_timeout(60)
        self.driver.set_script_timeout(60)

    def test_open_ai_sora(self):
        driver = self.driver
        try:
            print("\n=== Starting Chrome test ===")
            driver.get("https://openai.com/sora/#12345")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")
            driver.save_screenshot("Chrome_Screenshot4.png")

            self.assertIn("Sora", driver.title, f"Title check failed: {driver.title}")
            print("✓ Title check passed")

        finally:
            print("\n=== Test cleanup ===")
            time.sleep(2)

    def tearDown(self):
        try:
            self.driver.quit()
            print("✓ Driver closed")
        except Exception as e:
            print(f"✗ Error closing driver: {e}")


class FirefoxSoraTest(unittest.TestCase):

    def setUp(self):
        options = FF_Options()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1920, 1050)

    def test_open_ai_sora(self):
        driver = self.driver
        try:
            print("\n=== Starting Firefox test ===")
            driver.get("https://openai.com/sora/#12345")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")
            driver.save_screenshot("Firefox_Screenshot4.png")

            self.assertIn("Sora", driver.title, f"Title check failed: {driver.title}")
            print("✓ Title check passed")

        finally:
            print("\n=== Test cleanup ===")
            time.sleep(2)

    def tearDown(self):
        try:
            self.driver.quit()
            print("✓ Driver closed")
        except Exception as e:
            print(f"✗ Error closing driver: {e}")


class EdgeSoraTest(unittest.TestCase):

    def setUp(self):
        options = Edge_Options()
        self.driver = webdriver.Edge(options=options)
        self.driver.set_window_size(1920, 1050)

    def test_open_ai_sora(self):
        driver = self.driver
        try:
            print("\n=== Starting Edge test ===")
            driver.get("https://openai.com/sora/#12345")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")
            driver.save_screenshot("Edge_Screenshot4.png")

            self.assertIn("Sora", driver.title, f"Title check failed: {driver.title}")
            print("✓ Title check passed")

        finally:
            print("\n=== Test cleanup ===")
            time.sleep(2)

    def tearDown(self):
        try:
            self.driver.quit()
            print("✓ Driver closed")
        except Exception as e:
            print(f"✗ Error closing driver: {e}")


if __name__ == "__main__":
    unittest.main()