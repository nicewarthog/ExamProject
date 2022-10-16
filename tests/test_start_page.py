import logging

from pages.utils import User


class TestStartPage:
    log = logging.getLogger("[StartPage]")

    # SIGN IN

    def test_success_sign_up(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Go to Sign Up form
        - Fill phone, username, password
        - Click Sign Up button
        - Verify success registration
        """

        # Sign Up as a user
        new_random_user = User()
        new_random_user.random_user_data()
        open_start_page.sign_up(new_random_user)
        self.log.info("Signed Up as user %s", new_random_user.login)

        # Verify success
        open_start_page.verify_success_sign_up(new_random_user.login)
        self.log.info(f"Account name {new_random_user.login} was verified, Sign Up was successfully")

    # SIGN IN

    def test_correct_log_in(self, open_start_page):
        """
        Fixture:
        - Create driver, open page
        Steps:
        - Go to Sign In form
        - Fill phone, password
        - Click Sign In button
        - Verify success Sign In
        """

        # Log in as user
        basic_user = User(login="Ігор", phone="974955232", password="qwerty")
        open_start_page.sign_in(basic_user)

        # Verify success
        open_start_page.verify_success_sign_in(basic_user.login)
        self.log.info(f"Account name {basic_user.login} was verified, Sign In was successfully")

    # def test_add_to_cart(self, open_start_page, basic_user):
    #     """
    #     Fixture:
    #     - Create driver, open page
    #     - Sign In as basic user
    #     Steps:
    #     - Go to page of some product
    #     - Add to Cart the product
    #     - Verify the product on cart page
    #     """
    #
    #     # Navigate to CatalogPage
    #     catalog_page = open_start_page.start_page.navigate_to_catalog_page()
    #
    #     # Navigate to Product Card
    #     # sleep(1)
    #     card_page = catalog_page.navigate_to_product_card()
    #
    #     # Add to cart
    #     sleep(1)
    #     favorite_page = card_page.add_to_favorite()
    #
    #     sleep(1)
    #     favorite_page.verify_favorite_product()
