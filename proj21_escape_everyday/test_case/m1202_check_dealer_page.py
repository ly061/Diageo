"""
MY20 RYI Dealer checking.
"""

import time,os
import unittest
import pytest
from driver.browser import *
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from proj12_ryi.data.locales import *
from proj12_ryi.page.dealer_page import DealerPage

@pytest.mark.ryi
@pytest.mark.live_checker
class TestRYICheckDealerPage(unittest.TestCase):
    """
    MY20 RYI Dealer page
    """
    def setUp(self):
        self.driver = firefox_browser()
        self.dealerPage = DealerPage(self.driver)
    def tearDown(self):
        self.driver.quit()

    def test_ryi_check_dealer_page(self):
        """
        12. MY20 RYI Dealer page
        steps:
            1. Input letter 'a' into google map
            2. Select first result item
            3. Click the next button goto ryi-booking page
        """
        # check all locale
        for locale in Testing:
            # open dealer page
            self.dealerPage.url = self.dealerPage.url.format(locale)
            self.dealerPage.open()

            # input letter a
            self.dealerPage.input_element_value(self.dealerPage.element.dealerpage_dealer_locate, 'a')

            # wait for first result item
            self.dealerPage.wait_for_page_element(EC.element_to_be_clickable(self.dealerPage.element.dealerpage_googlemap_suggestfirst), 20)
            self.dealerPage.key_action(Keys.DOWN)
            self.dealerPage.key_action(Keys.ENTER)
            # self.dealerPage.click_element(self.dealerPage.element.dealerpage_googlemap_suggestfirst)

            # wait for the button
            self.dealerPage.wait_for_page_element(EC.element_to_be_clickable(self.dealerPage.element.dealerpage_next_button), 20)
            # click next button
            self.dealerPage.click_element(self.dealerPage.element.dealerpage_next_button, refresh_page=True)

    def test_ryi_check_cookie_model(self):
        """
        MY20 RYI check cookie panel
        1. New user show the cookie panel.
        2. Click close button , the cookie panel disappear.
        3. The second time , the cookie panel didn't show again.
        :return:
        """
        error = []
        for locale in Testing:

            # open dealer page
            self.dealerPage.url = self.dealerPage.url.format(locale)
            self.dealerPage.open()

            # wait for the cookie panel display
            self.dealerPage.wait_for_page_element(
                EC.visibility_of_element_located(self.dealerPage.element.homepage_cookiemodel), 10)
            # get the cookie copy
            cookie = self.dealerPage.get_element_text(self.dealerPage.element.homepage_cookiemodel)
            if cookie in ["--", ""]:
                error.append(locale)
                self.dealerPage.logger.warning("the locale [{}] missing cookie panel".format(locale))

        # the last time close the cookie panel
        self.dealerPage.click_element(self.dealerPage.element.homepage_cookiemodel_close)
        # wait for the cookie panel disappear
        self.dealerPage.wait_for_page_element(EC.invisibility_of_element_located(self.dealerPage.element.homepage_cookiemodel), 10)
        # check the cookie model is not visible
        self.assertFalse(self.dealerPage.find_element(self.dealerPage.element.homepage_cookiemodel).is_displayed(), "close cookie panel failed.")

        if len(error):
            self.assertTrue(0, "Some locale missing cookie, please see logs.")


if __name__ == "__main__":
    unittest.main()
