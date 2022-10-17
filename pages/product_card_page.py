import logging

from pages.base_page import BasePage
from pages.utils import wait_until_ok


class ProductCardPage(BasePage):
    log = logging.getLogger("[CardPage]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.product_card_page import ProductCardPageConst
        self.product_card_page_constants = ProductCardPageConst
        from constants.header import HeaderConst
        self.header_constants = HeaderConst
        from pages.catalog_flowers_page import CatalogFlowersPage
        self.catalog_flowers_page = CatalogFlowersPage(self.driver)

    def get_product_name(self):
        """Get the product title from product card"""
        product_card_title = self.get_element_text(xpath=self.product_card_page_constants.PRODUCT_TITLE_XPATH)
        return product_card_title

    @wait_until_ok(period=0.25)
    def add_product_to_cart(self):
        """Click cart button in the product card"""
        self.click(xpath=self.product_card_page_constants.ADD_TO_CART_BUTTON_XPATH)

    def verify_success_add_to_cart(self):
        """Verify the product was added to cart"""
        # The cart popup is opened
        assert self.get_element_text(
            self.product_card_page_constants.CART_TITLE_XPATH) == self.product_card_page_constants.CART_TITLE_TEXT
        # The product was added to cart
        assert self.get_element_text(
            self.product_card_page_constants.PRODUCT_TITLE_IN_CART_XPATH) == self.get_product_name(), \
            f"Actual message: {self.get_element_text(self.product_card_page_constants.PRODUCT_TITLE_IN_CART_XPATH)}"

    def delete_from_cart(self):
        """Click button to delete product from cart"""
        self.click(xpath=self.product_card_page_constants.DELETE_PRODUCT_FROM_CART_XPATH)
