from Precondition import data_storage
from selenium import webdriver

wb = webdriver.Chrome()


def open_page():
    wb.get("https://www.wildberries.ru/")

def enter_page():
    wb.find_element_by_link_text("Войти").click()

def frame_switch():
    wb.switch_to.frame(wb.find_element_by_tag_name("iframe"))

def login_field():
    login = wb.find_element_by_css_selector("#Item_Login")
    login.clear()
    login.send_keys(data_storage.username)

def password_field():
    password = wb.find_element_by_css_selector("#Item_Password")
    password.clear()
    password.send_keys(data_storage.password1)

def enter_button():
    wb.find_element_by_id("signIn").click()
    wb.switch_to.default_content()

def quit():
    wb.quit()

def aut_iframe():
    open_page()
    enter_page()
    frame_switch()
    login_field()
    password_field()
    enter_button()
    quit()



