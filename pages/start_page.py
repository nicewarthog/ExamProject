import logging

from pages.base_page import BasePage


class StartPage(BasePage):
    log = logging.getLogger("[StartPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.header import HeaderConst
        self.header_constants = HeaderConst
        from pages.header import Header
        self.header = Header(self.driver)
        from pages.product_card_page import ProductCardPage
        self.product_card_page = ProductCardPage(self.driver)

    # SIGN UP
    def sign_up(self, user):
        """Sign up as the user and verify that you are inside"""
        # Open Sign Up form
        self.click(xpath=self.header_constants.SIGN_UP_SIGN_IN_POPUP_XPATH)
        self.click(xpath=self.header_constants.SIGN_UP_FORM_XPATH)
        # Fill phone
        self.fill_field(xpath=self.header_constants.SIGN_UP_PHONE_FIELD_XPATH, value=user.phone)
        # Fill username
        self.fill_field(xpath=self.header_constants.SIGN_UP_LOGIN_FIELD_XPATH, value=user.login)
        # Fill password
        self.fill_field(xpath=self.header_constants.SIGN_UP_PASSWORD_FIELD_XPATH, value=user.password)
        # Click button
        self.click(xpath=self.header_constants.SIGN_UP_BUTTON_XPATH)

    def verify_success_sign_up(self, login):
        """Verify success Sign Up using Username in the header"""
        assert self.get_element_text(self.header_constants.ACCOUNT_USERNAME_XPATH.format(login_option=login)) == login, \
            f"Actual message: {self.get_element_text(self.header_constants.ACCOUNT_USERNAME_XPATH)}"

    # SIGN IN
    def sign_in(self, basic_user):
        """Sign in as the user"""
        # Open Sign In form
        self.click(xpath=self.header_constants.SIGN_UP_SIGN_IN_POPUP_XPATH)
        # Fill phone number
        self.fill_field(xpath=self.header_constants.SIGN_IN_PHONE_FIELD_XPATH, value=basic_user.phone)
        # Fill password
        self.fill_field(xpath=self.header_constants.SIGN_IN_PASSWORD_FIELD_XPATH, value=basic_user.password)
        # Click button
        self.click(xpath=self.header_constants.SIGN_IN_BUTTON_XPATH)

    def verify_empty_fields_sign_in(self):
        """Verify validation messages for empty fields in Sign In form"""
        assert self.get_element_text(
            self.header_constants.SIGN_IN_EMPTY_PHONE_MESSAGE_XPATH) == self.header_constants.SIGN_IN_EMPTY_PHONE_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.header_constants.SIGN_IN_EMPTY_PHONE_MESSAGE_XPATH)}"
        assert self.get_element_text(
            self.header_constants.SIGN_IN_EMPTY_PASSWORD_MESSAGE_XPATH) == self.header_constants.SIGN_IN_EMPTY_PASSWORD_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.header_constants.SIGN_IN_EMPTY_PASSWORD_MESSAGE_XPATH)}"

    def verify_incorrect_phone_sign_in(self):
        """Verify validation message for incorrect phone data in Sign In form"""
        assert self.get_element_text(
            self.header_constants.SIGN_IN_INCORRECT_PHONE_MESSAGE_XPATH) == self.header_constants.SIGN_IN_INCORRECT_PHONE_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.header_constants.SIGN_IN_INCORRECT_PHONE_MESSAGE_XPATH)}"

    def verify_incorrect_password_sign_in(self):
        """Verify validation message for incorrect password data in Sign In form"""
        assert self.get_element_text(
            self.header_constants.SIGN_IN_INCORRECT_PASSWORD_MESSAGE_XPATH) == self.header_constants.SIGN_IN_INCORRECT_PASSWORD_MESSAGE_TEXT, \
            f"Actual message: {self.get_element_text(self.header_constants.SIGN_IN_INCORRECT_PASSWORD_MESSAGE_XPATH)}"

    def verify_success_sign_in(self, login):
        """Verify correct Sign In"""
        assert self.get_element_text(self.header_constants.ACCOUNT_USERNAME_XPATH.format(login_option=login)) == login, \
            f"Actual message: {self.get_element_text(self.header_constants.ACCOUNT_USERNAME_XPATH)}"

    def verify_success_sign_out(self):
        """Verify success Sign Out"""
        assert self.get_element_text(
            self.header_constants.SIGN_UP_SIGN_IN_POPUP_XPATH) == self.header_constants.SIGN_UP_SIGN_IN_POPUP_TEXT, \
            f"Actual message: {self.get_element_text(self.header_constants.SIGN_UP_SIGN_IN_POPUP_XPATH)}"
