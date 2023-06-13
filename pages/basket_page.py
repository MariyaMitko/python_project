from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)

    def info_msg_is_displayed(self):
        text = self.browser.find_element(*BasketPageLocators.alert_msg).text
        assert text == "Your basket is empty. Continue shopping", f"Message 'Your basket is empty' should be " \
                                                                  f"displayed, but {text} found"

    def get_basket_items_count(self, expected_count):
        items_count = len(self.browser.find_elements(*BasketPageLocators.basket_items))
        assert items_count == expected_count, f"Basket should contain {expected_count} items, but {items_count} items found"
