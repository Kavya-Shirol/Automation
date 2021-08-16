from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

    searchbox = (By.CLASS_NAME, "search-keyword")
    def search_box(self):
        return self.driver.find_element(*HomePage.searchbox)

    products = (By.XPATH, "//div[@class='products']/div")
    def get_products(self):
        return self.driver.find_elements(*HomePage.products)

    buttons = (By.XPATH, "//div[@class='product-action']/button")
    def get_buttons(self):
        return self.driver.find_elements(*HomePage.buttons)

    cartbutton = (By.CLASS_NAME, "cart-icon")
    def get_cart_button(self):
        return self.driver.find_element(*HomePage.cartbutton)

    proceedbutton = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")
    def get_proceed_button(self):
        return self.driver.find_element(*HomePage.proceedbutton)

