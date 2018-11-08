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


def open_personalcab_main_page():
    wb.find_element_by_link_text("Личный кабинет").click()


def open_details_page():
    wb.find_element_by_link_text("Мои данные").click()


def pass_change_button():
    wb.find_element_by_id("updatePassword").click()


def fill_oldpass_field():
    # iframe1 = wb.find_elements_by_css_selector("#easyXDM_default4915_provider")
    # wb.switch_to.frame(iframe1)

    oldpass = wb.find_element_by_id("Item_OldPassword").click()
    oldpass.clear()
    oldpass.send_keys(data_storage.password1)
