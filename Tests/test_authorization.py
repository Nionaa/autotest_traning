
def test_authorization_pass(app_fixture):
    app_fixture.open_page()
    app_fixture.authorization.enter_page()
    app_fixture.authorization.frame_switch()
    app_fixture.authorization.login_field()
    app_fixture.authorization.password_field()
    app_fixture.authorization.enter_button()


