import allure
from base.base_page import BasePage


class ProductsPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}/inventory.html"
        self.PAGE_TITLE = "Swag Labs"
        self.ITEMS_LIST = ("xpath", "//div[@class='inventory_item']")
        self.CART_BADGE = ("xpath", "//span[@class='shopping_cart_badge']")

    @allure.step("Get all items on product page")
    def get_all_items(self):
        items = self.wait_until_all_elements_visible(self.ITEMS_LIST)
        return [SeparateItem(item, self.wait) for item in items]

    def get_num_of_items_in_cart(self, expected_num_of_items_in_cart):
        with allure.step(f"Check num of items in cart to be: {expected_num_of_items_in_cart}"):
            if int(expected_num_of_items_in_cart) > 0:
                self.wait_until_text_to_be_present(self.CART_BADGE, expected_num_of_items_in_cart)
            else:
                self.wait_until_invisible(self.CART_BADGE)


class SeparateItem:
    def __init__(self, item, wait):
        self.item = item
        self.wait = wait
        self.ITEM_IMAGE = ("xpath", ".//img[@class='inventory_item_img']")
        self.ITEM_TITLE = ("xpath", ".//div[contains(@class, 'inventory_item_name')]")
        self.ITEM_DESCRIPTION = (
            "xpath", ".//div[@class='inventory_item_label']//div[contains(@class, 'inventory_item_desc')]")
        self.ITEM_PRICE = ("xpath", ".//div[@class='inventory_item_price']")
        self.ADD_TO_CART_BUTTON = ("xpath", ".//button[contains(@id, 'add-to-cart')]")
        self.REMOVE_FROM_CART_BUTTON = ("xpath", ".//button[contains(@id, 'remove')]")

    def check_item_image(self, expected_item_image_name):
        with allure.step(f"Check item's image name to be: {expected_item_image_name}"):
            actual_image_name = self.item.find_element(*self.ITEM_IMAGE).get_attribute('alt')
            assert actual_image_name == expected_item_image_name, (
                f"Expected image name to be: '{expected_item_image_name}', actual: '{actual_image_name}'"
            )

    def check_item_title(self, expected_item_title):
        with allure.step(f"Check item's title to be: {expected_item_title}"):
            actual_title = self.item.find_element(*self.ITEM_TITLE).text
            assert actual_title == expected_item_title, (
                f"Expected title to be '{expected_item_title}', got '{actual_title}'"
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

    @allure.step("Click 'Add to cart' button")
    def click_add_to_cart(self):
        self.item.find_element(*self.ADD_TO_CART_BUTTON).click()

    @allure.step("Click 'Remove' button")
    def click_remove_from_cart(self):
        self.item.find_element(*self.REMOVE_FROM_CART_BUTTON).click()
