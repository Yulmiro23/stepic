from pages.main_page import MainPage


def test_guest_can_go_to_login_page(driver):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(driver, link)
    main_page.open()
    main_page.go_to_login_page()
