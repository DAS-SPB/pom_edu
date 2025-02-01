import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Product page functionality")
@pytest.mark.productpage
@pytest.mark.regression
class TestProductPage(BaseTest):
    def logged_in(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_username(username="standard_user")
        self.login_page.enter_password(password="secret_sauce")
        self.login_page.click_submit_button()
        self.products_page.is_opened()

    @allure.severity("Critical")
    @allure.title("Check info for the first product on product page")
    @pytest.mark.smoke
    def test_check_info_for_the_first_product(self):
        self.logged_in()
        products = self.products_page.get_all_items()
        for product in products:
            product.check_item_image(expected_item_image_name="Sauce Labs Backpack")
            product.check_item_title(expected_item_title="Sauce Labs Backpack")
            product.check_item_description(
                expected_item_description="carry.allTheThings() with the sleek, streamlined Sly Pack that melds uncompromising style with unequaled laptop and tablet protection.")
            product.check_item_price(expected_item_price="$29.99")
            break

    @allure.severity("Normal")
    @allure.title("Check info for another product on product page")
    @pytest.mark.smoke
    def test_check_info_for_another_product(self):
        self.logged_in()
        products = self.products_page.get_all_items()
        product = products[2]
        product.check_item_image(expected_item_image_name="Sauce Labs Bolt T-Shirt")
        product.check_item_title(expected_item_title="Sauce Labs Bolt T-Shirt")
        product.check_item_description(
            expected_item_description="Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.")
        product.check_item_price(expected_item_price="$15.99")

    @allure.severity("Critical")
    @allure.title("Add product on product page to the cart")
    @pytest.mark.smoke
    def test_add_product_to_cart(self):
        self.logged_in()
        products = self.products_page.get_all_items()
        for product in products:
            product.click_add_to_cart()
            break
        self.products_page.get_num_of_items_in_cart(expected_num_of_items_in_cart="1")

    @allure.severity("Normal")
    @allure.title("Remove product on product page from the cart")
    @pytest.mark.smoke
    def test_remove_product_from_cart(self):
        self.logged_in()
        products = self.products_page.get_all_items()
        for product in products:
            product.click_add_to_cart()
            product.click_remove_from_cart()
            break
        self.products_page.get_num_of_items_in_cart(expected_num_of_items_in_cart="0")
