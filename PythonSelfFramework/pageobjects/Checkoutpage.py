from selenium.webdriver.common.by import By

from pageobjects.confirmpage import ConfirmPage


class CheckoutPage:

    code = (By.CSS_SELECTOR, ".promoCode")
    promobutton = (By.CLASS_NAME, "promoBtn")
    promoinfo = (By.CLASS_NAME, "promoInfo")
    placeorder = (By.XPATH, "//button[text()='Place Order']")
    def __init__(self, driver):
        self.driver = driver

    def sendpromocode(self):
        return self.driver.find_element(*CheckoutPage.code)

    def getpromobutton(self):
        return self.driver.find_element(*CheckoutPage.promobutton)

    def getpromoinfo(self):
        return self.driver.find_element(*CheckoutPage.promoinfo)

    def getplaceorderbutton(self):
        self.driver.find_element(*CheckoutPage.placeorder).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage