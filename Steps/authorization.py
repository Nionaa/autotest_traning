from selenium.common.exceptions import NoSuchElementException
from Precondition import data_storage

class Authorization():
    def __init__(self, app):
        self.app = app

    # Поиск и нажатие на кнопку "Войти"
    def enter_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Войти").click()

    # Переход на окно попапа
    def frame_switch(self):
        wd = self.app.wd
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))

    # Ввод данных в поле "Логин"
    def login_field(self):
        wd = self.app.wd
        login = wd.find_element_by_css_selector("#Item_Login")
        login.clear()
        login.send_keys(data_storage.username)

    # Ввод данных в поле "Пароль"
    def password_field(self):
        wd = self.app.wd
        password = wd.find_element_by_css_selector("#Item_Password")
        password.clear()
        password.send_keys(data_storage.password1)

    # Нажатие на кнопку "Войти" (в ЛК)
    def enter_button(self):
        wd = self.app.wd
        wd.find_element_by_id("signIn").click()
        wd.switch_to.default_content()

    # Авторизация в одной функции (пароль 1)
    def auth_steps(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Войти").click()
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))
        login = wd.find_element_by_css_selector("#Item_Login")
        login.clear()
        login.send_keys(data_storage.username)
        password = wd.find_element_by_css_selector("#Item_Password")
        password.clear()
        password.send_keys(data_storage.password1)
        wd.find_element_by_id("signIn").click()
        wd.switch_to.default_content()

    # Авторизация в одной функции (пароль 2)
    def auth_steps2(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Войти").click()
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))
        login = wd.find_element_by_css_selector("#Item_Login")
        login.clear()
        login.send_keys(data_storage.username)
        password = wd.find_element_by_css_selector("#Item_Password")
        password.clear()
        password.send_keys(data_storage.password2)
        wd.find_element_by_id("signIn").click()
        wd.switch_to.default_content()