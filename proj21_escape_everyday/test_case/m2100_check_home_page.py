"""
MY20 RYI Home checking.
"""

import unittest
import pytest
from driver.browser import chrome_browser
from proj21_escape_everyday.data.locales import All_Locales
from proj21_escape_everyday.data.marketmatrix_utils import get_social_matrix
from proj21_escape_everyday.page.home_page import HomePage





class TestEsacpeCheckHomePage(unittest.TestCase):
    """
    Test Esacpe Check HomePage
    """

    def setUp(self):
        self.driver = chrome_browser()
        self.homePage = HomePage(self.driver)

    def tearDown(self):
        self.driver.quit()

    @pytest.mark.run(order=1)
    def test_escape_check_social_link(self):
        """
        MY20 RYI Homepage check social link
        :return:
        """
        res = []
        # get social link matrix
        social_link_matrix = get_social_matrix()
        for locale in All_Locales:
            # open locale homePage
            self.homePage.url = "/{}/home".format(locale)
            self.homePage.open()

            # get social link
            social_links = self.homePage.get_social_links()
            if not sorted(social_links) == sorted(social_link_matrix[locale]):
                res.append(f"locale: [{locale}] social links is not equal. \rpage social links: {sorted(social_links)}\
                    \rmatrix social links:{sorted(social_link_matrix[locale])}")
                self.homePage.logger.warning(res[-1])

        if len(res):
            assert 0, "Some locales social links are incorrect."


    @pytest.mark.run(order=2)
    def test_escape__check_footer_link(self):
        """
        MY20 RYI homepage check footer links
        :return:
        """
        footer_links = ["privacy-policy", "terms-of-use", "we-care-about-you", "cookie-policy", "cookie-opt-out"]
        link_template = "https://www.harley-davidson.com/{}/{}/footer/utility/{}.html"

        res = []
        for locale in All_Locales:
            footer_link = self.homePage.get_footer_links(locale)
            for link in footer_link:
                if self.homePage.check_response_code(link[0]) != 200:
                    res.append(f"locale: {locale}, footer link:{link[0]} response code is incorrect, code: {self.homePage.check_response_code(link[0])} !")
                    self.homePage.logger.warning(res[-1])

            for index, li in enumerate(footer_link):
                href = li[0]
                target = li[1]
                if target != "_blank" or href != link_template.format(locale.split('_')[1], locale.split('_')[0], footer_links[index]).lower():
                    res.append(f"locale: {locale}, footer link:{href} is incorrect, target: {target} !")
                    self.homePage.logger.warning(res[-1])

        if len(res):
            assert 0, "some locale footer link is not correct, please see the log."

    # def test_ryi_check_ryi_button(self):
    #     """
    #     MY20 RYI Homepage check register you interest button
    #     :return:
    #     """
    #     for locale in All_Locales:
    #         # open locale homePage
    #         self.homePage.url = "/{}/home".format(locale)
    #         self.homePage.open()
    #
    #         # waiting for the bottom ryi button
    #         self.homePage.wait_for_page_element(EC.visibility_of_element_located(self.homePage.element.homepage_ryi_button))
    #
    #         # click the ryi button
    #         self.homePage.click_element(self.homePage.element.homepage_ryi_button, refresh_page=True)
    #
    #         # check url if is the ryi-dealer
    #         self.assertIn("ryi-dealer", self.driver.current_url.lower(),
    #                       f"The current url is not correct :[{self.driver.current_url}], it should be the ryi-dealer.")
    #


    #
    # def test_ryi_check_footer_country_list(self):
    #     """
    #     MY20 RYI homepage check footer country_list
    #     Only check en_GB locale
    #     :return:
    #     """
    #     # open locale homePage
    #     self.homePage.url = "/{}/home".format("en_GB")
    #     self.homePage.open()
    #
    #     options = self.homePage.find_elements(self.homePage.element.homepage_footer_country_list)
    #     opts = [o.get_attribute('value') for o in options if o.get_attribute('value') and o.get_attribute('value') != "SWITCH LOCATION"]
    #
    #     # self.homePage.logger.warning(sorted(opts))
    #     # self.homePage.logger.warning(get_all_locale())
    #     self.assertListEqual(sorted(opts), sorted(get_all_locale()))
    #
    # def test_ryi_check_tracking_code(self):
    #     """
    #     MY20 RYI homepage check tracking code
    #     :return:
    #     """
    #
    #     # dtm_script = "<script src=\"//assets.adobedtm.com/launch-EN809b0f5705984a49bcf4ef12cfbb5073-development.min.js\" async></script>"
    #     # grm_script = "<script src='//grmtech.net/r/de806fec5af7f5b48b8a31a003e171f3fb.js' async defer></script>"
    #     dtm_script_id = "launch-EN809b0f5705984a49bcf4ef12cfbb5073-development.min.js"
    #     grm_script_id = "de806fec5af7f5b48b8a31a003e171f3fb.js"
    #
    #     res = []
    #     for locale in All_Locales:
    #         # open locale homePage
    #         self.homePage.url = "/{}/home".format(locale)
    #         self.homePage.open()
    #
    #         if dtm_script_id not in self.driver.page_source:
    #             res.append(f"Locale :{locale}, missing DTM Tracking Code!")
    #             self.homePage.logger.warning(res[-1])
    #         if locale != "en_ZZ" and grm_script_id not in self.driver.page_source:
    #             res.append(f"Locale :{locale}, missing Media Tracking Code!")
    #             self.homePage.logger.warning(res[-1])
    #
    #     if len(res):
    #         assert 0, "some tracking code  is not correct, please see the log."

if __name__ == "__main__":
    unittest.main()
