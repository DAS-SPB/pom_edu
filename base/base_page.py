import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.PAGE_URL = None
        self.PAGE_NAME = self.__class__.__name__
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Open {self.PAGE_NAME} page"):
            self.driver.get(self.PAGE_URL)

    def is_opened(self, page_title: str):
        with allure.step(f"Page {self.PAGE_NAME} is opened"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))
            self.wait.until(EC.title_is(page_title))

    def make_screenshot(self, screenshot_name):
        allure.attach(
            body=self.driver.get_screenshot_as_png(),
            name=screenshot_name,
            attachment_type=AttachmentType.PNG
        )

    @staticmethod
    def screenshot_on_failure(method):
        def wrapper(self, *args, **kwargs):
            try:
                return method(self, *args, **kwargs)
            except Exception as e:
                self.make_screenshot(screenshot_name=f"{method.__name__}_failure_screenshot")
                raise e

        return wrapper
