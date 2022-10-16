import logging

from pages.base_page import BasePage
from pages.utils import wait_until_ok


class Header(BasePage):
    log = logging.getLogger("[Header]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.header import HeaderConst
        self.header_constants = HeaderConst

    @wait_until_ok(period=0.25)
    def navigate_to_profile(self):
        """Click on username button"""
        # sleep(3)
        self.click(xpath=self.header_constants.PROFILE_BUTTON_XPATH)
        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver)
