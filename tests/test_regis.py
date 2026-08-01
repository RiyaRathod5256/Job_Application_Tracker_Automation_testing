from playwright.sync_api import expect
from pages.registerpage import RegisterPage


def test_register_page_loads(page):
    register=RegisterPage(page)

    register.open()
    expect(page).to_have_url(RegisterPage.URL)

def test_register_page_logo_visible(page):
    register=RegisterPage(page)

    register.open()
    expect(register.logo).to_be_visible()

def test_register_page_form_group(page):
    register = RegisterPage(page)
    register.open()
    
    expect(register.form).to_be_visible()

def test_register_page__username_invalid_length(page):
    register = RegisterPage(page)
    register.open()
    register.fill_form("gsfvhffufhydg"*25,"riya@gmail.com","9894857543","Riya@123","Riya@123")
    register.click_register()
    error=page.locator("#usernameError")

    expect(error).to_be_visible()





