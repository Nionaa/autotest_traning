from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Navigation_buttons():
    def __init__(self, app):
        self.app = app

    def main_lk(self):
        wd = self.app.wd
        menu = WebDriverWait(wd, 20).until(EC.presence_of_element_located((By.LINK_TEXT,"Личный кабинет")))
        menu.click()

    def profile_navigation(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Профиль").click()