import time
link = "http://selenium1py.pythonanywhere.com/"

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    time.sleep(10)
    #go_to_login_page(browser) 
