from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time
import pytest# для того щоб xfail тест працював.


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link):
    #link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/?promo=newYear2019"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
    #time.sleep(2)
    page.solve_quiz_and_get_code()
    #time.sleep(2)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    #time.sleep(10)

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
    time.sleep(2)
    page.should_not_be_success_message()


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                                #Відкриваємо сторінку товару
    page.test_guest_can_add_product_to_basket()#Додаємо товар у корзину
    #time.sleep(1)
    page.should_not_be_success_message()       #Перевіряємо що немає повідомлення про успіх задопомогою is_not_element_present

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()                                
    page.should_not_be_success_message()       #Перевіряємо що немає повідомлення про успіх задопомогою is_not_element_present

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                                
    page.test_guest_can_add_product_to_basket()#Додаємо товар у корзину 
    time.sleep(1)
    page.should_not_be_success_message_after_adding_product_to_basket()#Перевіряємо що немає повідомлення про успіх задопомогою is_disappeared


#pytest  -v -s --tb=line test_product_page.py


