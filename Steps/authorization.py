from Precondition import data_storage

class Authorization:

    def __init__(self,driver):
        self.driver = driver

    def enter_page(self):
        driver = self.driver
        driver.find_element_by_link_text("Войти").click()

    def frame_switch(self):
        driver = self.driver
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

    def login_field(self):
        driver = self.driver
        login = driver.find_element_by_css_selector("#Item_Login")
        login.clear()
        login.send_keys(data_storage.username)

    def password_field(self):
        driver = self.driver
        password = driver.find_element_by_css_selector("#Item_Password")
        password.clear()
        password.send_keys(data_storage.password1)

    def enter_button(self):
        driver = self.driver
        driver.find_element_by_id("signIn").click()
        driver.switch_to.default_content()
