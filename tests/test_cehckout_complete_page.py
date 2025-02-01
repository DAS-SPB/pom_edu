import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Checkout Complete Page functionality")
@pytest.mark.checkoutcompletepage
@pytest.mark.regression
class TestCheckoutCompletePage(BaseTest):
    def open_checkout_complete_page_after_payment(self):
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
        self.checkout_step_one.enter_first_name(first_name="First Name")
        self.checkout_step_one.enter_last_name(last_name="Last Name")
        self.checkout_step_one.enter_postal_code(postal_code="Postal Code")
        self.checkout_step_one.click_continue_button()

        self.checkout_step_two.is_opened()
        self.checkout_step_two.click_finish_button()

        self.checkout_complete.is_opened()

    @allure.severity("Normal")
    @allure.title("Check information on the page")
    def test_check_information_on_page(self):
        self.open_checkout_complete_page_after_payment()

        self.checkout_complete.check_checkout_notification(expected_checkout_notification="Thank you for your order!")
        self.checkout_complete.check_checkout_description(
            expected_checkout_description="Your order has been dispatched, and will arrive just as fast as the pony can get there!")

    @allure.severity("Normal")
    @allure.title("Click 'Back Home' button")
    def test_click_back_home_button(self):
        self.open_checkout_complete_page_after_payment()

        self.checkout_complete.click_back_home_button()

        self.products_page.is_opened()
