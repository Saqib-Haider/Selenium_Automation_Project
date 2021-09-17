from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

class Ecomm(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get('http://www.tutorialsninja.com/demo/')



    def test_cart(self):
        self.driver.find_element_by_link_text("Cameras").click()
        self.driver.find_element_by_link_text("Nikon D300").click()
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[1]/ul[1]/li[1]/a/img").click()
        self.next_btn = self.driver.find_element_by_xpath("/html/body/div[2]/div/button[2]")

        for i in range(0, 5):
            self.next_btn.click()
            time.sleep(2)

        self.driver.save_screenshot("Site Screenshots.png")
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div[1]/div/button").click()
        time.sleep(1)

        iq = self.driver.find_element_by_xpath("//*[@id='input-quantity']")
        iq.click()
        time.sleep(1)
        iq.clear()
        time.sleep(1)
        iq.send_keys("2")
        self.driver.find_element_by_xpath("//*[@id='button-cart']").click()

        actions = ActionChains(self.driver)
        hov_element = self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[3]/a")
        actions.move_to_element(hov_element).perform()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='menu']/div[2]/ul/li[3]/div/div/ul/li[2]/a").click()
        time.sleep(1)

        self.driver.find_element_by_xpath("//*[@id='content']/div[3]/div[2]/div/div[2]/div[1]/h4/a").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='button-cart']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='cart-total']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='cart']/ul/li[2]/div/p/a[1]/strong").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='content']/div[3]/div[2]/a").click()
        time.sleep(1)

        self.driver.find_element_by_xpath("//*[@id='collapse-checkout-option']/div/div/div[1]/div[2]/label").click()
        time.sleep(1)

        self.driver.find_element_by_xpath("//*[@id='button-account']").click()
        time.sleep(1)


        scroll_options = self.driver.find_element_by_xpath("//*[@id='collapse-payment-address']/div")
        scroll_options.location_once_scrolled_into_view
        time.sleep(1)

        self.driver.find_element_by_name("firstname").send_keys("Jack")
        time.sleep(1)
        self.driver.find_element_by_name("lastname").send_keys("Kettle")
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='input-payment-email']").send_keys(("jacktesting101@hotmail.com"))
        time.sleep(1)
        self.driver.find_element_by_name("telephone").send_keys("01773408567")
        time.sleep(1)
        self.driver.find_element_by_name("address_1").send_keys("Street:13, Con Hills")
        time.sleep(1)
        self.driver.find_element_by_name("city").send_keys("Dhaka")
        time.sleep(1)
        self.driver.find_element_by_name("postcode").send_keys("1120")
        time.sleep(1)
        country_code = self.driver.find_element_by_xpath("//*[@id='input-payment-country']")
        country_select = Select(country_code)
        country_select.select_by_value("18")
        time.sleep(2)
        region = self.driver.find_element_by_xpath("//*[@id='input-payment-zone']")
        region_select = Select(region)
        region_select.select_by_visible_text("Dhaka")
        time.sleep(2)
        self.driver.find_element_by_xpath("//*[@id='button-guest']").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//*[@id='button-shipping-method']").click()
        time.sleep(1)

        self.driver.find_element_by_name("agree").click()
        self.driver.find_element_by_xpath("//*[@id='button-payment-method']").click()
        time.sleep(1)

        total = self.driver.find_element_by_xpath("//*[@id='collapse-checkout-confirm']/div/div[1]/table/tfoot/tr[3]/td[2]")
        print("The full price is:" + total.text)
        self.driver.find_element_by_xpath("//*[@id='button-confirm']").click()
        time.sleep(1)

        title = self.driver.title
        if title == "Your order has been placed!":
            print("Test Passed and Completed Successfully")
        else:
            print("Test Failed. Result Unknown")

        self.driver.find_element_by_xpath("//*[@id='content']/div/div/a").click()

    def test_title(self):
        self.assertEqual("Your Store",self.driver.title,"Title not matching")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()



if __name__ == "__main__":
    unittest.main()
