from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "/login/" in self.browser.current_url, "MAY BE NOT 'LOGIN' PAGE" #Перевіряємо подстрока "login" есть в текущем url браузера.

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.L_FORM), "LOGIN FORM NOT FOUND"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.R_FORM), "REGISTER FORM NOT FOUND"

    #def register_new_user(self, email, password):
        #self.browser.find_element(*LoginPageLocators.EMAIL).send_keys(email)
        #self.browser.find_element(*LoginPageLocators.PASSWORD1).send_keys(password)
        #self.browser.find_element(*LoginPageLocators.PASSWORD2).send_keys(password)
        #self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
