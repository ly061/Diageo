"""
MY20 RYI Booking process .
"""

import time,os
import unittest
import pytest
from random import choice
from driver.browser import *
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.expected_conditions as EC
from parameterized import parameterized, parameterized_class

#from proj12_ryi.data.locales import *
from proj12_ryi.data.marketmatrix_utils import *
from proj12_ryi.page.booking_process_page import BookingProcessPage
from common.fake_email_address import pick_one_address

@pytest.mark.ryi
class TestRyiBookingProcess(unittest.TestCase):
    """
    MY20 RYI Booking process
    """
    @classmethod
    def setUpClass(cls):
        cls.driver = chrome_browser()
        cls.currentPage = BookingProcessPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # @parameterized.expand(['en_EU', 'en_GB', 'en_IE', 'en_ZZ', 'es_ES', 'fi_FI', 'fr_BE', 'fr_CH', 'fr_FR', 'fr_LU'])
    @parameterized.expand(['cs_CZ', 'da_DK', 'de_AT', 'de_CH', 'de_DE', 'en_AA', 'en_CA', 'en_EU', 'en_GB', 'en_IE',
                           'en_ZZ', 'es_ES', 'es_MX', 'es_XX', 'fi_FI', 'fr_BE', 'fr_CA', 'fr_CH', 'fr_FR', 'fr_LU',
                           'hu_HU', 'it_CH', 'it_IT', 'nl_BE', 'nl_NL', 'no_NO', 'pl_PL', 'pt_PT', 'ru_RU', 'sv_SE'])
    #@parameterized.expand(['ru_RU'])
    def test_ryi_booking_process(self, locale):
        self.test_ryi_dealer_page(locale)

        self.test_ryi_booking_error_validation()

        self.test_ryi_booking_page_title()

        self.test_ryi_booking_page_privacy_popup()

        self.test_ryi_booking_submit()

        self.test_ryi_thankyou_page_title()

        self.test_ryi_check_bikelist()

        self.test_ryi_thankyou_select_bike()

        self.test_booking_title()

        self.test_booking_form()

        self.test_thankyou_title()

    @pytest.mark.skip()
    @pytest.mark.run(order=10)
    def test_ryi_dealer_page(self, locale):
        """
        12. MY20 RYI Booking process :select dealer
        """
        #open dealer page
        self.currentPage.url = "/{}/ryi-dealer".format(locale)
        self.currentPage.open()

        time.sleep(1)

        # input letter a
        self.currentPage.input_element_value(self.currentPage.element.dealerpage_dealer_locate, 'a')

        # wait for first result item
        self.currentPage.wait_for_page_element(
            EC.element_to_be_clickable(self.currentPage.element.dealerpage_googlemap_suggestfirst), 20)
        self.currentPage.key_action(Keys.DOWN)
        self.currentPage.key_action(Keys.ENTER)
        # self.currentPage.click_element(self.currentPage.element.dealerpage_googlemap_suggestfirst)

        # wait for the button
        self.currentPage.wait_for_page_element(
            EC.element_to_be_clickable(self.currentPage.element.dealerpage_next_button), 20)
        # click next button
        self.currentPage.click_element(self.currentPage.element.dealerpage_next_button, refresh_page=True)

        #
        self.assertIn("ryi-booking", self.driver.current_url.lower(), "Select dealer page Error! : [{}], it should be the ryi-booking.".format(self.driver.current_url))

    @pytest.mark.skip()
    @pytest.mark.run(order=20)
    def test_ryi_booking_error_validation(self):
        """
        12. MY20 RYI Booking process: booking error validation

        1. check the current page url should be ryi-booking
        :return:
        """

        self.assertIn("ryi-booking", self.driver.current_url.lower(), "The current url is incorrent : [{}], it should be the ryi-booking.".format(self.driver.current_url))

        # click the via post checkbox
        self.currentPage.click_element(self.currentPage.element.ryibooking_form_viapost)

        # click the submit button
        self.currentPage.click_element(self.currentPage.element.ryibooking_submit_button)

        # check the form errors
        form_errors = self.currentPage.find_elements(self.currentPage.element.ryibooking_form_errors)

        # the errors source
        errors_id = ["titleError", "firstNameError", "lastNameError", "emailError", "mobileError", "birthDayError", "myBikeNameError", "addressError1", "postcodeError"]

        # check the form_errors number
        self.assertEqual(len(form_errors), len(errors_id))

    @pytest.mark.skip()
    @pytest.mark.run(order=21)
    def test_ryi_booking_page_title(self):
        """
        RYI Booking page title checking.
        :return:
        """
        page_title = "Harley-Davidson® | Low Rider® S RYI - Enter your details"
        self.assertEqual(page_title, self.driver.title, "RYI Booking page title is incorrect: [{}]".format(self.driver.title))

    @pytest.mark.skip()
    @pytest.mark.run(order=22)
    def test_ryi_booking_page_privacy_popup(self):
        """
        RYI booking page privacy popup checking
        1. click page privacy notification link.
        2. check the first popup if showing.
        3. click the first popup close icon, check if the first popup if closing.
        :return:
        """

        # click privacy notification link
        self.currentPage.click_element(self.currentPage.element.ryibooking_privacy_page_link)

        # waiting for privacy popup showing
        self.currentPage.wait_for_page_element(
            EC.visibility_of_element_located(self.currentPage.element.ryibooking_privacy_first_popup))

        # check the privacy popup is visible
        self.assertTrue(self.currentPage.find_element(
            self.currentPage.element.ryibooking_privacy_first_popup).is_displayed(), "Privacy popup is not showing.")

        # click the first popup close icon
        self.currentPage.click_element(self.currentPage.element.ryibooking_privacy_first_popup_close)

        # waiting for first popup closing
        self.currentPage.wait_for_page_element(
            EC.invisibility_of_element_located(self.currentPage.element.ryibooking_privacy_first_popup))

        # check the first popup is not visible
        self.assertFalse(self.currentPage.find_element(
            self.currentPage.element.ryibooking_privacy_first_popup).is_displayed(), "First popup is not closing.")

    @pytest.mark.skip()
    @pytest.mark.run(order=23)
    def test_ryi_booking_submit(self):
        """
        MY20 RYI booking process: auto submit booking
        1. Title : select first one.
        2. First Name : Test_RYI_FN
        3. Last Name: Test_RYI_LN
        4. Email: Random genrator one email
        5. Mobile: 123456789
        6. Date of birth: 29-07-1990
        7. License: Yes
        8. Motocycle: choice one ["Aprilia", "BMW", "Ducati", "HarleyDavidson", "Honda", "Hyosung", "Indian", "Kawasaki", "KTM", "Moto Guzzi", "MVAgusta", "Other", "Suzuki", "Triumph", "Victory", "Yamaha"]
        9. Via email: Yes
        10.Via phone: Yes
        11.Submit the form.
        :return:
        """
        form_data = {
            "firstname": "Test_RYI_FN",
            "lastname": "Test_RYI_LN",
            "email": pick_one_address(),
            "mobile": "123456789",
            "birthday": "29-07-1990",
            "motocycle": choice(["Aprilia", "BMW", "Ducati", "HarleyDavidson", "Honda", "Hyosung", "Indian", "Kawasaki", "KTM", "Moto Guzzi", "MVAgusta", "Other", "Suzuki", "Triumph", "Victory", "Yamaha"])
        }
        # 1. Title
        self.currentPage.select_element_by_index(self.currentPage.element.ryibooking_form_title, 1)

        # 2. First Name
        self.currentPage.input_element_value(self.currentPage.element.ryibooking_form_firstname, form_data["firstname"])

        # 3. Last Name
        self.currentPage.input_element_value(self.currentPage.element.ryibooking_form_lastname, form_data["lastname"])

        # 4. Email
        self.currentPage.input_element_value(self.currentPage.element.ryibooking_form_email, form_data["email"])

        # 5. Mobile
        self.currentPage.input_element_value(self.currentPage.element.ryibooking_form_mobile, form_data["mobile"])

        # 6. Birthday
        #self.currentPage.input_element_value(self.currentPage.element.ryibooking_form_birthday, form_data["birthday"])
        self.currentPage.script('document.querySelector("#birthDay").value = "{}"'.format(form_data["birthday"]))

        # 8. Motocycle
        self.currentPage.select_element_by_value(self.currentPage.element.ryibooking_form_motocycle, form_data["motocycle"])

        # 9. Via Email
        self.currentPage.click_element(self.currentPage.element.ryibooking_form_viaemail)

        # 10. Via Phone
        self.currentPage.click_element(self.currentPage.element.ryibooking_form_viaphone)

        # 11. Close Via Post
        self.currentPage.click_element(self.currentPage.element.ryibooking_form_viapost)

        # 11. Submit Form, waiting for page refresh.
        self.currentPage.click_element(self.currentPage.element.ryibooking_submit_button, refresh_page=True)

        # 12 check the URL if correct.
        self.assertIn("ryi-thankyou", self.driver.current_url.lower(), "The current url is incorrect :[{}], it should be the ryi-thankyou.".format(self.driver.current_url))

    @pytest.mark.skip()
    @pytest.mark.run(order=30)
    def test_ryi_thankyou_page_title(self):
        """
        Check ryi thankyou page title.
        :return:
        """
        page_title = "Harley-Davidson® | Low Rider® S RYI - Thanks"
        self.assertEqual(page_title, self.driver.title, "RYI Thankyou title is incorrect: [{}]".format(self.driver.title))

    @pytest.mark.skip()
    @pytest.mark.run(order=31)
    def test_ryi_check_bikelist(self):
        """
        Check RYI thankyou page BikeList
        0. Get current locale from URL
        1. Get the bikelist matrix from excel
        2. Get the bikelist from current page.
        3. Check those two bikelist if equal?
        :return:
        """
        # 0. locale : [https://hdguest:MLP%402017@my20-ryi.proferochina.com/en_GB/Select]
        locale = self.driver.current_url.split('/')[-2]

        # 1. Get bikelist matrix
        bikes = get_bike_matrix()[locale]
        #self.currentPage.logger.warning(bikes)
        # 2. Get page bike list
        res = []
        categories = self.currentPage.find_elements(self.currentPage.element.ryithankyou_bikelist)
        cant_decide = self.currentPage.find_element(self.currentPage.element.ryithankyou_cant_decide)
        for index, c in enumerate(categories):
            title = c.find_element_by_css_selector(self.currentPage.element.ryithankyou_bikelist_title[1]).text.strip()
            bl = c.find_elements_by_css_selector(self.currentPage.element.ryithankyou_bikelist_list[1])
            bikeid = [a.get_attribute("data-href").split("=")[1] for a in bl if a.get_attribute("data-href") and a.get_attribute("data-href").find("=") > -1]
            if index == 2:
                bikeid.append(cant_decide.get_attribute('href').split("=")[1])
            if not sorted(bikes[index]) == sorted(bikeid):
                res.append("Locale: [{}], Category: [{}], Matrix: [{}], Page: [{}]".format(locale, title, sorted(bikes[index]), sorted(bikeid)))
                self.currentPage.logger.warning(res[-1])

        if len(res):
            assert 0, "Some bike list is incorrect"

    @pytest.mark.skip()
    @pytest.mark.run(order=32)
    def test_ryi_thankyou_select_bike(self):
        """
        Click one bike, goto booking page.
        :return:
        """

        bike = self.currentPage.find_elements(self.currentPage.element.ryithankyou_bikelist_list)[-1]
        bike.click()
        with self.currentPage.wait_for_page_load():
            bike.click()

        #self.currentPage.click_element(self.currentPage.element.ryithankyou_bikelist_list, refresh_page=True)

        # check the URL if correct.
        self.assertIn("booking", self.driver.current_url.lower(),
                      "The current url is incorrent :[{}], it should be the booking.".format(
                          self.driver.current_url))
        self.currentPage.logger.warning(self.driver.current_url)

    @pytest.mark.skip()
    def test_booking_title(self):
        """
        Check booking page title
        :return:
        """
        page_title = "Harley-Davidson® | Low Rider® S RYI - Softail test ride"
        self.assertEqual(page_title, self.driver.title,
                         "Booking title is incorrect: [{}]".format(self.driver.title))

    @pytest.mark.skip()
    def test_booking_form(self):
        """
        Submit booking form
        :return:
        """

        #self.currentPage.input_element_value(self.currentPage.element.booking_form_email, "michael.tian@profero.com")

        # wait for the button
        self.currentPage.wait_for_page_element(
            EC.element_to_be_clickable(self.currentPage.element.booking_submit_button))

        self.currentPage.click_element(self.currentPage.element.booking_submit_button, refresh_page=True)

        # check the URL if correct.
        self.assertIn("thankyou", self.driver.current_url.lower(),
                      f"The current url is incorrect: [{self.driver.current_url}], it should be the final thankyou.")

    @pytest.mark.skip()
    def test_thankyou_title(self):
        """
        Check final thankyou page title
        :return:
        """
        page_title = "Harley-Davidson® | Low Rider® S RYI - Softail test ride thanks"
        self.assertEqual(page_title, self.driver.title,
                         "Final thankyou page title is incorrect: [{}]".format(self.driver.title))


if __name__ == "__main__":
    unittest.main()