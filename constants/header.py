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
    SIGN_IN_EMPTY_PHONE_MESSAGE_TEXT = "Будь ласка, введіть дійсний телефон"
    SIGN_IN_EMPTY_PHONE_MESSAGE_XPATH = f".//span[contains(text(),'{SIGN_IN_EMPTY_PHONE_MESSAGE_TEXT}')]"
    SIGN_IN_EMPTY_PASSWORD_MESSAGE_TEXT = "Вкажіть Ваш пароль"
    SIGN_IN_EMPTY_PASSWORD_MESSAGE_XPATH = f".//span[contains(text(),'{SIGN_IN_EMPTY_PASSWORD_MESSAGE_TEXT}')]"
    SIGN_IN_INCORRECT_PHONE_MESSAGE_TEXT = "Зазначеного користувача не знайдено"
    SIGN_IN_INCORRECT_PHONE_MESSAGE_XPATH = f".//span[contains(text(),'{SIGN_IN_INCORRECT_PHONE_MESSAGE_TEXT}')]"
    SIGN_IN_INCORRECT_PASSWORD_MESSAGE_TEXT = "Помилка: Неправильне ім'я або пароль користувача."
    SIGN_IN_INCORRECT_PASSWORD_MESSAGE_XPATH = ".//div[@class='btn-holder']/span[@class='error-text']"

    # Profile
    ACCOUNT_USERNAME_XPATH = ".//span[contains(text(),'{login_option}')]"
    PROFILE_BUTTON_XPATH = ".//div[@class='header-middle__personal hide-mob']//i[@class='ic-personal']"

    # Search
    SEARCH_BUTTON_XPATH = ".//div[@class='header-middle__search ']//i[@class='ic-search']"
    SEARCH_FIELD_XPATH = ".//input[@id='search__input']"
    SEARCH_LIST_BUTTON_XPATH = ".//a[@href='search/?query={search_option}']"
    SEARCH_INCORRECT_TEXT = "За вашим запитом нічого не знайдено"
    SEARCH_INCORRECT_XPATH = f".//p[contains(text(),'{SEARCH_INCORRECT_TEXT}')]"

    # Catalog
    CATALOG_FLOWERS_BUTTON_XPATH = ".//ul[@class='main-menu__list']//a[@href='https://dicentra.ua/ua/czvetyi/']"
