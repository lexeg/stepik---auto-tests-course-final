from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group a")
    BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner > p a")
    BASKET_FORMSET = (By.ID, "basket_formset")

class LoginPageLocators():
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    REGISTER_EMAIL_INPUT = (By.ID, "id_registration-email")
    REGISTER_PASSWORD_INPUT = (By.ID, "id_registration-password1")
    REGISTER_CONFIRM_PASSWORD_INPUT = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form button[name='registration_submit']")

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success:nth-child(1) strong")
    PRODUCT_PRICE_IN_BASKET_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-info strong")
