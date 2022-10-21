import logging


class TestCardPage:
    log = logging.getLogger("[CatalogFlowersPage]")

    # def test_general_price_of_order(self, open_catalog_flowers_page):
    #     """
    #     Preconditions:
    #     - Create driver, open Start page
    #     - Log In as basic user
    #     - Open Catalog page
    #     Steps:
    #     - Add 3 items to cart
    #     - Verify that prices sum of all items equals the total amount of the order
    #     Postconditions:
    #     - Delete product from cart
    #     """
    #
    #     # Add products to cart
    #     open_catalog_flowers_page.add_products_to_cart()
    #     self.log.info("Products are added to cart")
    #
    #     # Verify the product 1 is added to cart
    #     # open_product_card.verify_success_add_to_cart()
    #     # self.log.info("The product card was verify")
