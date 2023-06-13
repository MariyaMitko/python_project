from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def should_open_login_page(self):
        url_text = self.get_current_url()
        assert '/login' in url_text, f"Login page should be opened, but {url_text} opened"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.login_form), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.reg_form), "Registration form is not presented"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.inpt_reg_email).send_keys(email)
        self.browser.find_element(*LoginPageLocators.inpt_reg_password).send_keys(password)
        self.browser.find_element(*LoginPageLocators.inpt_reg_password_confirm).send_keys(password)
        self.browser.find_element(*LoginPageLocators.btn_reg_submit).click()
