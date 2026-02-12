from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):

    login_link = (By.CSS_SELECTOR, "a[href='/login']")
    login_email= (By.ID,"Email")
    login_password = (By.ID, "Password")
    login_button = (By.CSS_SELECTOR, "input[value='Log in']")
    login_success_message = (By.CLASS_NAME, "topic-html-content-body")
    login_unsuccess_message = (By.CLASS_NAME, "validation-summary-errors")


    def click_loginlink(self):
        self.click(self.login_link)
    
    def enter_login_emailid(self,email):
        self.clear_and_send_keys(self.login_email,email)

    def enter_login_password(self,password):
        self.clear_and_send_keys(self.login_password,password)

    def click_loginbutton(self):
        self.click(self.login_button)

    def get_login_successtext(self):
        self.scroll_into_view(self.login_success_message)
        return self.get_text(self.login_success_message)
    
    def get_login_unsuccesstext(self):
     return self.driver.page_source




