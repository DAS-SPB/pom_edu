import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ProductsPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}/inventory.html"
        self.PAGE_TITLE = "Swag Labs"
        self.ITEMS_LIST = ("class", "inventory_item")
        self.ITEM_IMAGE = ("xpath", "//img[@class='inventory_item_img']")
        self.ITEM_TITLE = ("xpath", "//div[contains(@class, 'inventory_item_name')]")
        self.ITEM_DESCRIPTION = (
            "xpath", "//div[@class='inventory_item_label']//div[contains(@class, 'inventory_item_desc')]")
        self.ITEM_PRICE = ("class", "inventory_item_price")
        self.ADD_TO_CART_BUTTON = ("xpath", "//button[contains(@id, 'add-to-cart')]")
        self.REMOVE_FROM_CART_BUTTON = ("xpath", "//button[contains(@id, 'remove')]")

    @allure.step("Get all items on page")
    def get_all_items(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.ITEMS_LIST))

    def check_item_image(self, expected_item_image_name):
        with allure.step(f"Check item's image name to be: {expected_item_image_name}"):
            self.wait.until(EC.visibility_of_element_located(self.ITEM_IMAGE))
            # self.wait.until(EC.element_attribute_to_include(self.ITEM_IMAGE, 'alt'), expected_item_image_name)
            actual_image_name = self.driver.find_element(*self.ITEM_IMAGE).get_attribute('alt')
            assert actual_image_name == expected_item_image_name, (
                f"Expected: '{expected_item_image_name}', actual: '{actual_image_name}'"
            )

    def check_item_title(self, expected_item_title):
        with allure.step(f"Check item's title to be: {expected_item_title}"):
            self.wait.until(EC.text_to_be_present_in_element(self.ITEM_TITLE, expected_item_title))

    def check_item_description(self, expected_item_description):
        with allure.step(f"Check item's description to be: {expected_item_description}"):
            self.wait.until(EC.text_to_be_present_in_element(self.ITEM_DESCRIPTION, expected_item_description))

    def check_item_price(self, expected_item_price):
        with allure.step(f"Check item's price to be: {expected_item_price}"):
            self.wait.until(EC.text_to_be_present_in_element(self.ITEM_PRICE, expected_item_price))

    @allure.step("Click 'Add to cart' button")
    def click_add_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()

    @allure.step("Click 'Remove' button")
    def click_remove_from_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.REMOVE_FROM_CART_BUTTON)).click()
