from Precondition import data_storage

class PassChange():
    def __init__(self, app):
        self.app = app

    def pass_update_popup(self):
        wd = self.app.wd
        wd.find_element_by_id("updatePassword").click()

    def pass_frame_switch(self):
        wd = self.app.wd
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))

    def current_pass_key(self):
        wd = self.app.wd
        currentpass = wd.find_element_by_id("Item_OldPassword")
        currentpass.send_keys(data_storage.password1)

    def new_pass_key(self):
        wd = self.app.wd
        newpass = wd.find_element_by_id("Item_Password")
        newpass.send_keys(data_storage.password2)

    def confirm_pass_key(self):
        wd = self.app.wd
        confirmpass = wd.find_element_by_id("Item_ConfirmPassword")
        confirmpass.send_keys(data_storage.password2)

    def press_save_button(self):
        wd = self.app.wd
        wd.find_element_by_class_name("save").click()
        wd.switch_to.default_content()