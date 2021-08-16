from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    checkbox  = (By.CSS_SELECTOR, "input[type='checkbox']")
    def click_checkbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)