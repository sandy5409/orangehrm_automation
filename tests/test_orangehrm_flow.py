import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Page classes
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.NAME, "username")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.profile_dropdown = (By.CLASS_NAME, "oxd-userdropdown-tab")
        self.logout_button = (By.XPATH, "//a[text()='Logout']")

    def logout(self):
        self.driver.find_element(*self.profile_dropdown).click()
        time.sleep(1)
        self.driver.find_element(*self.logout_button).click()


# Main Test Class
class TestOrangeHRMFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        time.sleep(2)

    def test_login_and_verify_name(self):
        login_page = LoginPage(self.driver)
        dashboard_page = DashboardPage(self.driver)

        username = "Admin"
        password = "admin123"
        full_name = "Phillip Dale"

        login_page.login(username, password)
        time.sleep(3)

        if full_name in self.driver.page_source:
            print(f"{full_name} - Name Verified")
        else:
            print(f"{full_name} - Name Not Found")

        dashboard_page.logout()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
