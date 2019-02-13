def test_enter_profile_page(app_fixture):
    app_fixture.open_page()
    app_fixture.authorization.auth_steps()
    app_fixture.navigation.main_lk()
    app_fixture.navigation.profile_navigation()
    app_fixture.update_pass.pass_update()
    app_fixture.update_pass.rerurn_password()
