class ProfilePage:

    def __init__(self, app):
        self.app = app

    def main_personal_cab_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text('Личный кабинет')

    def profile_section(self):
        wd = self.app.wd
        wd.find_element_by_link_txt('Профиль')
