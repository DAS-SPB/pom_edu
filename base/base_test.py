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
