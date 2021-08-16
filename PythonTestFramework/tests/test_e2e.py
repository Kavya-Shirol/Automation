import time

from BasePackage.BaseClass import BaseClass
from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.ConfirmPage import ConfirmPage
from PageObjects.HomePage import HomePage
from PageObjects.SuccessPage import SuccessPage


class TestE2E(BaseClass):

    def test_e2e(self):

        homeobj = HomePage(self.driver)
        homeobj.search_box().send_keys("cum")
        time.sleep(5)
        products = homeobj.get_products()
        count = len(products)
        print(count)
        assert count == 2
        buttons = homeobj.get_buttons()
        for button in buttons:
            button.click()
        homeobj.get_cart_button().click()
        homeobj.get_proceed_button().click()

        self.wait("promoCode")
        checkoutobj = CheckoutPage(self.driver)
        checkoutobj.send_promo_code().send_keys("rahulshettyacademy")
        checkoutobj.get_apply_button().click()

        self.wait("promoInfo")
        print(checkoutobj.get_promo_info())
        checkoutobj.place_order().click()
        self.select_dropdown("India")

        confirmobj = ConfirmPage(self.driver)
        confirmobj.click_checkbox().click()

        successobj = SuccessPage(self.driver)
        successobj.click_proceed().click()




