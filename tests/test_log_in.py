import pytest
import allure
from base.base_test import BaseTest


class TestLogin(BaseTest):

    def test_successful_login(self):
        self.login_page.open()
        self.login_page.is_opened()
        self.login_page.enter_login(login='standard_user')
        self.login_page.enter_password(password='secret_sauce')
        self.login_page.click_submit_button()

        self.products_page.is_opened()
