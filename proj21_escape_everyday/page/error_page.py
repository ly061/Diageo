"""
MY20 RYI Error Page
"""

from page.page import Page
from proj12_ryi.data.urls import current_url
from proj12_ryi.element.elements_define import ElementsDefine


class ErrorPage(Page):
    """
    MY20 RYI Error Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/{}/404"
        super(ErrorPage, self).__init__(driver, current_url())
        self.element = ElementsDefine()
