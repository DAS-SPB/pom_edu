import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Checkout Complete Page functionality")
@pytest.mark.checkoutcompletepage
@pytest.mark.regression
@pytest.mark.xdist_group("checkoutcompletepage")
class TestCheckoutCompletePage(BaseTest):

    @allure.severity("Critical")
    @allure.title("Check information on the page")
    def test_check_information_on_page(self):
        self.open_checkout_complete_page_after_payment()

        self.checkout_complete.check_checkout_notification(expected_checkout_notification="Thank you for your order!")
        self.checkout_complete.check_checkout_description(
            expected_checkout_description="Your order has been dispatched, and will arrive just as fast as the pony can get there!")

    @allure.severity("Normal")
    @allure.title("Click 'Back Home' button")
    def test_click_back_home_button(self):
        self.open_checkout_complete_page_after_payment()

        self.checkout_complete.click_back_home_button()

        self.products_page.is_opened()
