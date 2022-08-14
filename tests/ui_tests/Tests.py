from LoginPages import LoginHelper


def test_valid_login(browser):
    main_page = LoginHelper(browser)
    main_page.go_to_site()
    main_page.enter_login('standard_user')
    main_page.enter_password('secret_sauce')
    main_page.enter_button()



# assert "Картинки" and "Видео" in elements