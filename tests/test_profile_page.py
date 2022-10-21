import logging

import pytest


class TestProfilePage:
    log = logging.getLogger("[ProfilePage]")

    @pytest.fixture(scope="function")
    def open_profile_page(self, open_start_page, basic_user):
        """Open Profile page"""
        profile_page = open_start_page.header.navigate_to_profile()
        self.log.info("Profile is opened")
        return profile_page

    def test_success_sign_out(self, open_profile_page):
        """
        Fixture:
        - Create driver, open Start page
        - Open Profile page
        - Log In as basic user
        Steps:
        - Click Sign Out button
        - Verify success Sign Out
        """

        # Navigate from Account to StartPage
        open_start_page = open_profile_page.sign_out()

        # Verify success Sign Out
        open_start_page.verify_success_sign_out()
        self.log.info("Sign Out is successful")
