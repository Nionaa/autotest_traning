def test_email_change_pass(app_fixture):
    app_fixture.open_page()
    app_fixture.authorization.auth_steps()
    app_fixture.navigation.main_lk()
    app_fixture.navigation.profile_navigation()
    app_fixture.email_change.iframe_switch()
    app_fixture.email_change.email_change_button_click()
    app_fixture.email_change.new_email_enter()
    app_fixture.email_change.press_confirm_button()
    app_fixture.svc_taker.svc_code_full()
    app_fixture.email_change.enter_confirm_code()
