import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}"
        self.PAGE_TITLE = "Swag Labs"
        self.USERNAME_INPUT = ("id", "user-name")
        self.PASSWORD_INPUT = ("id", "password")
        self.LOGIN_BUTTON = ("id", "login-button")
        self.VALIDATION_ERROR_CONTAINER = ("xpath", "//div[contains(@class, 'error-message')]")
        self.VALIDATION_ERROR_TEXT = ("xpath", "//div[contains(@class, 'error-message')]/h3")

    def enter_login(self, login):
        with allure.step(f"Enter login: {login}"):
            self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT)).send_keys(login)

    def enter_password(self, password):
        with allure.step(f"Enter login: {password}"):
            self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT)).send_keys(password)

    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def check_validation_error(self, validation_error):
        with allure.step(f"Check validation error message: {validation_error}"):
            self.wait.until(EC.visibility_of_element_located(self.VALIDATION_ERROR_CONTAINER))
            self.wait.until(EC.text_to_be_present_in_element(self.VALIDATION_ERROR_TEXT, validation_error))
