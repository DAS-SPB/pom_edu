import pytest
import allure
from base.base_test import BaseTest


@allure.feature("Login Page functionality")
@pytest.mark.login
@pytest.mark.regression
class TestLogin(BaseTest):

    @allure.severity("Critical")
    @allure.title("Log in successfully")
    @pytest.mark.smoke
    def test_login_successful(self):
        self.login(username="standard_user", password="secret_sauce")
        self.products_page.is_opened()

    @allure.severity("Normal")
    @allure.title("Log in for different types of users")
    @pytest.mark.parametrize("username, password", [
        ("problem_user", "secret_sauce"),
        ("performance_glitch_user", "secret_sauce"),
    ])
    def test_login_successful_different_users(self, username, password):
        self.login(username=username, password=password)
        self.products_page.is_opened()

    @allure.severity("Normal")
    @allure.title("Log in with invalid credentials")
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, validation_error", [
        ("wrong", "wrong", "Epic sadface: Username and password do not match any user in this service"),
    ])
    def test_login_invalid_credentials(self, username, password, validation_error):
        self.login(username=username, password=password)
        self.login_page.is_opened()
        self.login_page.check_validation_error(validation_error=validation_error)

    @allure.severity("Normal")
    @allure.title("Log in with missing username or password")
    @pytest.mark.negative
    @pytest.mark.parametrize("username, password, validation_error", [
        ("", "wrong", "Epic sadface: Username is required"),
        ("wrong", "", "Epic sadface: Password is required"),
    ])
    def test_login_missing_credentials(self, username, password, validation_error):
        self.login(username=username, password=password)
        self.login_page.is_opened()
        self.login_page.check_validation_error(validation_error=validation_error)
