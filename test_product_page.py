from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
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


link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                                #Відкриваємо сторінку товару
    page.test_guest_can_add_product_to_basket()#Додаємо товар у корзину
    #time.sleep(1)
    page.should_not_be_success_message()       #Перевіряємо що немає повідомлення про успіх задопомогою is_not_element_present

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()                                
    page.should_not_be_success_message()       #Перевіряємо що немає повідомлення про успіх задопомогою is_not_element_present

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                                
    page.test_guest_can_add_product_to_basket()#Додаємо товар у корзину 
    time.sleep(1)
    page.should_not_be_success_message_after_adding_product_to_basket()#Перевіряємо що немає повідомлення про успіх задопомогою is_disappeared
    
@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)# надаємо доступ до методів із product_page класу ProductPage
    page.open()
    time.sleep(2)
    page.should_be_login_link()#оскільки ProductPage є наслідником BasePage, тоиу ми можемо
                               # використати цей метод.
    time.sleep(2)
    
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(2)
    login_page = LoginPage(browser, browser.current_url)#Переключаємось на login_page і маємо 
                                                        #доступ до методів із класу LoginPage 
    login_page.should_be_login_page()#оскільки LoginPage є наслідником BasePage, тому ми можемо
                                     # використати метод should_be_login_page() із BasePage.

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()                                              
    page.test_guest_can_go_to_basket()                     #Переходимо у корзину по кнопці із шапки сайту 
    basket_page = BasketPage(browser, browser.current_url) #Переключаємось на basket_page і маємо 
                                                           #доступ до методів із класу BasketPage
    basket_page.should_not_be_any_products_in_busket()     #Очікуємо що у корзині немає ніяких товарів
    print("Method should_not_be_any_products_in_busket --- finished")
    basket_page.should_be_empty_basket_page_with_text()    #Очікуємо що є текст про те що корзина пуста

#pytest  -v -s --tb=line test_product_page.py





                                     


