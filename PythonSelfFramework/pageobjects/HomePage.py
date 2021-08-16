from selenium.webdriver.common.by import By

class HomePage:
    
    search = (By.CSS_SELECTOR, ".search-keyword")
    products = (By.XPATH, "//div[@class='products']/div")
    buttons = (By.XPATH, "//div[@class='product-action']/button")
    image = (By.CSS_SELECTOR, "img[alt='Cart']")
    proceed = (By.XPATH, "//button[text()='PROCEED TO CHECKOUT']")

    def __init__(self, driver):
        self.driver = driver

    def getsearch(self):
        return self.driver.find_element(*HomePage.search)

    def getproducts(self):
        return self.driver.find_elements(*HomePage.products)

    def getbuttons(self):
        return self.driver.find_elements(*HomePage.buttons)

    def getimagebutton(self):
        return self.driver.find_element(*HomePage.image)

    def getproceedbutton(self):
        return self.driver.find_element(*HomePage.proceed)

