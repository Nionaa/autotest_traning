from selenium.common.exceptions import NoSuchElementException
from Precondition import data_storage

class Authorization():
    def __init__(self, app):
        self.app = app

    def enter_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Войти").click()

    def frame_switch(self):
        wd = self.app.wd
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))

    def login_field(self):
        wd = self.app.wd
        login = wd.find_element_by_css_selector("#Item_Login")
        login.clear()
        login.send_keys(data_storage.username)

    def password_field(self):
        wd = self.app.wd
        password = wd.find_element_by_css_selector("#Item_Password")
        password.clear()
        password.send_keys(data_storage.password1)

    def enter_button(self):
        wd = self.app.wd
        wd.find_element_by_id("signIn").click()
        wd.switch_to.default_content()

    def auth_check(self):
        wd = self.app.wd
        try:
            wd.find_element_by_id("error")
        except NoSuchElementException:
            wd.find_element_by_css_selector("#Item_Password").send_keys(data_storage.password2)
            wd.find_element_by_id("signIn").click()

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


