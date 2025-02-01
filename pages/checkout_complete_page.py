import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutCompletePage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}/checkout-complete.html"
        self.PAGE_TITLE = "Swag Labs"
        self.CHECKOUT_NOTIFICATION = ("xpath", "//div[contains(@id, 'checkout')]/h2[contains(@class, 'header')]")
        self.CHECKOUT_DESCRIPTION = ("xpath", "//div[contains(@id, 'checkout')]/div[contains(@class, 'text')]")
        self.BACK_HOME = ("id", "back-to-products")

    @allure.step("Click 'Back Home' button")
    def click_back_home_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BACK_HOME)).click()

    def check_checkout_notification(self, expected_checkout_notification):
        with allure.step(f"Check checkout notification to be: {expected_checkout_notification}"):
            actual_notification = self.wait.until(
                EC.visibility_of_element_located(self.CHECKOUT_NOTIFICATION)).text
            assert actual_notification == expected_checkout_notification, (
                f"Expected notification text to be: {expected_checkout_notification}, actual: {actual_notification}"
            )

    def check_checkout_description(self, expected_checkout_description):
        with allure.step(f"Check checkout notification to be: {expected_checkout_description}"):
            actual_description = self.wait.until(EC.visibility_of_element_located(self.CHECKOUT_DESCRIPTION)).text
            assert actual_description == expected_checkout_description, (
                f"Expected description text to be: {expected_checkout_description}, actual: {actual_description}"
            )
