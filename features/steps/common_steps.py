from behave import given
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from pages.addtocart_page import AddtoCartPage
from pages.checkout_page import CheckoutPage


@given('the user is on the Demo Web Shop home page')
def step_open_url(context):
    context.login_page = LoginPage(context.driver)
    context.registration_page = RegistrationPage(context.driver)


@given(
    'user naviagtes to checkoutpage with "{email}", "{password}", '
    'and select "{category}", "{sortOrder}", "{bookName}"'
)
def step_navigate_to_checkoutpage(
    context, email, password, category, sortOrder, bookName
):
    context.login_page = LoginPage(context.driver)
    context.addtocart_page = AddtoCartPage(context.driver)

    # Login
    context.login_page.click_loginlink()
    context.login_page.enter_login_emailid(email)
    context.login_page.enter_login_password(password)
    context.login_page.click_loginbutton()

    # ✅ wait for category menu after login (VERY IMPORTANT)
    context.login_page.wait.until(
        EC.presence_of_element_located((By.LINK_TEXT, category))
    )

    # Add to cart
    context.addtocart_page.select_category(category)
    context.addtocart_page.select_sortorder(sortOrder)
    context.addtocart_page.select_bookName(bookName)
    context.addtocart_page.click_addtocart_button()
    context.addtocart_page.click_Shoppingcart_link()

    product_name = context.addtocart_page.get_productname()
    assert bookName in product_name

    cart_count = context.addtocart_page.get_cartquantity()
    assert cart_count > 0, f"Expected cart count > 0 but got {cart_count}"

    context.checkout_page = CheckoutPage(context.driver)
