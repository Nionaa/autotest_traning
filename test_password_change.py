import password_change

def test_password_change_pass():
    password_change.open_page()
    password_change.enter_page()
    password_change.login_field()
    password_change.password_field()
    password_change.enter_button()
    password_change.open_personalcab_main_page()
    password_change.open_details_page()
    password_change.pass_change_button()

