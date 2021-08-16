from selenium.webdriver.common.by import By


class HomePage:

    name = (By.NAME, "name")
    email = (By.NAME, "email")
    pwd = (By.ID, "exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "input[type='checkbox']")
    radio_button = (By.ID, "inlineRadio2")
    date = (By.NAME, "bday")
    submit_button = (By.XPATH, "//input[@type='submit']")
    success_msg = (By.CSS_SELECTOR, "div[class*='alert-success ']")


    def __init__(self, driver):
        self.driver = driver

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_id(self):
        return self.driver.find_element(*HomePage.pwd)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_radio_button(self):
        return self.driver.find_element(*HomePage.radio_button)

    def get_date(self):
        return self.driver.find_element(*HomePage.date)

    def get_submit_button(self):
        return self.driver.find_element(*HomePage.submit_button)

    def get_success_msg(self):
        return self.driver.find_element(*HomePage.success_msg)

