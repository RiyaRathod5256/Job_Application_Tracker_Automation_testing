class RegisterPage:

    URL="http://127.0.0.1:8000/register"

    def __init__(self,page):
        self.page=page
        self.username=page.locator("#username")
        self.email=page.locator("#useremail")
        self.phonenumber=page.locator("#userphonenumber")
        self.userpassword=page.locator("#userpassword")
        self.confirmpassword=page.locator("#confirmpassword")
        self.register_button = page.locator("#registerBtn")
        self.logo=page.locator(".logo")
        self.form=page.locator(".form-group")

    def open(self):
          self.page.goto(self.URL)

    def fill_form(self,username,email,phonenumber,userpassword,confirmpassword):
                self.username.fill(username)
                self.email.fill(email)
                self.phonenumber.fill(phonenumber)
                self.userpassword.fill(userpassword)
                self.confirmpassword.fill(confirmpassword)

    def click_register(self):
           self.register_button.click()

    
    



    


    
        