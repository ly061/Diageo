"""
MY20 RYI Home Page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

from page.page import Page
from proj12_ryi.data.urls import current_url
from proj12_ryi.element.elements_define import ElementsDefine

class DealerPage(Page):
    """
    MY20 RYI Dealer Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/{}/location"
        super(DealerPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

