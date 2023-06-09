from ..pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_product_should_be_added_to_basket(browser):
    page = ProductPage(browser, link)

    page.open()
    product_name = page.read_product_name()
    price = page.read_product_price()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    actual_name = page.read_product_success_msg()
    assert product_name in actual_name, f"Expected {product_name} to be in {actual_name}"
    actual_price = page.read_price_success_msg()
    assert price in actual_price, f"Expected {price} to be in {actual_price}"
