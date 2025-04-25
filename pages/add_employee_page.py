from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddEmployeePage(BasePage):
    FIRST_NAME = (By.NAME, "firstName")
    LAST_NAME = (By.NAME, "lastName")
    SAVE_BUTTON = (By.XPATH, "//button[@type='submit']")

    def add_employee(self, first_name, last_name):
        self.wait_for_element(self.FIRST_NAME).send_keys(first_name)
        self.wait_for_element(self.LAST_NAME).send_keys(last_name)
        self.click_element(self.SAVE_BUTTON)