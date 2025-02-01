import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Checkout Page Two functionality")
@pytest.mark.checkoutpagetwopage
@pytest.mark.regression
class TestCheckoutPageTwo(BaseTest):
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
        self.checkout_step_one.enter_first_name(first_name="First Name")
        self.checkout_step_one.enter_last_name(last_name="Last Name")
        self.checkout_step_one.enter_postal_code(postal_code="Postal Code")
        self.checkout_step_one.click_continue_button()

        self.checkout_step_two.is_opened()

    @allure.severity("Normal")
    @allure.title("Check first item on the page")
    def test_check_first_item_on_page(self):
        self.open_checkout_page_with_items_in_cart()

        items = self.checkout_step_two.get_all_items()
        for item in items:
            item.check_item_quantity(expected_item_quantity="1")
            item.check_item_title(expected_item_title="Sauce Labs Backpack")
            item.check_item_description(
                expected_item_description="carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")
            item.check_item_price(expected_item_price="$29.99")
            break

    @allure.severity("Normal")
    @allure.title("Check order information on the page")
    def test_check_order_info_on_page(self):
        self.open_checkout_page_with_items_in_cart()

        self.checkout_step_two.check_payment_information(expected_payment_information="SauceCard #31337")
        self.checkout_step_two.check_shipping_information(expected_shipping_information="Free Pony Express Delivery!")
        self.checkout_step_two.check_price_subtotal(expected_price_subtotal="Item total: $39.98")
        self.checkout_step_two.check_price_tax(expected_price_tax="Tax: $3.20")
        self.checkout_step_two.check_price_total(expected_price_total="Total: $43.18")

    @allure.severity("Critical")
    @allure.title("Click 'Finish' button")
    def test_click_finish_button(self):
        self.open_checkout_page_with_items_in_cart()

        self.checkout_step_two.click_finish_button()

        self.checkout_complete.is_opened()

    @allure.severity("Normal")
    @allure.title("Click 'Cancel' button")
    def test_click_cancel_button(self):
        self.open_checkout_page_with_items_in_cart()

        self.checkout_step_two.click_cancel_button()

        self.products_page.is_opened()
