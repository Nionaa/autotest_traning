
class ProfilePage:

    def __init__(self,driver):
        self.driver = driver

    def main_personal_cab_page(self):
        driver = self.driver
        driver.find_element_by_link_text('Личный кабинет')

    def profile_section(self):
        driver = self.driver
        driver.find_element_by_link_txt('Профиль')