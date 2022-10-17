class HeaderConst:
    # Sign Up/Sign In
    SIGN_UP_SIGN_IN_POPUP_TEXT = "Особистий кабінет"
    SIGN_UP_SIGN_IN_POPUP_XPATH = ".//a[@class='personal__link link_black js-login']/span[@class='personal__text']"

    # Sign Up
    SIGN_UP_FORM_XPATH = ".//span[contains(text(),'Зареєструватися')]"
    SIGN_UP_PHONE_FIELD_XPATH = ".//div[@class='auth__form-inner']//input[@class='tel input input-tel']"
    SIGN_UP_LOGIN_FIELD_XPATH = ".//input[@name='fullname']"
    SIGN_UP_PASSWORD_FIELD_XPATH = ".//div[@class='auth__form-inner']//input[@class='input input-pass']"
    SIGN_UP_BUTTON_XPATH = ".//button[contains(text(),'Зареєструватися')]"

    # Sign In
    SIGN_IN_PHONE_FIELD_XPATH = ".//div[@class='login__form-inner']//input[@class='tel input input-tel']"
    SIGN_IN_PASSWORD_FIELD_XPATH = ".//div[@class='login__form-inner']//input[@class='input input-pass']"
    SIGN_IN_BUTTON_XPATH = ".//button[contains(text(),'Увiйти')]"

    # Profile
    CLOSE_YOUR_CITY_POPUP_XPATH = ".//a[@class='geo-close js-close-geo']"
    ACCOUNT_USERNAME_XPATH = ".//span[contains(text(),'{login_option}')]"
    PROFILE_BUTTON_XPATH = ".//div[@class='header-middle__personal hide-mob']//i[@class='ic-personal']"

    # Search
    SEARCH_BUTTON_XPATH = ".//div[@class='header-middle__search ']//i[@class='ic-search']"

    # Catalog
    CATALOG_FLOWERS_BUTTON_XPATH = ".//li[@class='main-menu__item']/a[@href='https://dicentra.ua/ua/czvetyi/']"
