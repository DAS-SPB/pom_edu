import allure
from base.base_page import BasePage


class CheckoutStepTwoPage(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}/checkout-step-two.html"
        self.PAGE_TITLE = "Swag Labs"
        self.ITEMS_LIST = ("xpath", "//div[@class='cart_item']")
        self.PAYMENT_INFORMATION = ("xpath", "//div[@class='summary_info']/div[@data-test='payment-info-value']")
        self.SHIPPING_INFORMATION = ("xpath", "//div[@class='summary_info']/div[@data-test='shipping-info-value']")
        self.PRICE_SUBTOTAL = ("xpath", "//div[@class='summary_info']/div[@data-test='subtotal-label']")
        self.PRICE_TAX = ("xpath", "//div[@class='summary_info']/div[@data-test='tax-label']")
        self.PRICE_TOTAL = ("xpath", "//div[@class='summary_info']/div[@data-test='total-label']")
        self.FINISH_BUTTON = ("id", "finish")
        self.CANCEL_BUTTON = ("id", "cancel")

    @allure.step("Get all items in cart on checkout page two")
    def get_all_items(self):
        items = self.wait_until_all_elements_visible(self.ITEMS_LIST)
        return [SeparateItem(item, self.wait) for item in items]

    def check_payment_information(self, expected_payment_information):
        with allure.step(f"Check 'Payment information' to be: {expected_payment_information}"):
            actual_payment_info = self.wait_until_visible(self.PAYMENT_INFORMATION).text
            assert actual_payment_info == expected_payment_information, (
                f"Expected payment information to be: {expected_payment_information}, actual: {actual_payment_info}"
            )

    def check_shipping_information(self, expected_shipping_information):
        with allure.step(f"Check 'Shipping information' to be: {expected_shipping_information}"):
            actual_shipping_info = self.wait_until_visible(self.SHIPPING_INFORMATION).text
            assert actual_shipping_info == expected_shipping_information, (
                f"Expected shipping information to be: {expected_shipping_information}, actual: {actual_shipping_info}"
            )

    def check_price_subtotal(self, expected_price_subtotal):
        with allure.step(f"Check subtotal price to be: {expected_price_subtotal}"):
            actual_subtotal_price = self.wait_until_visible(self.PRICE_SUBTOTAL).text
            assert actual_subtotal_price == expected_price_subtotal, (
                f"Expected subtotal price to be: {expected_price_subtotal}, actual: {actual_subtotal_price}"
            )

    def check_price_tax(self, expected_price_tax):
        with allure.step(f"Check tax price to be: {expected_price_tax}"):
            actual_tax_price = self.wait_until_visible(self.PRICE_TAX).text
            assert actual_tax_price == expected_price_tax, (
                f"Expected tax price to be: {expected_price_tax}, actual: {actual_tax_price}"
            )

    def check_price_total(self, expected_price_total):
        with allure.step(f"Check total price to be: {expected_price_total}"):
            actual_total_price = self.wait_until_visible(self.PRICE_TOTAL).text
            assert actual_total_price == expected_price_total, (
                f"Expected total price to be: {expected_price_total}, actual: {actual_total_price}"
            )

    @allure.step("Click 'Finish' button")
    def click_finish_button(self):
        self.wait_until_clickable(self.FINISH_BUTTON).click()

    @allure.step("Click 'Cancel' button")
    def click_cancel_button(self):
        self.wait_until_clickable(self.CANCEL_BUTTON).click()


class SeparateItem:
    def __init__(self, item, wait):
        self.item = item
        self.wait = wait
        self.ITEM_QUANTITY = ("xpath", ".//div[@class='cart_quantity']")
        self.ITEM_TITLE = ("xpath", ".//div[contains(@class, 'inventory_item_name')]")
        self.ITEM_DESCRIPTION = ("xpath", ".//div[contains(@class, 'inventory_item_desc')]")
        self.ITEM_PRICE = ("xpath", ".//div[@class='inventory_item_price']")

    def check_item_quantity(self, expected_item_quantity):
        with allure.step(f"Check item's quantity to be: {expected_item_quantity}"):
            actual_quantity = self.item.find_element(*self.ITEM_QUANTITY).text
            assert actual_quantity == expected_item_quantity, (
                f"Expected item's quantity to be: {expected_item_quantity}, actual: {actual_quantity}"
            )

    def check_item_title(self, expected_item_title):
        with allure.step(f"Check item's title to be: {expected_item_title}"):
            actual_title = self.item.find_element(*self.ITEM_TITLE).text
            assert actual_title == expected_item_title, (
                f"Expected item's title to be: {expected_item_title}, actual: {actual_title}"
            )

    def check_item_description(self, expected_item_description):
        with allure.step(f"Check item's description to be: {expected_item_description}"):
            actual_description = self.item.find_element(*self.ITEM_DESCRIPTION).text
            assert actual_description == expected_item_description, (
                f"Expected item's description to be: {expected_item_description}, actual: {actual_description}"
            )

    def check_item_price(self, expected_item_price):
        with allure.step(f"Check item's price to be: {expected_item_price}"):
            actual_price = self.item.find_element(*self.ITEM_PRICE).text
            assert actual_price == expected_item_price, (
                f"Expected item's description to be: {expected_item_price}, actual: {actual_price}"
            )
