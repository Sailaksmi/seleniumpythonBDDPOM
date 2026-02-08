from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class RegistrationPage(BasePage):

    register_link = (By.LINK_TEXT, "Register")
    gender_male = (By.ID,"gender-male")
    gender_female = (By.ID,"gender-female")
    first_name_input = (By.ID,"FirstName")
    last_name_input = (By.ID,"LastName")
    email_input = (By.ID,"Email")
    password_input = (By.ID,"Password")
    confirm_password_input = (By.ID,"ConfirmPassword")
    register_button = (By.ID,"register-button")
    registration_success_message = (By.CLASS_NAME,"result")

    def click_registerlink(self):
        self.click(self.register_link)

    def select_gender(self,gender):
        if gender == "female":
            self.click(self.gender_female)
        else:
            self.click(self.gender_male)

    def enter_first_name(self,firstName):
        self.clear_and_send_keys(self.first_name_input,firstName)

    def enter_last_name(self,lastName):
        self.clear_and_send_keys(self.last_name_input,lastName)

    def enter_email(self,email):
        self.clear_and_send_keys(self.email_input,email)

    def enter_password(self,password):
        self.clear_and_send_keys(self.password_input,password)

    def enter_confirmPassword(self,confirmPassword):
        self.clear_and_send_keys(self.confirm_password_input,confirmPassword)

    def click_registerbutton(self):
        self.click(self.register_button)

    def get_registration_text(self):
        return self.get_text(self.registration_success_message)
    

    # def register_user(self,gender,first_name,last_name,email,password,confirm_password):
    #     if gender=="female":
    #         self.click(self.gender_female)
    #     else:
    #         self.click(self.gender_male)
    #     self.clear_and_send_keys(self.first_name_input,first_name)
    #     self.clear_and_send_keys(self.last_name_input,last_name)
    #     self.clear_and_send_keys(self.email_input,email)
    #     self.clear_and_send_keys(self.password_input,password)
    #     self.clear_and_send_keys(self.confirm_password_input,confirm_password)
    #     self.click(self.register_button)
    #     return self.get_text(self.registration_success_message)