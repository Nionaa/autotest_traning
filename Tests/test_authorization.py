from Precondition import application
from Steps import authorization
from Steps import profile_page

def open():
    application.Application()

def test_authorization_pass():
    authorization.Authorization()

def enter_profile_page():
    profile_page.ProfilePage()

