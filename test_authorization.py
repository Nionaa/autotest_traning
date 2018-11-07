import authorization

def test_authorization():
    authorization.open_page()
    authorization.enter_privatcabinet()
    authorization.login_field()
    authorization.password_field()
    authorization.login_privatcabinet()
    authorization.quit()