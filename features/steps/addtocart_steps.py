from behave import given,when,then
from pages.addtocart_page import AddtoCartPage



@when('user navigates to the "{category}" category')
def step_select_category(context,category):
    context.addtocart_page = AddtoCartPage(context.driver)
    context.addtocart_page.select_category(category)

@when('user sorts the books by "{sortOrder}"')
def step_select_sortorder(context,sortOrder):
    context.addtocart_page.select_sortorder(sortOrder)

@when('user selects the book "{bookName}"')
def step_select_bookName(context,bookName):
    context.addtocart_page.select_bookName(bookName)

@when('user clicks on Add to Cart button')
def step_click_Addtocart_button(context):
    context.addtocart_page.click_addtocart_button()
    

@then('the book "{bookName}" should be added to the shopping cart')
def step_bookName_addedtocart(context,bookName):
    context.addtocart_page.click_Shoppingcart_link()
    productName = context.addtocart_page.get_productname()
    assert bookName in productName

@then('shopping cart count should be updated')
def step_cartcount_increased(context):
    cartcount = context.addtocart_page.get_cartquantity()
    assert cartcount > 0, f"Expected cart count > 0 but got {cartcount}"
