from selenium.webdriver.common.by import By

from .base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.btn_add_to_basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
        self.product_name = (By.CSS_SELECTOR, ".product_main h1")
        self.product_price = (By.CSS_SELECTOR, ".price_color")
        self.product_msg = (By.CSS_SELECTOR, ".alert-success")
        self.price_msg = (By.CSS_SELECTOR, ".alert-info")
        self.inpt_reg_email = (By.CSS_SELECTOR, "[name='registration_email']")
        self.inpt_reg_password = (By.CSS_SELECTOR, "[name='registration-password1']")
        self.inpt_reg_password_confirm = (By.CSS_SELECTOR, "[name='registration-password2']")
        self.btn_reg_submit = (By.CSS_SELECTOR, "[name='registration_submit']")

    def add_to_basket(self):
        add_btn = self.browser.find_element(*self.btn_add_to_basket)
        add_btn.click()

    def read_product_name(self):
        return self.browser.find_element(*self.product_name).text

    def read_product_price(self):
        return self.browser.find_element(*self.product_price).text

    def read_product_success_msg(self):
        return self.browser.find_element(*self.product_msg).text

    def read_price_success_msg(self):
        return self.browser.find_element(*self.price_msg).text
