import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CartPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}"
        self.PAGE_TITLE = "Swag Labs"
        self.ITEMS_LIST = ("xpath", "//div[@class='cart_item']")
        self.ITEM_QUANTITY = ("xpath", "//div[@class='cart_quantity']")
        self.ITEM_TITLE = ("xpath", "//div[contains(@class, 'inventory_item_name')]")
        self.ITEM_DESCRIPTION = ("xpath", "//div[contains(@class, 'inventory_item_desc')]")
        self.ITEM_PRICE = ("class", "inventory_item_price")
        self.REMOVE_FROM_CART_BUTTON = ("xpath", "//button[contains(@id, 'remove')]")
        self.BACK_TO_SHOPPING_BUTTON = ("id", "continue-shopping")
        self.CHECKOUT_BUTTON = ("id", "checkout")

    @allure.step("Get all items in cart")
    def get_all_items(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.ITEMS_LIST))

    def check_item_quantity(self, expected_item_quantity):
        with allure.step(f"Check item's quantity to be: {expected_item_quantity}"):
            self.wait.until(EC.text_to_be_present_in_element(self.ITEM_QUANTITY, expected_item_quantity))

    def check_item_title(self, expected_item_title):
        with allure.step(f"Check item's title to be: {expected_item_title}"):
            self.wait.until(EC.text_to_be_present_in_element(self.ITEM_TITLE, expected_item_title))

    def check_item_description(self, expected_item_description):
        with allure.step(f"Check item's description to be: {expected_item_description}"):
            self.wait.until(EC.text_to_be_present_in_element(self.ITEM_DESCRIPTION, expected_item_description))

    def check_item_price(self, expected_item_price):
        with allure.step(f"Check item's price to be: {expected_item_price}"):
            self.wait.until(EC.text_to_be_present_in_element(self.ITEM_PRICE, expected_item_price))

    @allure.step("Click 'Remove' button")
    def click_remove_from_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_FROM_CART_BUTTON)).click()

    @allure.step("Click 'Continue Shopping' button")
    def click_remove_from_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.BACK_TO_SHOPPING_BUTTON)).click()

    @allure.step("Click 'Checkout' button")
    def click_remove_from_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON)).click()
