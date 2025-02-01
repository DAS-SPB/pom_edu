import pytest
import allure
from base.base_test import BaseTest
from test_product_page import TestProductPage


@allure.feature("Cart page functionality")
@pytest.mark.cartpage
@pytest.mark.regression
class TestCartPage(BaseTest):
    def logged_in(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_username(username="standard_user")
        self.login_page.enter_password(password="secret_sauce")
        self.login_page.click_submit_button()
        self.products_page.is_opened()

    def add_items_to_cart(self):
        products = self.products_page
