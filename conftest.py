import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def create_driver(browser_name: str, headless: bool, remote: bool):

    browser_map = {
        "chrome": (webdriver.Chrome, ChromeOptions),
        "firefox": (webdriver.Firefox, FirefoxOptions),
        "edge": (webdriver.Edge, EdgeOptions),
    }

    if browser_name not in browser_map:
        raise ValueError(f"Unsupported browser: {browser_name}. Options: chrome, firefox, edge.")

    driver_class, options_class = browser_map.get(browser_name)
    options = options_class()

    # Common options
    options.add_argument("--window-size=1920,1080")

    # Specific options for Chrome
    if browser_name == "chrome":
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

    if headless:
        options.add_argument("--headless")

    if remote:
        return webdriver.Remote(
            command_executor="http://hub:4444/wd/hub",
            options=options
        )
    else:
        return driver_class(options=options)


def pytest_addoption(parser):
    """Adding a command line parameter to select a browser"""
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests on. Options: chrome, firefox, edge.",
    )
    parser.addoption(
        "--headless",
        action="store_true",  # This makes the option a flag (boolean)
        help="Run tests in headless mode. By default, it is False (headed mode).",
    )
    parser.addoption(
        "--remote",
        action="store_true",  # This makes the option a flag (boolean)
        help="Run tests in remote mode. By default, it is False (local mode).",
    )
    parser.addoption(
        "--env",
        action="store",
        default="https://www.saucedemo.com",
        help="Env host to run tests on.",
    )


@pytest.fixture(scope="function", autouse=True)
def driver(request):
    """Fixture for creating a web driver"""
    browser_name = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    remote = request.config.getoption("--remote")
    driver = create_driver(browser_name, headless, remote)
    request.cls.driver = driver
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def host(request):
    """Fixture for determining env host"""
    return request.config.getoption("--env")


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.failed and call.when == "call":
        driver = item.funcargs.get("driver", None)
        if driver:
            allure.attach(
                body=driver.get_screenshot_as_png(),
                name="screenshot-on-failure",
                attachment_type=AttachmentType.PNG
            )
