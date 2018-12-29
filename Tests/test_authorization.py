from Precondition import application
from Steps import authorization
from Steps import profile_page

def open():
    application.Application.__init__()
    application.Application.open_page()

def test_authorization_pass():
    authorization.Authorization()

def enter_profile_page():
    profile_page.ProfilePage()