import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.service import Service
import time


class ChromeSoraTest(unittest.TestCase):

    def setUp(self):
        options = ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1050)
        self.driver.maximize_window()

    def test_play_all_sounds(self):
        driver = self.driver
        actions = ActionChains(driver)  # Initialize Mouse Actions
        driver.get("https://openai.com/sora/")
        wait = WebDriverWait(driver, 15)

        # Base XPath for the Cards
        card_xpath_base = "//div[contains(@class, 'snap-center') and .//span[contains(text(), 'Play sound')]]"

        # Wait for cards to load
        wait.until(EC.presence_of_element_located((By.XPATH, card_xpath_base)))
        cards_found = driver.find_elements(By.XPATH, card_xpath_base)
        print(f"Found {len(cards_found)} video cards.")

        # --- UPDATED LOOP: Only check the first 3 ---
        # We use min() to ensure we don't crash if there are fewer than 3 videos
        limit = min(3, len(cards_found))

        for i in range(1, limit + 1):
            try:
                print(f"\n--- Processing Video #{i} ---")

                # 1. Find the Card Container
                current_card_xpath = f"({card_xpath_base})[{i}]"
                card = wait.until(EC.presence_of_element_located((By.XPATH, current_card_xpath)))

                # 2. Scroll Logic
                # Since we are only doing the first 3, 'center' is safe for all of them
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", card)

                time.sleep(1.5)  # Allow scroll animation to finish

                # 3. HOVER over the card
                actions.move_to_element(card).perform()
                time.sleep(0.5)

                # 4. Find and Click the button
                play_button = card.find_element(By.XPATH, ".//span[contains(text(), 'Play sound')]")

                # We wait until the button is actually visible/clickable
                wait.until(EC.element_to_be_clickable(play_button))

                # Try Standard Click first, Fallback to JS Click
                try:
                    play_button.click()
                except:
                    driver.execute_script("arguments[0].click();", play_button)

                print(f"SUCCESS: Clicked 'Play sound' for video #{i}")

                # Wait for a bit of audio to play
                time.sleep(2)

            except Exception as e:
                print(f"FAILED on Video #{i}. \nReason: {str(e).splitlines()[0]}")

    def tearDown(self):
        self.driver.quit()


class FirefoxSoraTest(unittest.TestCase):
    def setUp(self):
        options = FirefoxOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        # options.add_experimental_option("detach", True) # Firefox doesn't support this exactly like Chrome

        # Set binary location BEFORE creating the driver
        options.binary_location = "/Applications/Firefox.app/Contents/MacOS/firefox"

        # Use the Homebrew-installed geckodriver directly (avoids auto-download mismatch)
        service = Service("/opt/homebrew/bin/geckodriver")

        try:
            self.driver = webdriver.Firefox(service=service, options=options)
            self.driver.set_window_size(1920, 1050)
            self.driver.maximize_window()  # Matches your Chrome setup
        except Exception as e:
            print(f"Firefox initialization failed: {e}")
            raise

    def test_play_all_sounds(self):
        driver = self.driver
        actions = ActionChains(driver)  # Initialize Mouse Actions
        driver.get("https://openai.com/sora/")
        wait = WebDriverWait(driver, 15)

        # Base XPath for the Cards
        card_xpath_base = "//div[contains(@class, 'snap-center') and .//span[contains(text(), 'Play sound')]]"

        # Wait for cards to load
        wait.until(EC.presence_of_element_located((By.XPATH, card_xpath_base)))
        cards_found = driver.find_elements(By.XPATH, card_xpath_base)
        print(f"Found {len(cards_found)} video cards.")

        # --- UPDATED LOOP: Only check the first 3 ---
        # We use min() to ensure we don't crash if there are fewer than 3 videos
        limit = min(3, len(cards_found))

        for i in range(1, limit + 1):
            try:
                print(f"\n--- Processing Video #{i} ---")

                # 1. Find the Card Container
                current_card_xpath = f"({card_xpath_base})[{i}]"
                card = wait.until(EC.presence_of_element_located((By.XPATH, current_card_xpath)))

                # 2. Scroll Logic
                # Since we are only doing the first 3, 'center' is safe for all of them
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", card)

                time.sleep(1.5)  # Allow scroll animation to finish

                # 3. HOVER over the card
                actions.move_to_element(card).perform()
                time.sleep(0.5)

                # 4. Find and Click the button
                play_button = card.find_element(By.XPATH, ".//span[contains(text(), 'Play sound')]")

                # We wait until the button is actually visible/clickable
                wait.until(EC.element_to_be_clickable(play_button))

                # Try Standard Click first, Fallback to JS Click
                try:
                    play_button.click()
                except:
                    driver.execute_script("arguments[0].click();", play_button)

                print(f"SUCCESS: Clicked 'Play sound' for video #{i}")

                # Wait for a bit of audio to play
                time.sleep(2)

            except Exception as e:
                print(f"FAILED on Video #{i}. \nReason: {str(e).splitlines()[0]}")

    def tearDown(self):
        self.driver.quit()


class EdgeSoraTest(unittest.TestCase):
    def setUp(self):
        options = EdgeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=options)
        self.driver.set_window_size(1920, 1050)
        self.driver.maximize_window()

    def test_play_all_sounds(self):
        driver = self.driver
        actions = ActionChains(driver)  # Initialize Mouse Actions
        driver.get("https://openai.com/sora/")
        wait = WebDriverWait(driver, 15)

        # Base XPath for the Cards
        card_xpath_base = "//div[contains(@class, 'snap-center') and .//span[contains(text(), 'Play sound')]]"

        # Wait for cards to load
        wait.until(EC.presence_of_element_located((By.XPATH, card_xpath_base)))
        cards_found = driver.find_elements(By.XPATH, card_xpath_base)
        print(f"Found {len(cards_found)} video cards.")

        # --- UPDATED LOOP: Only check the first 3 ---
        # We use min() to ensure we don't crash if there are fewer than 3 videos
        limit = min(3, len(cards_found))

        for i in range(1, limit + 1):
            try:
                print(f"\n--- Processing Video #{i} ---")

                # 1. Find the Card Container
                current_card_xpath = f"({card_xpath_base})[{i}]"
                card = wait.until(EC.presence_of_element_located((By.XPATH, current_card_xpath)))

                # 2. Scroll Logic
                # Since we are only doing the first 3, 'center' is safe for all of them
                driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", card)

                time.sleep(1.5)  # Allow scroll animation to finish

                # 3. HOVER over the card
                actions.move_to_element(card).perform()
                time.sleep(0.5)

                # 4. Find and Click the button
                play_button = card.find_element(By.XPATH, ".//span[contains(text(), 'Play sound')]")

                # We wait until the button is actually visible/clickable
                wait.until(EC.element_to_be_clickable(play_button))

                # Try Standard Click first, Fallback to JS Click
                try:
                    play_button.click()
                except:
                    driver.execute_script("arguments[0].click();", play_button)

                print(f"SUCCESS: Clicked 'Play sound' for video #{i}")

                # Wait for a bit of audio to play
                time.sleep(2)

            except Exception as e:
                print(f"FAILED on Video #{i}. \nReason: {str(e).splitlines()[0]}")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(ChromeSoraTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(FirefoxSoraTest))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(EdgeSoraTest))

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)