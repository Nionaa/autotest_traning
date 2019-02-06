from selenium import webdriver
from Steps.authorization import Authorization
from Steps.profile_page import ProfilePage


class Application:
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.base_url = "https://www.wildberries.ru/"
        self.authorization = Authorization(self)
        self.profile_page = ProfilePage(self)

    def open_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
