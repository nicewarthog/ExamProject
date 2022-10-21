import logging

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchPage(BasePage):
    log = logging.getLogger("[SearchPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.search_page import SearchPageConst
        self.search_page_constants = SearchPageConst

    def verify_correct_search(self, basic_search_word):
        """Verify the search is correct"""
        search_list = self.driver.find_elements(by=By.XPATH, value=self.search_page_constants.SEARCH_ITEMS_LIST_XPATH)
        for item in search_list:
            assert basic_search_word in item.text.lower(), f"Actual message: {item.text.lower()}"
