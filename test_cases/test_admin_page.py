from unittest import TestCase

from selenium import webdriver

from base_pages.login_admin_page import login_admin_page


class test_admin_page:
    admin_page_url = "https://admin-demo.nopcommerce.com/login"
    username = "admin@yourstore.com"
    password = "admin"
    invalid_email = "wrong@your.com"

    def page_title(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        act_title = self.driver.title
        expected_title = "NoPCommerce"
        if act_title == expected_title:
            assert True
            self.driver.close()
        else:
            self.driver.close()

    def validate_log(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.admin_page_url)
        self.login_obj = login_admin_page()
        self.login_obj.enterUserName()
        self.login_obj.enterPassword()
        self.login_obj.login()
        dashboard_title = self.driver.find_element("//div[@class='content-header']/h1").text
        if dashboard_title == "expected_title":
            assert True
            self.driver.close()
        else:
            self.driver.close()
