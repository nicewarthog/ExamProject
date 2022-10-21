import logging

from pages.utils import random_str


class TestHeader:
    log = logging.getLogger("[Header]")

    # SEARCH
    def test_incorrect_search(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Go to Search form
        - Fill search field with random value
        - Verify incorrect search message
        """

        # Input search value
        random_search_value = random_str(9)
        open_start_page.header.search(random_search_value)
        self.log.info(f"Search field got the value {random_search_value}")

        # Verify unsuccessful search
        open_start_page.header.verify_incorrect_search()
        self.log.info(f"Search is incorrect")

    def test_correct_search(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Go to Search form
        - Fill search field with correct value
        - Verify successful search
        """

        for basic_search_value in ("тюльпан", "коробка"):
            # Input search text
            open_start_page.header.search(basic_search_value)
            self.log.info(f"Search field has the value {basic_search_value}")

            # Navigate to search page
            search_page = open_start_page.header.navigate_to_search_page(basic_search_value)

            # Verify successful search
            search_page.verify_correct_search(basic_search_value)
            self.log.info(f"Search item has the value {basic_search_value}")
