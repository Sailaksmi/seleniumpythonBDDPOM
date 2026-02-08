from behave import given,when,then
from pages.login_page import LoginPage


@given('user navigates to Login page')
def step_loginlink(context):
    context.login_page.click_loginlink()

@when('user enters email "{email}"')
def step_enter_loginemailid(context,email):
    context.login_page.enter_login_emailid(email)

@when('user enters password "{password}"')
def step_enter_loginpassword(context,password):
    context.login_page.enter_login_password(password)

@when('user clicks on Login button')
def step_click_loginbutton(context):
    context.login_page.click_loginbutton()

@then('the user should be logged in successfully')
def step_verify_loginsuccesstext(context):    
    loginmsgtext= context.login_page.get_login_successtext()
    assert "Welcome to the new Tricentis store!" in loginmsgtext