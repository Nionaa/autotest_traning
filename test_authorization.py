import authorization


def test_authorization_pass():
    authorization.open_page()
    authorization.enter_page()
    authorization.frame_switch()
    authorization.login_field()
    authorization.password_field()
    authorization.enter_button()
    authorization.quit()