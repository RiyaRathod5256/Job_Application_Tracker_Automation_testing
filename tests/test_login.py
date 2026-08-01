from playwright.sync_api import expect
import pytest

login_url="http://127.0.0.1:8000/login"

def fill_login_form(page,username,password):
    page.fill("#username",username)
    page.fill("#userpassword",password)

def test_login_page_loads(login_page):
    expect(login_page).to_have_url(login_url)

def test_login_page_username(login_page):

    username=login_page.locator("#username")
    expect(username).to_be_visible()

def test_login_page_username(login_page):

    password=login_page.locator("#userpassword")
    expect(password).to_be_visible()
    
def test_login_page_valid_credentials(login_page):
    fill_login_form(login_page,"Admin","admin123")

    login_page.click("#loginBtn")

    msg=login_page.locator("#serverMessage")

    print(msg)

    expect(login_page).to_have_url("http://127.0.0.1:8000/admin")


    




