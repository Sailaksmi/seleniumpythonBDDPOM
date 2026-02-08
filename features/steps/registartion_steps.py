from selenium import webdriver
from behave import given,when,then
from utils.browser_factory import get_browser
from pages.registration_page import RegistrationPage



@when('the user clicks on the "Register" link')
def step_click_Registerlink(context):
    context.registration_page.click_registerlink()

@when('the user selects gender as "{gender}"')
def step_select_gender(context,gender):
    context.registration_page.select_gender(gender.lower())

@when('the user enters first name "{firstName}"')
def step_enter_firstName(context,firstName):
    context.registration_page.enter_first_name(firstName)

@when('the user enters last name "{lastName}"')
def step_enter_lastName(context,lastName):
    context.registration_page.enter_last_name(lastName)

@when('the user enters email "{email}"')
def step_enter_email(context,email):
    context.registration_page.enter_email(email)

@when('the user enters password "{password}"')
def password(context,password):
    context.registration_page.enter_password(password)

@when('the user enters confirm password "{confirmPassword}"')
def confirmPassword(context,confirmPassword):
    context.registration_page.enter_confirmPassword(confirmPassword)

@when('the user clicks on the Register button')
def step_click_Registerbutton(context):
    context.registration_page.click_registerbutton()

@then('the user should see the registration success message')
def step_registration_text(context):
    registrationtext = context.registration_page.get_registration_text()
    # if(registrationtext == "Your registration completed"):
    #     print("registration is successful")
    # else:
    #     print("registration is not successful")
    assert "Your registration completed" in registrationtext