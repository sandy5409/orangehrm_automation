from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class PIMPage(BasePage):
    PIM_MENU = (By.XPATH, "//span[text()='PIM']")
    ADD_EMPLOYEE_BUTTON = (By.XPATH, "//a[text()='Add Employee']")

    def navigate_to_pim(self):
        self.click_element(self.PIM_MENU)

    def click_add_employee(self):
        self.click_element(self.ADD_EMPLOYEE_BUTTON)