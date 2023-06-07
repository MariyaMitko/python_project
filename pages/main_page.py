from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.login_button = (By.CSS_SELECTOR, "#login_link")

    def go_to_login_page(self):
        login_link = self.browser.find_element(*self.login_button)
        login_link.click()

    def should_be_login_link(self):
        return self.is_element_present(*self.login_button)