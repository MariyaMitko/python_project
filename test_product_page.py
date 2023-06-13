import time
import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["offer0",
                                  "offer1",
                                  "offer2",
                                  "offer3",
                                  "offer4",
                                  "offer5",
                                  "offer6",
                                  pytest.param("offer7", marks=pytest.mark.xfail),
                                  "offer8",
                                  "offer9"
                                  ])
def test_guest_can_add_product_to_basket(browser, link):
    current_link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={link}"
    page = ProductPage(browser, current_link)
    print(f"Open {current_link}")
    page.open()
    product_name = page.read_product_name()
    price = page.read_product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.read_product_success_msg(product_name)
    page.read_price_success_msg(price)


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link, 0)
    page.open()
    page.add_to_basket()
    page.is_product_success_msg_not_displayed()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_link, 0)
    page.open()
    page.is_product_success_msg_not_displayed()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_link, 0)
    page.open()
    page.add_to_basket()
    page.is_product_success_msg_disappeared()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, product_link)
    basket_page = BasketPage(browser, product_link, 1)

    product_page.open()
    product_page.go_to_basket()
    basket_page.get_basket_items_count(0)
    basket_page.info_msg_is_displayed()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)
    login_page = LoginPage(browser, link)
    product_page.open()
    product_page.click_login_link()
    login_page.should_open_login_page()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, product_link)
    login_page = LoginPage(browser, product_link)
    product_page.open()
    product_page.click_login_link()
    login_page.should_open_login_page()


class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, "http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        email = f"{str(time.time())}@fakemail.org"
        password = f"{str(time.time())}"
        login_page.open()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, product_link, 0)
        page.open()
        page.is_product_success_msg_not_displayed()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, product_link)
        page.open()
        product_name = page.read_product_name()
        price = page.read_product_price()
        page.add_to_basket()
        page.read_product_success_msg(product_name)
        page.read_price_success_msg(price)
