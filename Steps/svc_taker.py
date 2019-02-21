from Precondition import data_storage
import time
import re

class SvsTaker:
    def __init__(self, app):
        self.app = app

    def open_new_wind(self):
        wd = self.app.wd
        wd.execute_script("window.open('');")

    def switch_to_new_window(self):
        wd = self.app.wd
        wd.switch_to.window(wd.window_handles[1])
        wd.get(data_storage.SVS_URL)

    def login_pass(self):
        wd = self.app.wd
        login_form = wd.find_element_by_xpath("/html/body/div/div/div/section/form/div[1]/input")
        login_form.send_keys(data_storage.myname)

    def passwd_pass(self):
        wd = self.app.wd
        pass_form = wd.find_element_by_xpath("/html/body/div/div/div/section/form/div[2]/input")
        pass_form.send_keys(data_storage.mypassword)

    def submit_button(self):
        wd = self.app.wd
        wd.find_element_by_xpath("/html/body/div/div/div/section/form/div[3]/button").click()

    def sms_log_finder(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='sidebar-menu']/div/ul/li[1]/a").click()
        wd.find_element_by_xpath("//*[@id='sidebar-menu']/div/ul/li[1]/ul/li[1]/a").click()

    def number_search(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//*[@id='carousel-content']/nav/form/div[3]/button[1]").click()
        time.sleep(2)
        number_field = wd.find_element_by_id("find-number")
        number_field.send_keys(data_storage.number)
        wd.find_element_by_xpath("//*[@id='find-panel']/div/div/div[3]/button[2]").click()
        time.sleep(2)

    def svc_code(self):
        wd = self.app.wd
        message = wd.find_element_by_xpath("//*[@id='sms-list-content']/table/tbody/tr[1]/td[9]").text
        numbers = re.split('\D', message)[32]
        # global svc
        svc = list(map(str, numbers))
        return svc

    def return_window(self):
        wd = self.app.wd
        wd.switch_to.window(wd.window_handles[0])

    def svc_code_full(self):
        wd = self.app.wd
        wd.execute_script("window.open('');")
        wd.switch_to.window(wd.window_handles[1])
        wd.get(data_storage.SVS_URL)
        login_form = wd.find_element_by_xpath("/html/body/div/div/div/section/form/div[1]/input")
        login_form.send_keys(data_storage.myname)
        pass_form = wd.find_element_by_xpath("/html/body/div/div/div/section/form/div[2]/input")
        pass_form.send_keys(data_storage.mypassword)
        wd.find_element_by_xpath("/html/body/div/div/div/section/form/div[3]/button").click()
        wd.find_element_by_xpath("//*[@id='sidebar-menu']/div/ul/li[1]/a").click()
        wd.find_element_by_xpath("//*[@id='sidebar-menu']/div/ul/li[1]/ul/li[1]/a").click()
        wd.find_element_by_xpath("//*[@id='carousel-content']/nav/form/div[3]/button[1]").click()
        time.sleep(2)
        number_field = wd.find_element_by_id("find-number")
        number_field.send_keys(data_storage.number)
        wd.find_element_by_xpath("//*[@id='find-panel']/div/div/div[3]/button[2]").click()
        time.sleep(2)
        message = wd.find_element_by_xpath("//*[@id='sms-list-content']/table/tbody/tr[1]/td[9]").text
        numbers = re.split('\D', message)[32]
        # global svc
        svc = list(map(str, numbers))
        return svc
