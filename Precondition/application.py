from selenium import webdriver
from Precondition import data_storage
from Steps.authorization import Authorization
from Steps.navigation import Navigation_buttons
from Steps.update_pass import PassChange


class Application:

    # Инициализация драйвера в классах
    def __init__(self):
        self.wd = webdriver.Chrome()
        self.base_url = data_storage.BASE_URL
        self.authorization = Authorization(self)
        self.navigation = Navigation_buttons(self)
        self.update_pass = PassChange(self)

    # Переход по ссылке
    def open_page(self):
        wd = self.wd
        wd.get(self.base_url)

    # Закрытие браузера и веб.драйвера
    def destroy(self):
        self.wd.quit()

