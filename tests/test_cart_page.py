import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Cart Page functionality")
@pytest.mark.cartpage
@pytest.mark.regression
@pytest.mark.xdist_group("cartpage")
class TestCartPage(BaseTest):

    @allure.severity("Critical")
    @allure.title("Check num of items in the cart")
    def test_check_num_of_items_in_cart(self):
        self.open_cart_page_with_items()

        items = self.cart_page.get_all_items()
        items_num = len(items)
        assert items_num == 2, f"Expected items num: 2, actual: {items_num}"
        self.cart_page.get_num_of_items_in_cart(expected_num_of_items_in_cart="2")

    @allure.severity("Critical")
    @allure.title("Click 'Checkout' button")
    def test_check_checkout_button_in_cart(self):
        self.open_cart_page_with_items()

        self.cart_page.click_checkout_button()
        self.checkout_step_one.is_opened()

    @allure.severity("Normal")
    @allure.title("Click 'Continue shopping' button")
    def test_check_checkout_button_in_cart(self):
        self.open_cart_page_with_items()

        self.cart_page.click_continue_shopping_button()
        self.products_page.is_opened()

    @allure.severity("Normal")
    @allure.title("Check first item in the cart")
    def test_check_first_item_in_cart(self):
        self.open_cart_page_with_items()

        items = self.cart_page.get_all_items()
        for item in items:
            item.check_item_quantity(expected_item_quantity="1")
            item.check_item_title(expected_item_title="Sauce Labs Backpack")
            item.check_item_description(
                expected_item_description="carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")
            item.check_item_price(expected_item_price="$29.99")
            break

    @allure.severity("Normal")
    @allure.title("Remove second item from the cart")
    def test_remove_second_item_from_cart(self):
        self.open_cart_page_with_items()

        items = self.cart_page.get_all_items()
        item = items[1]
        item.click_remove_from_cart()
        self.cart_page.get_num_of_items_in_cart(expected_num_of_items_in_cart="1")
