from playwright.sync_api import expect

def test_register_page_loads(page):
    page.goto("http://127.0.0.1:8000/register")
    expect(page).to_have_url("http://127.0.0.1:8000/register")

def test_register_page_logo_visible(page):
    page.goto("http://127.0.0.1:8000/register")
    logo=page.locator(".logo")
    expect(logo).to_be_visible

def test_register_page_form_group(page):
    page.goto("http://127.0.0.1:8000/register")
    form=page.locator(".form-group")
    expect(form).to_be_visible
