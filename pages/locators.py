from selenium.webdriver.common.by import By


class BasePageLocators():
    user_icon = (By.CSS_SELECTOR, ".icon-user")
    go_to_basket_btn = (By.CSS_SELECTOR, ".basket-mini a")
    login_link = (By.CSS_SELECTOR, "#login_link")


class BasketPageLocators():
    alert_msg = (By.CSS_SELECTOR, "#content_inner")
    basket_items = (By.CSS_SELECTOR, ".basket-items")


class LoginPageLocators():
    login_form = (By.CSS_SELECTOR, "#login_form")
    reg_form = (By.CSS_SELECTOR, "#register_form")
    inpt_reg_email = (By.CSS_SELECTOR, "[name='registration-email']")
    inpt_reg_password = (By.CSS_SELECTOR, "[name='registration-password1']")
    inpt_reg_password_confirm = (By.CSS_SELECTOR, "[name='registration-password2']")
    btn_reg_submit = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    btn_add_to_basket = (By.CSS_SELECTOR, ".btn-add-to-basket")
    product_name = (By.CSS_SELECTOR, ".product_main h1")
    product_price = (By.CSS_SELECTOR, ".price_color")
    product_msg = (By.CSS_SELECTOR, ".alert-success")
    price_msg = (By.CSS_SELECTOR, ".alert-info")