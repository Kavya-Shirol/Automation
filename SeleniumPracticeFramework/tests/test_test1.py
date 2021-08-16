import pytest

import time

from PageObjects.Homepage import HomePage
from Utilities.base_class import BaseClass



class TestOne(BaseClass):

    def test_first(self):

        homepage = HomePage(self.driver)
        homepage.get_name().send_keys("Kavya")
        homepage.get_email().send_keys("kavyashirol9@gmail.com")
        homepage.get_id().send_keys("kavya123")
        homepage.get_checkbox().click()
        self.select_text("Female")
        homepage.get_radio_button().click()
        homepage.get_date().send_keys("09/04/1997")
        homepage.get_submit_button().click()
        Success_msg = homepage.get_success_msg().text
        print(Success_msg)
        assert 'Success' in Success_msg, "Form not submitted"

    def test_second(self):

        self.driver.find_element_by_link_text("Shop").click()
        products = self.driver.find_elements_by_xpath("//div[@class='card h-100']")
        for product in products:
            product_name = product.find_element_by_xpath("div/h4/a").text
            if product_name == 'Samsung Note 8':
                product.find_element_by_xpath("div/button").click()

        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_css_selector("button[class*='btn-success']").click()
        self.driver.find_element_by_css_selector("#country").send_keys("ind")
        time.sleep(5)
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_css_selector("input[class*='btn-success']").click()
        print(self.driver.find_element_by_css_selector("div[class*='alert-succes']").text)
