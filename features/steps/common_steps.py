from behave import given,when
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.addtocart_page import AddtoCartPage
from pages.checkout_page import CheckoutPage


@given('the user is on the Demo Web Shop home page')
def step_open_url(context):
    context.login_page = LoginPage(context.driver)
    context.registration_page = RegistrationPage(context.driver)
    context.addtocart_page = AddtoCartPage(context.driver)


@when('the user registers with valid details')
def step_register_valid(context):
    context.email = f"user_{int(time.time())}@test.com"

    context.registration_page.click_registerlink()
    context.registration_page.select_gender("female")
    context.registration_page.enter_first_name("Test")
    context.registration_page.enter_last_name("User")
    context.registration_page.enter_email(context.email)
    context.registration_page.enter_password("Test@123")
    context.registration_page.enter_confirmPassword("Test@123")
    context.registration_page.click_registerbutton()
    context.registration_page.click_logout()

    context.registration_page = RegistrationPage(context.driver)
    context.addtocart_page = AddtoCartPage(context.driver)

    

@when('the user tries to register again with the same email')
def step_register_again(context):
    context.registration_page.click_registerlink()
    context.registration_page.select_gender("female")
    context.registration_page.enter_first_name("Test")
    context.registration_page.enter_last_name("User")
    context.registration_page.enter_email(context.email)  # SAME EMAIL
    context.registration_page.enter_password("Test@123")
    context.registration_page.enter_confirmPassword("Test@123")
    context.registration_page.click_registerbutton()

    context.registration_page = RegistrationPage(context.driver)



@when('the user logs in with the same registered details')
def step_login_with_same_user(context):
    context.login_page.click_loginlink()
    context.login_page.enter_login_emailid(context.email)
    context.login_page.enter_login_password("Test@123")
    context.login_page.click_loginbutton()
    
    context.addtocart_page = AddtoCartPage(context.driver)




# @given(
#     'user naviagtes to checkoutpage with "{email}", "{password}", '
#     'and select "{category}", "{sortOrder}", "{bookName}"'
# )
# def step_navigate_to_checkoutpage(
#     context, email, password, category, sortOrder, bookName
# ):
#     context.login_page = LoginPage(context.driver)
#     context.addtocart_page = AddtoCartPage(context.driver)

#     # Login
#     context.login_page.click_loginlink()
#     context.login_page.enter_login_emailid(email)
#     context.login_page.enter_login_password(password)
#     context.login_page.click_loginbutton()

#     # ✅ wait for category menu after login (VERY IMPORTANT)
#     context.login_page.wait.until(
#         EC.presence_of_element_located((By.LINK_TEXT, category))
#     )

#     # Add to cart
#     context.addtocart_page.select_category(category)
#     context.addtocart_page.select_sortorder(sortOrder)
#     context.addtocart_page.select_bookName(bookName)
#     context.addtocart_page.click_addtocart_button()
#     context.addtocart_page.click_Shoppingcart_link()

#     product_name = context.addtocart_page.get_productname()
#     assert bookName in product_name

#     cart_count = context.addtocart_page.get_cartquantity()
#     assert cart_count > 0, f"Expected cart count > 0 but got {cart_count}"

#     context.checkout_page = CheckoutPage(context.driver)


@given('a new user is registered successfully')
def step_register_new_user(context):
    import time
    unique_email = f"user_{int(time.time())}@test.com"
    context.email = unique_email

    context.registration_page.click_registerlink()
    context.registration_page.select_gender("female")
    context.registration_page.enter_first_name("Test")
    context.registration_page.enter_last_name("User")
    context.registration_page.enter_email(unique_email)
    context.registration_page.enter_password("Test@123")
    context.registration_page.enter_confirmPassword("Test@123")
    context.registration_page.click_registerbutton()

    context.checkout_page = CheckoutPage(context.driver)


@when('the user selects "{category}", sorts by "{sortOrder}", and chooses "{bookName}"')
def step_select_category_sort_book(context, category, sortOrder, bookName):
    context.addtocart_page = AddtoCartPage(context.driver)

    context.addtocart_page.select_category(category)
    context.addtocart_page.select_sortorder(sortOrder)
    context.addtocart_page.select_bookName(bookName)
    context.addtocart_page.click_addtocart_button()
    context.addtocart_page.click_Shoppingcart_link()
 



