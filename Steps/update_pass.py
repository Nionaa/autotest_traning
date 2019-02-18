from Precondition import data_storage

class PassChange():
    def __init__(self, app):
        self.app = app

    # Полная смена пароля (первый раз)
    def pass_update(self):
        wd = self.app.wd
        # Находим блок изменение паролья
        wd.find_element_by_id("updatePassword").click()
        # Переход на окно попапа
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))
        # Введение текущего пароля
        currentpass = wd.find_element_by_id("Item_OldPassword")
        currentpass.send_keys(data_storage.password1)
        # Введение нового пароля
        newpass = wd.find_element_by_id("Item_Password")
        newpass.send_keys(data_storage.password2)
        # Подтверждение нового пароля
        confirmpass = wd.find_element_by_id("Item_ConfirmPassword")
        confirmpass.send_keys(data_storage.password2)
        # Нажать на кнопку "Сохранить"
        wd.find_element_by_class_name("save").click()
        wd.switch_to.default_content()

    # Полная смена пароя (возврат пароля)
    def rerurn_password(self):
        wd = self.app.wd
        # Находим блок изменение паролья
        wd.find_element_by_id("updatePassword").click()
        # Переход на окно попапа
        wd.switch_to.frame(wd.find_element_by_tag_name("iframe"))
        # Введение текущего пароля
        currentpass = wd.find_element_by_id("Item_OldPassword")
        currentpass.send_keys(data_storage.password2)
        # Введение нового пароля
        newpass = wd.find_element_by_id("Item_Password")
        newpass.send_keys(data_storage.password1)
        # Подтверждение нового пароля
        confirmpass = wd.find_element_by_id("Item_ConfirmPassword")
        confirmpass.send_keys(data_storage.password1)
        # Нажать на кнопку "Сохранить"
        wd.find_element_by_class_name("save").click()
        wd.switch_to.default_content()