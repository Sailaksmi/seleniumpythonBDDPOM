from behave import given, when, then

from pages.checkout_page import CheckoutPage


@when('user should accept terms and conditions')
def step_accept_terms(context):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.accept_terms()


@when('user proceeds to checkout')
def step_click_checkout(context):
    context.checkout_page.click_checkout()


@when(
    'user fills all billing details and proceed to checkout '
    '"{company}", "{country}", "{state}", "{city}", "{address1}", '
    '"{address2}", "{zipCode}", "{phone}", "{fax}"'
)
def step_fill_billing(
    context, company, country, state, city,
    address1, address2, zipCode, phone, fax
):
    context.checkout_page.fill_billing_details(
        company, country, state, city,
        address1, address2, zipCode, phone, fax
    )
    context.checkout_page.click_billing_continue()


@then('the user should see the "Log out" link')
def step_verify_logout(context):
    assert context.checkout_page.is_logout_visible()
