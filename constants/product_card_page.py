class ProductCardPageConst:
    PRODUCT_TITLE_XPATH = ".//h1"
    ADD_TO_CART_BUTTON_XPATH = ".//span[contains(text(),'Додати до кошику')]"
    PRODUCT_TITLE_IN_CART_XPATH = ".//a[@class='basket-product__name']"
    CART_TITLE_TEXT = "Ви додали до кошик"
    CART_TITLE_XPATH = f".//span[contains(text(),'{CART_TITLE_TEXT}')]"
    DELETE_PRODUCT_FROM_CART_XPATH = ".//button[@class='basket-order__remove btn']"
