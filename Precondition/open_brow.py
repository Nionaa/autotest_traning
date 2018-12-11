from selenium import webdriver

class Application:
    def __init__(self, browser):
        if browser == "firefox":
            self.wb = webdriver.Firefox()
        elif browser == "chrome":
            self.wb = webdriver.Chrome()
        elif browser == "ie":
            self.wb = webdriver.Ie()
        else:
            raise ValueError ("Unrecognize browser %s" % browser)

    def open_page(self):
        wd = self.wb
        wd.get("https://www.wildberries.ru/")
    def quit(self):
        self.wb.quit()