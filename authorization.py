import data_storage
from selenium import webdriver


wb = webdriver.Firefox()

def open_page():
    wb.get("https://www.wildberries.ru/")

def enter_privatcabinet():
    wb.find_element_by_link_text("Войти").click()

def login_field():
    wb.find_element_by_xpath("//input[@type='text']").send_keys(data_storage.username)


def password_field():
    wb.find_element_by_xpath("//input[@type='password']").send_keys(data_storage.password1)

def login_privatcabinet():
    wb.find_element_by_id("signIn").click()

def quit():
    wb.quit()