from playwright.sync_api import expect

def test_home_page_load(page):
    
        page.goto("http://127.0.0.1:8000")
        expect(page).to_have_url("http://127.0.0.1:8000/")


def test_home_page_title(page):
        page.goto("http://127.0.0.1:8000")
        expect(page).to_have_title("Job Portal")

def test_register_button_visible(page):
        page.goto("http://127.0.0.1:8000")
        expect(page.locator(".register-btn")).to_be_visible()

def test_register_button_visible(page):
        page.goto("http://127.0.0.1:8000")
        expect(page.locator(".login-btn")).to_be_visible()


def test_register_button_enabled(page):
        page.goto("http://127.0.0.1:8000")
        expect(page.locator(".register-btn")).to_be_enabled()

def test_login_button_enabled(page):
        page.goto("http://127.0.0.1:8000")
        expect(page.locator(".login-btn")).to_be_enabled()

def test_home_button_enabled(page):
        page.goto("http://127.0.0.1:8000")
        expect(page.locator(".register-btn")).to_be_enabled()

def test_register_navigation(page):
         page.goto("http://127.0.0.1:8000")
         register_btn=page.locator(".register-btn")

         register_btn.click()

         expect(page).to_have_url("http://127.0.0.1:8000/register")

def test_register_navigation(page):
         
         page.goto("http://127.0.0.1:8000")
         login_btn=page.locator(".login-btn")
         login_btn.click()
         expect(page).to_have_url("http://127.0.0.1:8000/login")






        



