import allure
from base.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}/"
        self.PAGE_TITLE = "Swag Labs"
        self.USERNAME_INPUT = ("id", "user-name")
        self.PASSWORD_INPUT = ("id", "password")
        self.LOGIN_BUTTON = ("id", "login-button")
        self.VALIDATION_ERROR_CONTAINER = ("xpath", "//div[contains(@class, 'error-message')]")
        self.VALIDATION_ERROR_TEXT = ("xpath", "//div[contains(@class, 'error-message')]/h3")

    def enter_username(self, username):
        with allure.step(f"Enter login: {username}"):
            self.wait_until_clickable(self.USERNAME_INPUT).send_keys(username)

    def enter_password(self, password):
        with allure.step(f"Enter login: {password}"):
            self.wait_until_clickable(self.PASSWORD_INPUT).send_keys(password)

    @allure.step("Click 'Login' button")
    def click_submit_button(self):
        self.wait_until_clickable(self.LOGIN_BUTTON).click()

    def check_validation_error(self, validation_error):
        with allure.step(f"Check validation error message: {validation_error}"):
            self.wait_until_visible(self.VALIDATION_ERROR_CONTAINER)
            self.wait_until_text_to_be_present(self.VALIDATION_ERROR_TEXT, validation_error)
