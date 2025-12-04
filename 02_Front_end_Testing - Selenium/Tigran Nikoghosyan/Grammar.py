import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
import language_tool_python

URL = "https://openai.com/sora/"
WAIT_TIMEOUT = 15


@pytest.fixture(scope="session")
def language_tool():
    tool = language_tool_python.LanguageTool('en-US')
    yield tool
    tool.close()


@pytest.fixture
def chrome_driver():
    options = ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    options = FirefoxOptions()
    options.add_argument("--width=1920")
    options.add_argument("--height=1080")
    driver = webdriver.Firefox(options=options)
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()


@pytest.fixture
def edge_driver():
    options = EdgeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=options)
    driver.set_page_load_timeout(10)
    yield driver
    driver.quit()


def test_header_grammar_chrome(chrome_driver, language_tool):
    try:
        chrome_driver.get(URL)
        wait = WebDriverWait(chrome_driver, WAIT_TIMEOUT)
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

        header_text = header.text.strip()
        matches = language_tool.check(header_text)

        assert len(matches) == 0
        print("✅ Chrome - Grammar is Ok:", header_text)
    except AssertionError:
        print("❌ Chrome - Grammar errors found:", [m.message for m in matches])
        raise


def test_header_grammar_firefox(firefox_driver, language_tool):
    try:
        firefox_driver.get(URL)
        wait = WebDriverWait(firefox_driver, WAIT_TIMEOUT)
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

        header_text = header.text.strip()
        matches = language_tool.check(header_text)

        assert len(matches) == 0
        print("✅ Firefox - Grammar is Ok:", header_text)
    except AssertionError:
        print("❌ Firefox - Grammar errors found:", [m.message for m in matches])
        raise


def test_header_grammar_edge(edge_driver, language_tool):
    try:
        edge_driver.get(URL)
        wait = WebDriverWait(edge_driver, WAIT_TIMEOUT)
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, "h1")))

        header_text = header.text.strip()
        matches = language_tool.check(header_text)

        assert len(matches) == 0
        print("✅ Edge - Grammar is Ok:", header_text)
    except AssertionError:
        print("❌ Edge - Grammar errors found:", [m.message for m in matches])
        raise