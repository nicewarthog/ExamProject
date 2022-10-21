class ProductCardPageConst:
    # PRODUCT CARD
    PRODUCT_TITLE_XPATH = ".//h1"
    ADD_TO_CART_BUTTON_XPATH = ".//span[contains(text(),'Додати до кошику')]"
    PRODUCT_TITLE_IN_CART_XPATH = ".//a[@class='basket-product__name']"

    # CART
    CART_TITLE_TEXT = "Ви додали до кошик"
    CART_TITLE_XPATH = f".//span[contains(text(),'{CART_TITLE_TEXT}')]"
    DELETE_PRODUCT_FROM_CART_XPATH = ".//button[@class='basket-order__remove btn']"
    CART_PRODUCT_1_PRICE_XPATH = "//div[@id='a82d593e40d3b6c183b9f77eff88433e']//div[@class='basket-table__col-4']//span[@class='price-new']/span[1]"
    CART_PRODUCT_2_PRICE_XPATH = "//div[@id='25d58913825c1695c5ab8298c2c28c27']//div[@class='basket-table__col-4']//span[@class='price-new']/span[1]"
    CART_TOTAL_PRICE_XPATH = "//div[@class='basket-total__price']//span[@class='ms2_total_cost']"
    CART_POPUP_CLOSE_BUTTON_XPATH = ".//a[@class='close-modal']"
