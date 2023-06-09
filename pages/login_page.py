from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.inpt_login_form = (By.CSS_SELECTOR, "#login_form")
        self.inpt_login_email = (By.CSS_SELECTOR, "[name='login-username']")
        self.inpt_login_password = (By.CSS_SELECTOR, "[name='login-password']")
        self.btn_login_submit = (By.CSS_SELECTOR, "[name='login-submit']")
        self.inpt_reg_form = (By.CSS_SELECTOR, "#registration_form")
        self.inpt_reg_email = (By.CSS_SELECTOR, "[name='registration_email']")
        self.inpt_reg_password = (By.CSS_SELECTOR, "[name='registration-password1']")
        self.inpt_reg_password_confirm = (By.CSS_SELECTOR, "[name='registration-password2']")
        self.btn_reg_submit = (By.CSS_SELECTOR, "[name='registration_submit']")

    def should_be_login_page(self):
        self.get_current_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_form(self):
        return self.is_element_present(*self.inpt_login_form)

    def should_be_register_form(self):
        return self.is_element_present(*self.inpt_reg_form)