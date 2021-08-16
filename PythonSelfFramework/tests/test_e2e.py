
import time
from pageobjects.Checkoutpage import CheckoutPage
from pageobjects.HomePage import HomePage
from utilities.Baseclass import BaseClass


class TestOne(BaseClass):

    def test_first(self):

        homepage = HomePage(self.driver)
        homepage.getsearch().send_keys("ber")
        time.sleep(5)
        print(len(homepage.getproducts()))
        buttons = homepage.getbuttons()
        print(len(buttons))
        for button in buttons:
            button.click()
        homepage.getimagebutton().click()
        homepage.getproceedbutton().click()

        self.verify_presence_of_element("promoCode")
        checkoutpage = CheckoutPage(self.driver)
        checkoutpage.sendpromocode().send_keys("rahulshettyacademy")

        checkoutpage.getpromobutton().click()
        self.verify_presence_of_element("promoInfo")
        print(checkoutpage.getpromoinfo().text)
        confirmpage = checkoutpage.getplaceorderbutton()

        self.select_text(confirmpage.get_tag(), "India")
        confirmpage.getcheckbox().click()
        confirmpage.getproceedbutton().click()
        time.sleep(5)


