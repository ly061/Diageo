"""
MY20 RYI Booking Process Page
the steps:
    1. start from select dealer
    2. then goto ryi-booking
    3. goto ryi-thankyou
    4. check bike list
    5. goto booking
    6. goto final thankyou

"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page.page import Page
from proj12_ryi.data.urls import current_url
from proj12_ryi.element.elements_define import ElementsDefine

class BookingProcessPage(Page):
    """
    MY20 RYI Booking Process Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        # self.url = "/{}/location"
        super(BookingProcessPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

