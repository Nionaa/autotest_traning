from Precondition import data_storage
from Steps.svc_taker import SvsTaker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class EmailChange:
    def __init__(self, app):
        self.app = app

    def email_change_button_click(self):
        wd = self.app.wd
        wd.find_element_by_id("changeEmail").click()

    def iframe_switch(self):
        wd = self.app.wd
        iframe = wd.find_element_by_tag_name("iframe")
        wd.switch_to.frame(iframe)


    def new_email_enter(self):
        wd = self.app.wd
        new_email_field = wd.find_element_by_id("Item_Email").click()
        new_email_field.send_keys(data_storage.username2)

    def press_confirm_button(self):
        wd = self.app.wd
        wd.find_element_by_class_name("j-request-confirm-code button button9").click()

    def enter_confirm_code(self):
        wd = self.app.wd
        confirm_field = WebDriverWait(wd, 20).until(EC.presence_of_element_located((By.ID,"Item_ConfirmCode")))
        confirm_field.send_keys(SvsTaker().svc_code_full().svc)
