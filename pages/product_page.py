from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def add_to_basket(self):
        add_btn = self.browser.find_element(*ProductPageLocators.btn_add_to_basket)
        add_btn.click()

    def read_product_name(self):
        return self.browser.find_element(*ProductPageLocators.product_name).text

    def read_product_price(self):
        return self.browser.find_element(*ProductPageLocators.product_price).text

    def read_product_success_msg(self, product_name):
        actual_name = self.browser.find_element(*ProductPageLocators.product_msg).text
        assert f"{product_name} has been added to your basket" in actual_name, f"Expected {product_name} to be {actual_name}"

    def read_price_success_msg(self, price):
        actual_price = self.browser.find_element(*ProductPageLocators.price_msg).text
        assert f"Your basket total is now {price}" in actual_price, f"Expected {price} to be {actual_price}"

    def is_product_success_msg_not_displayed(self):
        assert self.is_element_present(
            *ProductPageLocators.product_msg) == False, f"Success message displaying is displayed"

    def is_product_success_msg_disappeared(self):
        assert self.is_disappeared(
            *ProductPageLocators.product_msg) == True, "Success message for product doesn't disappear"
