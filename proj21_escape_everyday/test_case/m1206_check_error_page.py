"""
MY20 RYI Error checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *

from proj12_ryi.data.locales import *
from proj12_ryi.page.error_page import ErrorPage
import selenium.webdriver.support.expected_conditions as EC

@pytest.mark.ryi
class TestRYICheckErrorPage(unittest.TestCase):
    """
    MY20 RYI Error page
    """
    def setUp(self):
        self.driver = chrome_browser()
        self.errorPage = ErrorPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_errorpage_goback_button(self):
        """
        MY20 RYI Error page check Go back button
        :return:
        """
        res = []

        for locale in All_Locales:
            # open locale homePage
            self.errorPage.url = "/{}/404".format(locale)
            self.errorPage.open()

            # waiting for the go back button
            self.errorPage.wait_for_page_element(
                EC.visibility_of_element_located(self.errorPage.element.errorpage_goback_button))

            # click the go back button
            self.errorPage.click_element(self.errorPage.element.errorpage_goback_button, refresh_page=True)

            # check url if is the home
            self.assertIn("home", self.driver.current_url.lower(),
                          f"The current url is not correct :[{self.driver.current_url}], it should be the /home.")



if __name__ == "__main__":
    unittest.main()
