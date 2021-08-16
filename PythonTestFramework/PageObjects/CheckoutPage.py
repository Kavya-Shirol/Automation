from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    promocode = (By.CSS_SELECTOR, "input[class='promoCode']")
    def send_promo_code(self):
        return self.driver.find_element(*CheckoutPage.promocode)

    applybutton = (By.XPATH, "//button[text()='Apply']")
    def get_apply_button(self):
        return self.driver.find_element(*CheckoutPage.applybutton)

    promoinfo = (By.CLASS_NAME, "promoInfo")
    def get_promo_info(self):
        return self.driver.find_element(*CheckoutPage.promoinfo)

    placeorder = (By.XPATH, "//button[text()='Place Order']")
    def place_order(self):
        return  self.driver.find_element(*CheckoutPage.placeorder)


