from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators

class BasketPage(BasePage):    
    #Спочатку перевіряємо що текст, що корзина пуста, присутній на сторінці, а потім витягуємо повідомлення
    # що корзина пуста, і порівнюємо із еталонним значенням.
    def should_be_empty_basket_page_with_text(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), (
            "Message about empty basket is not presented")
        text_in_message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        message = "Your basket is empty. Continue shopping"
        assert text_in_message == message, \
             f"The alert contains text in message: {message} - {text_in_message}"

    def should_not_be_any_products_in_busket(self):
    #Перевіряємо що елемент BASKET_WITH_PRODUCTS не присутній.
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_PRODUCTS), \
            "Product is presented, but should not be"






        

