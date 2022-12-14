import logging

from pages.base_page import BasePage
from pages.utils import wait_until_ok


class CatalogFlowersPage(BasePage):
    log = logging.getLogger("[Flowers Page]")

    def __init__(self, driver):
        super().__init__(driver)
        from constants.catalog_flowers_page import CatalogFlowersPageConst
        self.catalog_flowers_constants = CatalogFlowersPageConst

    @wait_until_ok(period=0.25)
    def navigate_to_product_card_1(self):
        """Navigate to product card 1"""
        self.click(xpath=self.catalog_flowers_constants.PRODUCT_CARD_1_XPATH)
        from pages.product_card_page import ProductCardPage
        return ProductCardPage(self.driver)

    @wait_until_ok(period=0.25)
    def navigate_to_product_card_2(self):
        """Navigate to product card 2"""
        self.click(xpath=self.catalog_flowers_constants.PRODUCT_CARD_2_XPATH)
        from pages.product_card_page import ProductCardPage
        return ProductCardPage(self.driver)
