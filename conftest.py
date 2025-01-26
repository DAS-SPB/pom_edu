import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def create_driver(browser_name, headless):
    """Create driver based on browser name"""
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")
        return webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        options = FirefoxOptions()
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")
        return webdriver.Firefox(options=options)

    elif browser_name == "edge":
        options = EdgeOptions()
        options.add_argument("--window-size=1920,1080")
        if headless:
            options.add_argument("--headless")
        return webdriver.Edge(options=options)

    else:
        raise ValueError(f"Unsupported browser: {browser_name}. Options: chrome, firefox, edge")


def pytest_add_option(parser):
    """Adding a command line parameter to select a browser"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on. Options: chrome, firefox, edge",
    )
    parser.addoption(
        "--headless",
        action="store_true",  # This makes the option a flag (boolean)
        help="Run tests in headless mode. By default, it is False (headed mode).",
    )


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    """Fixture for creating a web driver"""
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    driver = create_driver(browser_name, headless)
    request.cls.driver = driver
    yield driver
    driver.quit()
