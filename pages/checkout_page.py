from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class CheckoutPage(BasePage):

    TERMS_CHECKBOX = (By.ID, "termsofservice")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    COMPANY = (By.ID, "BillingNewAddress_Company")
    COUNTRY = (By.ID, "BillingNewAddress_CountryId")
    STATE = (By.ID, "BillingNewAddress_StateProvinceId")
    CITY = (By.ID, "BillingNewAddress_City")
    ADDRESS1 = (By.ID, "BillingNewAddress_Address1")
    ADDRESS2 = (By.ID, "BillingNewAddress_Address2")
    ZIPCODE = (By.ID, "BillingNewAddress_ZipPostalCode")
    PHONE = (By.ID, "BillingNewAddress_PhoneNumber")
    FAX = (By.ID, "BillingNewAddress_FaxNumber")

    BILLING_CONTINUE = (By.XPATH, "//input[@onclick='Billing.save()']")
    LOGOUT_LINK = (By.LINK_TEXT, "Log out")

    def accept_terms(self):
        self.click(self.TERMS_CHECKBOX)

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def fill_billing_details(
        self, company, country, state, city,
        address1, address2, zipcode, phone, fax
    ):
        self.clear_and_send_keys(self.COMPANY, company)

        Select(self.wait.until(lambda d: d.find_element(*self.COUNTRY))) \
            .select_by_visible_text(country)

        Select(self.wait.until(lambda d: d.find_element(*self.STATE))) \
            .select_by_visible_text(state)

        self.clear_and_send_keys(self.CITY, city)
        self.clear_and_send_keys(self.ADDRESS1, address1)
        self.clear_and_send_keys(self.ADDRESS2, address2)
        self.clear_and_send_keys(self.ZIPCODE, zipcode)
        self.clear_and_send_keys(self.PHONE, phone)
        self.clear_and_send_keys(self.FAX, fax)

    def click_billing_continue(self):
        self.click(self.BILLING_CONTINUE)

    def is_logout_visible(self):
        return self.is_element_visible(self.LOGOUT_LINK)
