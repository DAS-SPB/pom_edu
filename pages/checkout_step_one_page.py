import allure
from base.base_page import BasePage


class CheckoutStepOnePage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}/checkout-step-one.html"
        self.PAGE_TITLE = "Swag Labs"
        self.FIRST_NAME_INPUT = ("id", "first-name")
        self.LAST_NAME_INPUT = ("id", "last-name")
        self.POSTAL_CODE_INPUT = ("id", "postal-code")
        self.CONTINUE_BUTTON = ("id", "continue")
        self.CANCEL_BUTTON = ("id", "cancel")
        self.VALIDATION_ERROR_CONTAINER = ("xpath", "//div[contains(@class, 'error-message')]")
        self.VALIDATION_ERROR_TEXT = ("xpath", "//div[contains(@class, 'error-message')]/h3")

    def enter_first_name(self, first_name):
        with allure.step(f"Enter First Name: {first_name}"):
            self.wait_until_visible(self.FIRST_NAME_INPUT).send_keys(first_name)

    def enter_last_name(self, last_name):
        with allure.step(f"Enter Last Name: {last_name}"):
            self.wait_until_visible(self.LAST_NAME_INPUT).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        with allure.step(f"Enter login: {postal_code}"):
            self.wait_until_visible(self.POSTAL_CODE_INPUT).send_keys(postal_code)

    @allure.step("Click 'Continue' button")
    def click_continue_button(self):
        self.wait_until_clickable(self.CONTINUE_BUTTON).click()

    @allure.step("Click 'Cancel' button")
    def click_cancel_button(self):
        self.wait_until_clickable(self.CANCEL_BUTTON).click()

    def check_validation_error(self, validation_error):
        with allure.step(f"Check validation error message: {validation_error}"):
            self.wait_until_visible(self.VALIDATION_ERROR_CONTAINER)
            self.wait_until_text_to_be_present(self.VALIDATION_ERROR_TEXT, validation_error)
