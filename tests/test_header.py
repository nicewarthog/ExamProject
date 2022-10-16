import logging


class TestHeader:
    log = logging.getLogger("[Header]")

    # def test_correct_log_in(self, open_start_page):
    #     """
    #     Fixture:
    #     - Create driver, open page
    #     Steps:
    #     - Go to Sign In form
    #     - Fill email, password
    #     - Click Sign In button
    #     - Verify success Sign In
    #     """
    #
    #     # Log in as user
    #     basic_user = User(login="Максим", email="max_sol@gmail.com", password="maxmaxmax")
    #     open_start_page.sign_in(basic_user)
    #
    #     # Verify success
    #     open_start_page.verify_success_sign_in(basic_user.login)
    #     self.log.info(f"Account name {basic_user.login} was verified, Sign In was successfully")
