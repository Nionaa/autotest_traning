from selenium import webdriver
from Steps.authorization import Authorization
from Steps.profile_page import ProfilePage

class Application:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.authorization = Authorization(self.driver)
        self.profile_page = ProfilePage(self.driver)

    def open_page(self):
        wb = self.driver
        wb.get("https://www.wildberries.ru/")

    def quit(self):
        self.driver.quit()