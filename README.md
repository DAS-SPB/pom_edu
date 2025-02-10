![Last commit](https://img.shields.io/github/last-commit/DAS-SPB/pom_edu?color=9cf&logo=git)
![GitHub top language](https://img.shields.io/github/languages/top/DAS-SPB/pom_edu?color=blue)

# Test Automation Project

This project demonstrates an automated testing framework for the [saucedemo.com](https://www.saucedemo.com/) demo website. 
It is designed to be scalable, maintainable and efficient for end-to-end web testing. 
The framework incorporates modern tools and best practices to ensure reliability and ease of execution.

Tests are implemented for the following pages:
- login page
- products page
- cart page
- checkout page one
- checkout page two
- checkout complete page

This project does not provide full test coverage. It is implemented as an example to demonstrate test automation concepts and best practices.

## Project Structure

Overview of the main directories and their contents:
- **[base](base)** – Contains the BasePage and BaseTest classes.
  - BasePage provides common methods for interacting with web pages.
  - BaseTest includes shared test setup, common test steps and annotations.
- **[pages](pages)** – Contains page classes with methods to interact with specific web pages.
- **[tests](tests)** – Implements test cases using page methods to verify functionality for each web page.

## Project Features

- **Page Object Model (POM)** – Ensures maintainability and re-usability of test code.
- **Automated Screenshot Capture** – Pytest hooks automatically generate screenshots on test failures.
- **Parallel Test Execution** – pytest-xdist enables running tests in parallel for improved efficiency.
- **Comprehensive Allure Reporting** –
  - Static and dynamic annotations for detailed step-by-step reports. Code examples:
```
@allure.step("Click 'Login' button")
def click_submit_button(self):
    self.wait_until_clickable(self.LOGIN_BUTTON).click()
        
def enter_username(self, username):
    with allure.step(f"Enter login: {username}"):
        self.wait_until_clickable(self.USERNAME_INPUT).send_keys(username)        
```
  - Reports are hosted separately for each browser on **GitHub Pages [gh-pages](https://das-spb.github.io/pom_edu/)** for easy access.
- **Cross-Browser Testing** – Tests run on Chrome, Firefox, and Edge using Selenium Grid.
- **Containerized Environment** – Docker manages test execution, Selenium Hub, and Allure service.
- **Continuous Integration (CI)** – Automated execution via GitHub Actions.


## Getting Started

To install the project dependencies, run the following command in the terminal:

```
$ poetry install
```
This will create a virtual environment and install all required dependencies.

## Run Automated Tests

To run tests locally **without generating an Allure report**, use the following command (Chrome, 8 parallel threads):
```
poetry run pytest tests -n 8 --browser=chrome
```
**Configurable Options**
- Browser Selection (--browser)
  - chrome
  - firefox
  - edge
- Execution Modes
  - Headless Mode – Run tests in the background (add --headless option).
  - Headed Mode – Run tests with a visible browser window (omit --headless).
- Parallel Execution
  - Adjust the number of parallel threads by modifying the -n parameter (-n <num_threads>).
- CI Execution
  - Regression tests can be triggered in the CI pipeline by clicking the "Run workflow" button in GitHub Actions.

## Possible Improvements

To minimize repetitive interactions with web pages, leveraging an API or managing authentication via cookies would be ideal. 
However, the demo website does not provide such capabilities, limiting the available optimization strategies.