from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")

    def login(self, username, password):
        self.wait_for_element(self.USERNAME).send_keys(username)
        self.wait_for_element(self.PASSWORD).send_keys(password)
        self.click_element(self.LOGIN_BUTTON)