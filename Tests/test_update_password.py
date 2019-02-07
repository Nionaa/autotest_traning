def test_enter_profile_page(app_fixture):
    app_fixture.open_page()
    app_fixture.authorization.auth_steps()
    app_fixture.navigation.main_lk()
    app_fixture.navigation.profile_navigation()
    app_fixture.update_pass.pass_update_popup()
    app_fixture.update_pass.pass_frame_switch()
    app_fixture.update_pass.current_pass_key()
    app_fixture.update_pass.new_pass_key()
    app_fixture.update_pass.confirm_pass_key()
    app_fixture.update_pass.press_save_button()