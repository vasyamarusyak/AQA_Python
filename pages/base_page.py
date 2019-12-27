from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import math
import time

class BasePage():    
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    #This code is for quiz
    def solve_quiz_and_get_code(self):
        #WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
           # WebDriverWait(self.browser, 3).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

#Коли ми пишемо у методі змінні how, what у цьому файлі - то це значить що таким чином ми просто
#об*являємо що в методі будуть такі змінні. А от у файлі product_page ми вже викликаємо цей метод
#і вносимо свої конкретні змінні.
            
#Цей метод перевіряє що елемент не з*являється на сторінці протягом заданого часу
    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
    
    

#Коли ми хочемо перевірити, що якийсь елемент щзникає, тоді варто використовувати явне очікування
#разом із функцією until_not, в залежності від того, який результат ми очікуємо.

#Метод is_disappeared: буде чекати до тих пір поки елемент не зникне.
    def is_disappeared(self, how, what, timeout=4):
        try:
            #Озаначає що чекаємо 4 сек і перевіряємо через 1 сек чи не з*явився елемент
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True

