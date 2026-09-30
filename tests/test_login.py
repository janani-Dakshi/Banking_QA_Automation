from pages.login_page import LoginPage

def test_valid_login(browser):
    login_page = LoginPage(browser)
    browser.get("https://parabank.parasoft.com/parabank/index.htm")
    login_page.enter_username("jack_d")
    login_page.enter_password("aq9012")
    login_page.click_login()