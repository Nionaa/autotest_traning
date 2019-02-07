from selenium import webdriver
from Steps.authorization import Authorization
from Steps.update_pass import PassChange
from Steps.navigation import Navigation_buttons
from Precondition import data_storage


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.wd.implicitly_wait(10)
        self.base_url = data_storage.BASE_URL
        self.authorization = Authorization(self)
        self.navigation = Navigation_buttons(self)
        self.update_pass = PassChange(self)

    def open_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
