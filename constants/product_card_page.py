class ProductCardPageConst:
    # PRODUCT CARD
    PRODUCT_TITLE_XPATH = ".//h1"
    ADD_TO_CART_BUTTON_XPATH = ".//span[contains(text(),'Додати до кошику')]"
    PRODUCT_TITLE_IN_CART_XPATH = ".//a[@class='basket-product__name']"

    # CART
    CART_TITLE_TEXT = "Ви додали до кошик"
    CART_TITLE_XPATH = f".//span[contains(text(),'{CART_TITLE_TEXT}')]"
    CART_TOTAL_PRICE_XPATH = "//div[@class='basket-total__price']//span[@class='ms2_total_cost']"
    CART_POPUP_CLOSE_BUTTON_XPATH = ".//a[@class='close-modal']"
    CART_PRODUCT_PRICES_XPATH = ".//div[@class='basket-table__col-4']//span[@class='price-new']/span[1]"
