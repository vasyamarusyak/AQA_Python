from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
    time.sleep(2)
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    time.sleep(10)

