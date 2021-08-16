import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.mark.usefixtures("setUp")
class BaseClass:

    def wait(self, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, text)))

    def select_dropdown(self, value):
        dropdown = Select(self.driver.find_element_by_tag_name("Select"))
        dropdown.select_by_visible_text(value)

