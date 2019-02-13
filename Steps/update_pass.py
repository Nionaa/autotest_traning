from Precondition import data_storage

class PassChange():
    def __init__(self, app):
        self.app = app

    def pass_update(self):
        wd = self.app.wd
        wd.find_element_by_id("updatePassword").click()
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))
        currentpass = wd.find_element_by_id("Item_OldPassword")
        currentpass.send_keys(data_storage.password1)
        newpass = wd.find_element_by_id("Item_Password")
        newpass.send_keys(data_storage.password2)
        confirmpass = wd.find_element_by_id("Item_ConfirmPassword")
        confirmpass.send_keys(data_storage.password2)
        wd.find_element_by_class_name("save").click()
        wd.switch_to.default_content()

    def rerurn_password(self):
        wd = self.app.wd
        wd.find_element_by_id("updatePassword").click()
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))
        currentpass = wd.find_element_by_id("Item_OldPassword")
        currentpass.send_keys(data_storage.password2)
        newpass = wd.find_element_by_id("Item_Password")
        newpass.send_keys(data_storage.password1)
        confirmpass = wd.find_element_by_id("Item_ConfirmPassword")
        confirmpass.send_keys(data_storage.password1)
        wd.find_element_by_class_name("save").click()
        wd.switch_to.default_content()