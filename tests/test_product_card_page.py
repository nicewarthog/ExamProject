import logging

import pytest


class TestCardPage:
    log = logging.getLogger("[ProfilePage]")

    @pytest.fixture(scope="function")
    def open_catalog_flowers_page(self, open_start_page, basic_user):
        """Open Profile page"""
        catalog_flowers_page = open_start_page.header.navigate_to_catalog_flowers()
        self.log.info("Profile is opened")
        return catalog_flowers_page

    # @pytest.fixture(scope="function")
    # def delete_product_from_cart(self, open_catalog_flowers_page):
    #     """Open Profile page"""
    #     yield TestCardPage.test_add_product_to_cart()
    #     open_catalog_flowers_page.navigate_to_product_card.delete_from_cart()

    def test_add_product_to_cart(self, open_catalog_flowers_page):
        """
        Fixture:
        - Create driver, open Start page ++
        - Log In as basic user ++
        - Open Catalog page ++
        Steps:
        - Open Card page
        - Click Add to Cart button
        - Verify the product was added to cart
        """

        # Click Product Card button
        open_product_card = open_catalog_flowers_page.navigate_to_product_card()
        self.log.info("Product card is opened")

        # Click Cart button
        open_product_card.add_product_to_cart()
        self.log.info("Product is added to cart")

        # Verify the product was added to cart
        open_product_card.verify_success_add_to_cart()
        self.log.info("The product card was verify")

        # Delete the product from cart
        open_product_card.delete_from_cart()
        self.log.info("The product was deleted from cart")
