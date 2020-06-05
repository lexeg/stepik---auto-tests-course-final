from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket_button.click()

    def should_be_product_in_basket(self, book_name):
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET_MESSAGE)
        text = message.text
        assert text == book_name, f"Book name in basket not equal to choosen book. Should be 'The shellcoder's handbook', but was {text}"

    def should_be_price_in_basket_equal_to_product_price(self, book_price):
        message = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_MESSAGE)
        text = message.text
        assert text == book_price, f"Book price in basket not equal to choosen book price. Should be '£9.99', but was {text}"
