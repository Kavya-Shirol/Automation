import pytest
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def select_text(self, text):
        select = Select(self.driver.find_element_by_id("exampleFormControlSelect1"))
        select.select_by_visible_text(text)

