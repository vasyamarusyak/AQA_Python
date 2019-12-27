from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import time


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)   # ініціалізуємо Page Object, передаємо в конструктор экземпляр драйвера и url адрес 
    page.open()                      # відкриваємо сторінку
    page.go_to_login_page()          # викликаємо метод go_to_login_page. Перейшли на сторінку логіну.
    time.sleep(5)
    login_page = LoginPage(browser, browser.current_url)# Ініціалізуємо LoginPage в тілі тесту, для того шоб викликати методи із файлу login_page 
    login_page.should_be_login_page()# із файлу login_page викликаємо метод should_be_login_page
    
def test_check_login_and_register(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    page =  LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    

