from selenium.webdriver.common.by import By


class SuccessPage:

    def __init__(self, driver):
        self.driver = driver

    proceedbutton = (By.XPATH, "//button[text()='Proceed']")
    def click_proceed(self):
        return self.driver.find_element(*SuccessPage.proceedbutton)