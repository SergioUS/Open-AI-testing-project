import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.edge.options import Options as Edge_Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
            driver.get("https://openai.com/sora/")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")
            driver.save_screenshot("Chrome_Screenshot_5.png")

            self.assertIn("Sora", driver.title, f"Title check failed: {driver.title}")
            print("✓ Title check passed")

            wait = WebDriverWait(driver, 15)

            # Scroll down to find the ghost icon
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            # Find the ghost icon using the section class
            ghost_icon = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//section[contains(@class, 'relative') and contains(@class, 'flex')]//div[contains(@class, 'absolute') and contains(@class, 'left-0') and contains(@class, 'top-0')]"
            )))

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ghost_icon)
            time.sleep(1)
            driver.save_screenshot("Chrome_Screenshot_2.png")

            print("✓ Found ghost icon, clicking 50 times...")
            for i in range(50):
                try:
                    driver.execute_script("arguments[0].click();", ghost_icon)
                    print(f"  Click {i + 1}/50")
                    time.sleep(0.3)
                except Exception as e:
                    print(f"  Click {i + 1}/50 failed: {e}")
                    time.sleep(0.3)

            print("✓ Completed 50 clicks")
            driver.save_screenshot("Chrome_Screenshot_5.1.png")

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
            driver.get("https://openai.com/sora/")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")
            driver.save_screenshot("Firefox_Screenshot_5.png")

            self.assertIn("Sora", driver.title, f"Title check failed: {driver.title}")
            print("✓ Title check passed")

            wait = WebDriverWait(driver, 15)

            # Scroll down to find the ghost icon
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            # Find the ghost icon
            ghost_icon = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//section[contains(@class, 'relative') and contains(@class, 'flex')]//div[contains(@class, 'absolute') and contains(@class, 'left-0') and contains(@class, 'top-0')]"
            )))

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ghost_icon)
            time.sleep(1)
            driver.save_screenshot("Firefox_Screenshot_2.png")

            print("✓ Found ghost icon, clicking 50 times...")
            for i in range(50):
                try:
                    driver.execute_script("arguments[0].click();", ghost_icon)
                    print(f"  Click {i + 1}/50")
                    time.sleep(0.3)
                except Exception as e:
                    print(f"  Click {i + 1}/50 failed: {e}")
                    time.sleep(0.3)

            print("✓ Completed 50 clicks")
            driver.save_screenshot("Firefox_Screenshot_5.1.png")

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
            driver.get("https://openai.com/sora/")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")
            driver.save_screenshot("Edge_Screenshot_5.png")

            self.assertIn("Sora", driver.title, f"Title check failed: {driver.title}")
            print("✓ Title check passed")

            wait = WebDriverWait(driver, 15)

            # Scroll down to find the ghost icon
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

            # Find the ghost icon
            ghost_icon = wait.until(EC.element_to_be_clickable((
                By.XPATH,
                "//section[contains(@class, 'relative') and contains(@class, 'flex')]//div[contains(@class, 'absolute') and contains(@class, 'left-0') and contains(@class, 'top-0')]"
            )))

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", ghost_icon)
            time.sleep(1)
            driver.save_screenshot("Edge_Screenshot_2.png")

            print("✓ Found ghost icon, clicking 50 times...")
            for i in range(50):
                try:
                    driver.execute_script("arguments[0].click();", ghost_icon)
                    print(f"  Click {i + 1}/50")
                    time.sleep(0.3)
                except Exception as e:
                    print(f"  Click {i + 1}/50 failed: {e}")
                    time.sleep(0.3)

            print("✓ Completed 50 clicks")
            driver.save_screenshot("Edge_Screenshot_5.1.png")

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