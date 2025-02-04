import pytest
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutStepOnePage
from pages.checkout_step_two_page import CheckoutStepTwoPage
from pages.checkout_complete_page import CheckoutCompletePage


class BaseTest:
    login_page: LoginPage
    products_page: ProductsPage
    cart_page: CartPage
    checkout_step_one: CheckoutStepOnePage
    checkout_step_two: CheckoutStepTwoPage
    checkout_complete: CheckoutCompletePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver, host):
        request.cls.driver = driver
        request.cls.host = host

        request.cls.login_page = LoginPage(driver, host)
        request.cls.products_page = ProductsPage(driver, host)
        request.cls.cart_page = CartPage(driver, host)
        request.cls.checkout_step_one = CheckoutStepOnePage(driver, host)
        request.cls.checkout_step_two = CheckoutStepTwoPage(driver, host)
        request.cls.checkout_complete = CheckoutCompletePage(driver, host)

    def login(self, username: str = None, password: str = None):
        self.login_page.open()
        self.login_page.is_opened()

        if username:
            self.login_page.enter_username(username=username)
        if password:
            self.login_page.enter_password(password=password)
        self.login_page.click_submit_button()

    def logged_in(self):
        self.login(username="standard_user", password="secret_sauce")
        self.products_page.is_opened()

    def open_cart_page_with_items(self):
        self.logged_in()
        items = self.products_page.get_all_items()
        items[0].click_add_to_cart()
        items[1].click_add_to_cart()

        self.cart_page.open()
        self.cart_page.is_opened()

    def open_checkout_page_one_with_items_in_cart(self):
        self.open_cart_page_with_items()
        self.cart_page.click_checkout_button()

        self.checkout_step_one.is_opened()

    def open_checkout_page_two_with_items_in_cart(self):
        self.open_checkout_page_one_with_items_in_cart()
        self.checkout_step_one.enter_first_name(first_name="First Name")
        self.checkout_step_one.enter_last_name(last_name="Last Name")
        self.checkout_step_one.enter_postal_code(postal_code="Postal Code")
        self.checkout_step_one.click_continue_button()

        self.checkout_step_two.is_opened()

    def open_checkout_complete_page_after_payment(self):
        self.open_checkout_page_two_with_items_in_cart()
        self.checkout_step_two.click_finish_button()

        self.checkout_complete.is_opened()
