import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Checkout Page One functionality")
@pytest.mark.checkoutpageonepage
@pytest.mark.regression
class TestCheckoutPageOne(BaseTest):
    def open_checkout_page_with_items_in_cart(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_username(username="standard_user")
        self.login_page.enter_password(password="secret_sauce")
        self.login_page.click_submit_button()

        self.products_page.is_opened()
        items = self.products_page.get_all_items()
        items[0].click_add_to_cart()
        items[1].click_add_to_cart()

        self.cart_page.open()
        self.cart_page.is_opened()
        self.cart_page.click_checkout_button()

        self.checkout_step_one.is_opened()

    @allure.severity("Critical")
    @allure.title("Fill in inputs and click 'Continue' button")
    def test_fill_in_inputs_and_continue(self):
        self.open_checkout_page_with_items_in_cart()

        self.checkout_step_one.enter_first_name(first_name="First Name")
        self.checkout_step_one.enter_last_name(last_name="Last Name")
        self.checkout_step_one.enter_postal_code(postal_code="Postal Code")

        self.checkout_step_one.click_continue_button()

        self.checkout_step_two.is_opened()

    @allure.severity("Normal")
    @allure.title("Click 'Cancel' button")
    def test_fill_in_inputs_and_continue(self):
        self.open_checkout_page_with_items_in_cart()

        self.checkout_step_one.click_cancel_button()

        self.cart_page.is_opened()

    @allure.severity("Normal")
    @allure.title("Continue with missing inputs")
    @pytest.mark.negative
    @pytest.mark.parametrize("first_name, last_name, postal_code, validation_error", [
        ("", "Last Name", "Postal Code", "Error: First Name is required"),
        ("First Name", "", "Postal Code", "Error: Last Name is required"),
        ("First Name", "Last Name", "", "Error: Postal Code is required"),
    ])
    def test_login_missing_credentials(self, first_name, last_name, postal_code, validation_error):
        self.open_checkout_page_with_items_in_cart()

        self.checkout_step_one.enter_first_name(first_name=first_name)
        self.checkout_step_one.enter_last_name(last_name=last_name)
        self.checkout_step_one.enter_postal_code(postal_code=postal_code)
        self.checkout_step_one.click_continue_button()
        self.checkout_step_one.check_validation_error(validation_error=validation_error)
