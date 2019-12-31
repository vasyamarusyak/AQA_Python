from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def test_guest_can_add_product_to_basket(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        link.click()

    def should_be_message_about_adding(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        # Перевіряємо що назва товару присутня в повідомленні про додавання товару.
        # assert product_name in message, \
        #       "No product name in the message"  #Перевіряємо що строка product_name є в строці message 
        assert product_name == message, \
            f"The alert contains wrong product name: {message} - {product_name}"  # Перевіряємо що строка product_name
        # дорівнює строці message

    def should_be_message_basket_total(self):
        # Спочатку перевіряємо що елементи присутні на сторінці
        assert self.is_element_present(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Message basket total is not presented")
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        # Отримуємо текст елементів для перевірки
        message_basket_total = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        # Перевіряємо що ціна товару присутня в повідомленні про  ціну корзини.
        assert product_price in message_basket_total, "No product price in the message"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING), \
            "Success message is presented, but should not be"
