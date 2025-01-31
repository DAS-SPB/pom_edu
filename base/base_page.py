import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.PAGE_URL = None
        self.PAGE_TITLE = None
        self.PAGE_NAME = self.__class__.__name__
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_NAME} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self):
        with allure.step(f"Page {self.PAGE_NAME} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))
            self.wait.until(EC.title_is(self.PAGE_TITLE))
