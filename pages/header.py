import logging

from pages.base_page import BasePage
from pages.utils import wait_until_ok


class Header(BasePage):
    log = logging.getLogger("[Header]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.header import HeaderConst
        self.header_constants = HeaderConst
        from pages.search_page import SearchPage
        self.search_page = SearchPage(self.driver)

    @wait_until_ok(period=0.25)
    def navigate_to_profile(self):
        """Click username on header"""
        self.click(xpath=self.header_constants.PROFILE_BUTTON_XPATH)
        from pages.profile_page import ProfilePage
        return ProfilePage(self.driver)

    @wait_until_ok(period=0.25)
    def navigate_to_catalog_flowers(self):
        """Click flowers button on catalog menu"""
        self.click(xpath=self.header_constants.CATALOG_FLOWERS_BUTTON_XPATH)
        from pages.catalog_flowers_page import CatalogFlowersPage
        return CatalogFlowersPage(self.driver)

    @wait_until_ok(period=0.25)
    def search(self, search_value):
        """Fill search field"""
        self.click(xpath=self.header_constants.SEARCH_BUTTON_XPATH)
        self.fill_field(xpath=self.header_constants.SEARCH_FIELD_XPATH, value=search_value)

    @wait_until_ok(period=0.25)
    def verify_incorrect_search(self):
        """Verify the search is incorrect"""
        assert self.get_element_text(self.header_constants.SEARCH_INCORRECT_XPATH) == self.header_constants.SEARCH_INCORRECT_TEXT, \
            f"Actual message: {self.get_element_text(self.header_constants.SEARCH_INCORRECT_XPATH)}"

    @wait_until_ok(period=0.25)
    def navigate_to_search_page(self, search_value):
        self.click(xpath=self.header_constants.SEARCH_LIST_BUTTON_XPATH.format(search_option=search_value))
        from pages.search_page import SearchPage
        return SearchPage(self.driver)
