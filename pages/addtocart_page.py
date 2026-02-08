from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AddtoCartPage(BasePage):

    SORT_DROPDOWN = (By.ID, "products-orderby")
    ADD_TO_CART_BUTTON = (By.XPATH, "//input[@value='Add to cart']")
    SHOPPING_CART_LINK = (By.LINK_TEXT, "Shopping cart")
    PRODUCT_NAME = (By.CLASS_NAME, "product-name")
    CART_QTY = (By.CLASS_NAME, "cart-qty")

    def category_link(self, category_name):
        return (By.LINK_TEXT, category_name)

    def book_link(self, book_name):
        return (By.LINK_TEXT, book_name)

    def select_category(self, category):
        self.wait.until(EC.element_to_be_clickable(self.category_link(category))).click()

    def select_sortorder(self, sort_order):
        dropdown = self.wait.until(EC.visibility_of_element_located(self.SORT_DROPDOWN))
        Select(dropdown).select_by_visible_text(sort_order)

    def select_bookName(self, book_name):
        self.wait.until(EC.element_to_be_clickable(self.book_link(book_name))).click()

    def click_addtocart_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)).click()

    def click_Shoppingcart_link(self):
        self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART_LINK)).click()

    def get_productname(self):
        return self.get_text(self.PRODUCT_NAME)

    def get_cartquantity(self):
        qty_text = self.get_text(self.CART_QTY)
        return int(qty_text.strip("()"))
