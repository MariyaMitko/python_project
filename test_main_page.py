import time

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)

    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, link)
    login_page = LoginPage(browser, link)

    main_page.open()
    main_page.click_login_link()
    login_page.should_open_login_page()


def test_guest_can_see_login_form(browser):
    main_page = MainPage(browser, link)
    login_page = LoginPage(browser, link)

    main_page.open()
    main_page.click_login_link()
    login_page.should_be_login_form()


def test_guest_can_see_registration_form(browser):
    main_page = MainPage(browser, link)
    login_page = LoginPage(browser, link)

    main_page.open()
    main_page.click_login_link()
    login_page.should_be_register_form()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    main_page = MainPage(browser, link)
    basket_page = BasketPage(browser, link, 1)

    main_page.open()
    main_page.go_to_basket()
    basket_page.get_basket_items_count(0)
    basket_page.info_msg_is_displayed()
