from playwright.sync_api import expect

def test_register_page_loads(page):
    page.goto("http://127.0.0.1:8000/register")
    expect(page).to_have_url("http://127.0.0.1:8000/register")

def test_register_page_logo_visible(page):
    page.goto("http://127.0.0.1:8000/register")
    logo=page.locator(".logo")
    expect(logo).to_be_visible()

def test_register_page_form_group(page):
    page.goto("http://127.0.0.1:8000/register")
    form=page.locator(".form-group")
    expect(form).to_be_visible()

def test_register_page_form_group(page):
    page.goto("http://127.0.0.1:8000/register")
    form=page.locator(".form-group")
    expect(form).to_be_visible()

def test_register_page_username_visible(page):
    page.goto("http://127.0.0.1:8000/register")
    username=page.locator("#username")

    expect(username).to_be_visible()

def test_register_page_email_visible(page):
    page.goto("http://127.0.0.1:8000/register")
    useremail=page.locator("#useremail")

    expect(useremail).to_be_visible()

def test_register_page_phonenumber_visible(page):
    page.goto("http://127.0.0.1:8000/register")
    userphonenumber=page.locator("#userphonenumber")
    
    expect(userphonenumber).to_be_visible()

def test_register_page_password_visible(page):
    page.goto("http://127.0.0.1:8000/register")
    userpassword=page.locator("#userpassword")
    
    expect(userpassword).to_be_visible()

def test_register_page_confirmpassword_visible(page):
    page.goto("http://127.0.0.1:8000/register")
    confirmpassword=page.locator("#confirmpassword")
    
    expect(confirmpassword).to_be_visible()


def test_register_page_valid_userdata(page):
    page.goto("http://127.0.0.1:8000/register")
    page.fill("#username","kalita") 
    page.fill("#useremail","kalita@gmail.com")
    page.fill("#userphonenumber","9938366355")
    page.fill("#userpassword","Riya@123")
    page.fill("#confirmpassword","Riya@123")

    page.click("#registerBtn")

    expect(page).to_have_url("http://127.0.0.1:8000/login")


def test_register_page__username_invalid_length(page):
    page.goto("http://127.0.0.1:8000/register")
    page.fill("#username","riyaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaoooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo") 
    page.fill("#useremail","rathod@gmail.com")
    page.fill("#userphonenumber","9933822898")
    page.fill("#userpassword","Riya@123")
    page.fill("#confirmpassword","Riya@123")

    page.locator("#registerBtn").click()

    error=page.locator("#usernameError")

    expect(error).to_be_visible()

def test_register_page_invalid_useremail(page):
    page.goto("http://127.0.0.1:8000/register")
    page.fill("#username","kashi") 
    page.fill("#useremail","kashigmail.com")
    page.fill("#userphonenumber","9933114898")
    page.fill("#userpassword","Riya@123")
    page.fill("#confirmpassword","Riya@123")

    page.locator("#registerBtn").click()

    error=page.locator("#emailError")


    expect(error).to_be_visible()


def test_register_page_invalid_userphonenumber(page):
    page.goto("http://127.0.0.1:8000/register")
    page.fill("#username","kashi") 
    page.fill("#useremail","kashipi@gmail.com")
    page.fill("#userphonenumber","33114898")
    page.fill("#userpassword","Riya@123")
    page.fill("#confirmpassword","Riya@123")

    page.locator("#registerBtn").click()

    error=page.locator("#phoneError")
    expect(error).to_be_visible()

def test_register_page_invalid_password(page):
    page.goto("http://127.0.0.1:8000/register")
    page.fill("#username","kashi") 
    page.fill("#useremail","kashipi@gmail.com")
    page.fill("#userphonenumber","9988556611")
    page.fill("#userpassword","riya@123")
    page.fill("#confirmpassword","riya@123")

    page.locator("#registerBtn").click()

    error=page.locator("#passwordError")

    expect(error).to_be_visible()













