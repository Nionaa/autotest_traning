import data_storage
from selenium import webdriver

wb = webdriver.Chrome()


def open_page():
    wb.get("https://www.wildberries.ru/")


def enter_page():
    wb.find_element_by_link_text("Регистрация").click()
    wb.find_element_by_class_name("auth-tabs-switch").click()


def login_field():
    login = wb.find_element_by_css_selector("#Item_Login")
    login.clear()
    login.send_keys(data_storage.username)


def password_field():
    password = wb.find_element_by_name("Item.Password")
    password.clear()
    password.send_keys(data_storage.password1)


def enter_button():
    wb.find_element_by_class_name("auth-btn-login").click()



