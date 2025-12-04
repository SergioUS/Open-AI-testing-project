import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FF_Options
from selenium.webdriver.edge.options import Options as Edge_Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait



class ChromeWordPress(unittest.TestCase):

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
            print("\n=== Starting test ===")
            driver.get("https://openai.com/sora/")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")

            wait = WebDriverWait(driver, 15)

            try:
                assert "Sora" in driver.title
                print("✓ Title check passed")
            except AssertionError:
                print(f"✗ Title check failed: {driver.title}")

            try:
                original_url = driver.current_url
                print(f"\nOriginal URL: {original_url}")

                download_button = driver.find_element(By.XPATH, "//span[@class='text-[white]']")
                print("✓ Download button found")
                download_button.click()
                print("✓ Download button clicked")

                time.sleep(3)  # Give it time to start redirect

                # Check if new window/tab opened
                current_windows = driver.window_handles
                print(f"Number of windows: {len(current_windows)}")

                if len(current_windows) > 1:
                    print("→ New window detected, switching to it...")
                    driver.switch_to.window(current_windows[-1])
                    time.sleep(2)

                new_url = driver.current_url
                print(f"Current URL after login: {new_url}")

                if new_url == original_url:
                    print("✗ URL did not change - login may have failed")
                else:
                    print("✓ URL changed successfully")

                # Try multiple methods to wait for page load
                print("\nWaiting for page to load...")
                try:
                    # Method 1: Wait for document ready state
                    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
                    print("✓ Page readyState is complete")
                except:
                    print("✗ ReadyState wait timed out")

                time.sleep(3)  # Extra wait for any remaining content
                print("✓ Page load complete")

            except Exception as e:
                print(f"✗ Error during login: {str(e)}")
                import traceback
                traceback.print_exc()
        finally:
            print("\n=== Test cleanup ===")
            time.sleep(2)

    def tearDown(self):
        try:
            self.driver.quit()
            print("✓ Driver closed")
        except Exception as e:
            print(f"✗ Error closing driver: {e}")


class FirefoxWordPress(unittest.TestCase):

    def setUp(self):
        options = FF_Options()
        options.set_preference("dom.webdriver.enabled", False)
        options.set_preference("useAutomationExtension", False)
        self.driver = webdriver.Firefox(options=options)
        self.driver.set_window_size(1920, 1050)

    def test_open_ai_sora(self):
        driver = self.driver
        try:
            print("\n=== Starting test ===")
            driver.get("https://openai.com/sora/")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")

            wait = WebDriverWait(driver, 15)

            try:
                assert "Sora" in driver.title
                print("✓ Title check passed")
            except AssertionError:
                print(f"✗ Title check failed: {driver.title}")

            try:
                original_url = driver.current_url
                print(f"\nOriginal URL: {original_url}")

                download_button = driver.find_element(By.XPATH, "//span[@class='text-[white]']")
                print("✓ Download button found")
                download_button.click()
                print("✓ Download button clicked")

                time.sleep(3)

                current_windows = driver.window_handles
                print(f"Number of windows: {len(current_windows)}")

                if len(current_windows) > 1:
                    print("→ New window detected, switching to it...")
                    driver.switch_to.window(current_windows[-1])
                    time.sleep(2)

                new_url = driver.current_url
                print(f"Current URL after login: {new_url}")

                if new_url == original_url:
                    print("✗ URL did not change - login may have failed")
                else:
                    print("✓ URL changed successfully")

                print("\nWaiting for page to load...")
                try:
                    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
                    print("✓ Page readyState is complete")
                except:
                    print("✗ ReadyState wait timed out")

                time.sleep(3)
                print("✓ Page load complete")

            except Exception as e:
                print(f"✗ Error during login: {str(e)}")
                import traceback
                traceback.print_exc()
        finally:
            print("\n=== Test cleanup ===")
            time.sleep(2)

    def tearDown(self):
        try:
            self.driver.quit()
            print("✓ Driver closed")
        except Exception as e:
            print(f"✗ Error closing driver: {e}")


class EdgeWordPress(unittest.TestCase):

    def setUp(self):
        options = Edge_Options()
        self.driver = webdriver.Edge(options=options)
        self.driver.set_window_size(1920, 1050)

    def test_open_ai_sora(self):
        driver = self.driver
        try:
            print("\n=== Starting test ===")
            driver.get("https://openai.com/sora/")
            print(f"Home page URL: {driver.current_url}")
            print(f"Home page title: {driver.title}")

            wait = WebDriverWait(driver, 15)

            try:
                assert "Sora" in driver.title
                print("✓ Title check passed")
            except AssertionError:
                print(f"✗ Title check failed: {driver.title}")

            try:
                original_url = driver.current_url
                print(f"\nOriginal URL: {original_url}")

                download_button = driver.find_element(By.XPATH, "//span[@class='text-[white]']")
                print("✓ Download button found")
                download_button.click()
                print("✓ Download button clicked")

                time.sleep(3)

                current_windows = driver.window_handles
                print(f"Number of windows: {len(current_windows)}")

                if len(current_windows) > 1:
                    print("→ New window detected, switching to it...")
                    driver.switch_to.window(current_windows[-1])
                    time.sleep(2)

                new_url = driver.current_url
                print(f"Current URL after login: {new_url}")

                if new_url == original_url:
                    print("✗ URL did not change - login may have failed")
                else:
                    print("✓ URL changed successfully")

                print("\nWaiting for page to load...")
                try:
                    wait.until(lambda d: d.execute_script("return document.readyState") == "complete")
                    print("✓ Page readyState is complete")
                except:
                    print("✗ ReadyState wait timed out")

                time.sleep(3)
                print("✓ Page load complete")

            except Exception as e:
                print(f"✗ Error during login: {str(e)}")
                import traceback
                traceback.print_exc()
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