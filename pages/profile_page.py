import logging

from pages.base_page import BasePage


class ProfilePage(BasePage):
    log = logging.getLogger("[ProfilePage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.profile_page import ProfilePageConst
        self.profile_page_constants = ProfilePageConst
        from constants.header import HeaderConst
        self.header_constants = HeaderConst
        from pages.header import Header
        self.header = Header(self.driver)

    def sign_out(self):
        """Log out from account"""
        self.click(xpath=self.profile_page_constants.SIGN_OUT_BUTTON_XPATH)
        from pages.start_page import StartPage
        return StartPage(self.driver)
