import logging

import pytest


class TestCardPage:
    log = logging.getLogger("[CardPage]")

    @pytest.fixture(scope="function")
    def open_catalog_flowers_page(self, open_start_page, basic_user):
        # Open catalog page
        catalog_flowers_page = open_start_page.header.navigate_to_catalog_flowers()
        self.log.info("Profile is opened")
        return catalog_flowers_page

        # Delete product from cart
        # open_start_page.product_card_page.delete_from_cart()
        # self.log.info("The product was deleted from cart")

    @pytest.fixture(scope="function")
    def open_product_card(self, open_catalog_flowers_page):
        # Open catalog page
        product_card_page = open_catalog_flowers_page.navigate_to_product_card_1()
        self.log.info("Profile is opened")
        return product_card_page

    def test_add_product_to_cart_from_card(self, open_catalog_flowers_page):
        """
        Preconditions:
        - Create driver, open Start page
        - Log In as basic user
        - Open Catalog page
        Steps:
        - Open Card page
        - Click Add to Cart button
        - Verify the product was added to cart
        - Delete product from cart
        """

        # Click Product Card button
        open_product_card = open_catalog_flowers_page.navigate_to_product_card_1()
        self.log.info("Product card is opened")

        # Add product to cart
        open_product_card.add_product_to_cart()
        self.log.info("Product is added to cart")

        # Verify the product is added to cart
        open_product_card.verify_success_add_to_cart()
        self.log.info("The product card was verify")

        # Delete the product from cart
        open_product_card.delete_from_cart()
        self.log.info("The product was deleted from cart")

    def test_total_price_of_order(self, open_product_card):
        """
        Preconditions:
        - Create driver, open Start page
        - Log In as basic user
        - Open Catalog page
        Steps:
        - Add product to cart
        - In the cart add one more product via product counter
        - Verify that prices sum of all products equals the total amount of the order
        Postconditions:
        - Delete product from cart
        """

        # Add product 1 to cart
        open_product_card.add_product_to_cart()
        self.log.info("Product is added to cart")

        # Verify total price with 1 product
        open_product_card.verify_total_price_with_one_product()
        self.log.info("One product price = total order price")

        # Close cart and add to cart one more product
        open_product_card.close_cart()
        open_catalog_flowers = open_product_card.header.navigate_to_catalog_flowers()
        open_catalog_flowers.navigate_to_product_card_2()
        open_product_card.add_product_to_cart()

        # Verify total price with 1 product
        open_product_card.verify_total_price_with_two_products()
        self.log.info("One product price = total order price")
