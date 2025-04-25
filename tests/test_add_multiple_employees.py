import unittest
from selenium import webdriver

from pages.pim_page import PIMPage
from pages.add_employee_page import AddEmployeePage
from pages.login_page import LoginPage
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class TestAddEmployees(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_add_multiple_employees(self):
        login_page = LoginPage(self.driver)
        login_page.login("Admin", "admin123")

        pim_page = PIMPage(self.driver)
        pim_page.navigate_to_pim()

        employees = [
            {"first_name": "sarkar", "last_name": "chandra"},
            {"first_name": "bappatla", "last_name": "sukendar"},
            {"first_name": "sruthi", "last_name": "gouri"},
            {"first_name": "ramani", "last_name": "burugula"},
        ]

        for emp in employees:
            pim_page.click_add_employee()
            add_employee_page = AddEmployeePage(self.driver)
            add_employee_page.add_employee(emp["first_name"], emp["last_name"])

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()