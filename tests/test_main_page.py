from pages.main_page import MainPage
from pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)

    page.open()
    assert page.should_be_login_link(), "Login link is not presented"


def test_guest_can_go_to_login_page(browser):
    main_page = MainPage(browser, link)
    login_page = LoginPage(browser, link)

    main_page.open()
    main_page.click_login_link()
    url_text = login_page.get_current_url()
    assert '/login' in url_text, f"Login link should be opened, but link {url_text} opened"


def test_guest_can_see_login_form(browser):
    main_page = MainPage(browser, link)
    login_page = LoginPage(browser, link)

    main_page.open()
    main_page.click_login_link()
    assert login_page.should_be_login_form(), "Login form is not presented "


def test_guest_can_see_registration_form(browser):
    main_page = MainPage(browser, link)
    login_page = LoginPage(browser, link)

    main_page.open()
    main_page.click_login_link()
    assert login_page.should_be_register_form(), "Registration form is not presented "
