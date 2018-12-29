from Precondition import data_storage

class Authorization:

    def __init__(self,driver):
        self.driver = driver

    def enter_page(self):
        self.driver.find_element_by_link_text("Войти").click()

    def frame_switch(self):
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))

    def login_field(self):
        login = self.driver.find_element_by_css_selector("#Item_Login")
        login.clear()
        login.send_keys(data_storage.username)

    def password_field(self):
        password = self.driver.find_element_by_css_selector("#Item_Password")
        password.clear()
        password.send_keys(data_storage.password1)

    def enter_button(self):
        self.driver.find_element_by_id("signIn").click()
        self.driver.switch_to.default_content()
