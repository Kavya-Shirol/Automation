from selenium.webdriver.common.by import By


class ConfirmPage:

    tag = (By.TAG_NAME, "select")
    checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    proceed = (By.XPATH, "//button[text()='Proceed']")
    def __init__(self, driver):
        self.driver = driver

    def get_tag(self):
        return self.driver.find_element(*ConfirmPage.tag)

    def getcheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getproceedbutton(self):
        return self.driver.find_element(*ConfirmPage.proceed)


