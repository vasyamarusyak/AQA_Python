from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        time.sleep(5)
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_check_login_and_register(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()
    page.test_guest_can_go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_any_products_in_busket()
    print("Method 'should_not_be_any_products_in_busket' --- finished")
    basket_page.should_be_empty_basket_page_with_text()

# pytest  -v -s --tb=line test_main_page.py -m login_guest - для того щоб запустити тести із міткою login_guest
