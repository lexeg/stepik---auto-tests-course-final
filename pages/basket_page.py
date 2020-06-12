from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), "Basket empty is not presented"

    def should_not_be_basket_formset(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_FORMSET), "Basket formset is presented, but should not be"
