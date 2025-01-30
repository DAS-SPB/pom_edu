import allure
from base.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class CheckoutStepTwo(BasePage):
    def __init__(self, driver, host):
        super().__init__(driver)
        self.PAGE_URL = f"{host}/checkout-step-two.html"
        self.PAGE_TITLE = "Swag Labs"
        self.ITEMS_LIST = ("xpath", "//div[@class='cart_item']")
        self.ITEM_QUANTITY = ("xpath", "//div[@class='cart_quantity']")
        self.ITEM_TITLE = ("xpath", "//div[contains(@class, 'inventory_item_name')]")
        self.ITEM_DESCRIPTION = ("xpath", "//div[contains(@class, 'inventory_item_desc')]")
        self.ITEM_PRICE = ("class", "inventory_item_price")
        self.PAYMENT_INFORMATION = ("xpath", "//div[@class='summary_info']/div[@data-test='payment-info-value']")
        self.SHIPPING_INFORMATION = ("xpath", "//div[@class='summary_info']/div[@data-test='shipping-info-value']")
        self.PRICE_SUBTOTAL = ("xpath", "//div[@class='summary_info']/div[@data-test='subtotal-label']")
        self.PRICE_TAX = ("xpath", "//div[@class='summary_info']/div[@data-test='tax-label']")
        self.PRICE_TOTAL = ("xpath", "//div[@class='summary_info']/div[@data-test='total-label']")
        self.FINISH_BUTTON = ("id", "finish")
        self.CANCEL_BUTTON = ("id", "cancel")

    @allure.step("Get all items in cart on checkout page two")
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

    def check_payment_information(self, expected_payment_information):
        with allure.step(f"Check 'Payment information' to be: {expected_payment_information}"):
            self.wait.until(EC.visibility_of_element_located(self.PAYMENT_INFORMATION))
            self.wait.until(EC.text_to_be_present_in_element(self.PAYMENT_INFORMATION, expected_payment_information))

    def check_shipping_information(self, expected_shipping_information):
        with allure.step(f"Check 'Shipping information' to be: {expected_shipping_information}"):
            self.wait.until(EC.visibility_of_element_located(self.SHIPPING_INFORMATION))
            self.wait.until(EC.text_to_be_present_in_element(self.SHIPPING_INFORMATION, expected_shipping_information))

    def check_price_subtotal(self, expected_price_subtotal):
        with allure.step(f"Check subtotal price to be: {expected_price_subtotal}"):
            self.wait.until(EC.visibility_of_element_located(self.PRICE_SUBTOTAL))
            self.wait.until(EC.text_to_be_present_in_element(self.PRICE_SUBTOTAL, expected_price_subtotal))

    def check_price_tax(self, expected_price_tax):
        with allure.step(f"Check tax price to be: {expected_price_tax}"):
            self.wait.until(EC.visibility_of_element_located(self.PRICE_TAX))
            self.wait.until(EC.text_to_be_present_in_element(self.PRICE_TAX, expected_price_tax))

    def check_price_total(self, expected_price_total):
        with allure.step(f"Check total price to be: {expected_price_total}"):
            self.wait.until(EC.visibility_of_element_located(self.PRICE_TOTAL))
            self.wait.until(EC.text_to_be_present_in_element(self.PRICE_TOTAL, expected_price_total))

    @allure.step("Click 'Finish' button")
    def click_finish_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FINISH_BUTTON)).click()

    @allure.step("Click 'Cancel' button")
    def click_cancel_button(self):
        self.wait.until(EC.element_to_be_clickable(self.CANCEL_BUTTON)).click()
