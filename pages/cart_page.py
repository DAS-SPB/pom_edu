import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}/cart.html"
        self.PAGE_TITLE = "Swag Labs"
        self.ITEMS_LIST = ("xpath", "//div[@class='cart_item']")
        self.BACK_TO_SHOPPING_BUTTON = ("id", "continue-shopping")
        self.CHECKOUT_BUTTON = ("id", "checkout")
        self.CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")

    @allure.step("Get all items in cart")
    def get_all_items(self):
        items = self.wait.until(EC.visibility_of_all_elements_located(self.ITEMS_LIST))
        return [SeparateItem(item, self.wait) for item in items]

    @allure.step("Click 'Continue Shopping' button")
    def click_continue_shopping_button(self):
        self.wait.until(EC.element_to_be_clickable(self.BACK_TO_SHOPPING_BUTTON)).click()

    @allure.step("Click 'Checkout' button")
    def click_checkout_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()

    def get_num_of_items_in_cart(self, expected_num_of_items_in_cart):
        with allure.step(f"Check num of items in cart to be: {expected_num_of_items_in_cart}"):
            if int(expected_num_of_items_in_cart) > 0:
                self.wait.until(EC.text_to_be_present_in_element(self.CART_BADGE, expected_num_of_items_in_cart))
            else:
                self.wait.until(EC.invisibility_of_element_located(self.CART_BADGE))


class SeparateItem:
    def __init__(self, item, wait):
        self.item = item
        self.wait = wait
        self.ITEM_QUANTITY = ("xpath", ".//div[@class='cart_quantity']")
        self.ITEM_TITLE = ("xpath", ".//div[contains(@class, 'inventory_item_name')]")
        self.ITEM_DESCRIPTION = ("xpath", ".//div[contains(@class, 'inventory_item_desc')]")
        self.ITEM_PRICE = ("class", "inventory_item_price")
        self.REMOVE_FROM_CART_BUTTON = ("xpath", ".//button[contains(@id, 'remove')]")

    def check_item_quantity(self, expected_item_quantity):
        with allure.step(f"Check item's quantity to be: {expected_item_quantity}"):
            actual_quantity = self.item.find_element(*self.ITEM_QUANTITY).text
            assert actual_quantity == expected_item_quantity, (
                f"Expected item's quantity to be: '{expected_item_quantity}', actual: '{actual_quantity}'"
            )

    def check_item_title(self, expected_item_title):
        with allure.step(f"Check item's title to be: {expected_item_title}"):
            actual_title = self.item.find_element(*self.ITEM_QUANTITY).text
            assert actual_title == expected_item_title, (
                f"Expected item's title to be: '{expected_item_title}', actual: '{actual_title}'"
            )

    def check_item_description(self, expected_item_description):
        with allure.step(f"Check item's description to be: {expected_item_description}"):
            actual_description = self.item.find_element(*self.ITEM_DESCRIPTION).text
            assert actual_description == expected_item_description, (
                f"Expected description to be '{expected_item_description}', got '{actual_description}'"
            )

    def check_item_price(self, expected_item_price):
        with allure.step(f"Check item's price to be: {expected_item_price}"):
            actual_price = self.item.find_element(*self.ITEM_PRICE).text
            assert actual_price == expected_item_price, (
                f"Expected description to be '{expected_item_price}', got '{actual_price}'"
            )

    @allure.step("Click 'Remove' button")
    def click_remove_from_cart(self):
        self.item.find_element(*self.REMOVE_FROM_CART_BUTTON).click()
