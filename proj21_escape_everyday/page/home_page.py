"""
MY20 RYI Home Page
"""
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
import openpyxl
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from selenium import webdriver
import requests
from page.page import Page
from proj21_escape_everyday.data.urls import current_url
from proj21_escape_everyday.element.elements_define import ElementsDefine

class HomePage(Page):
    """
    MY20 RYI Home Page
    """
    def __init__(self, driver):
        """
        init function
        :param driver:
        """
        self.url = "/{}/home"
        super(HomePage, self).__init__(driver, current_url())
        self.element = ElementsDefine()

    def get_social_links(self):
        """
        Get HomePage Social Link
        :return:
        """
        social_links = self.find_elements(self.element.homepage_social_link)
        return [a.get_attribute("href") for a in social_links if a.get_attribute("href")]

    def check_response_code(self, url):
        headers = {
            # "Connection": "close",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=5))  # 失败之后重试
        s.mount('https://', HTTPAdapter(max_retries=5))
        r = s.get(url, headers=headers, timeout=20)
        return r.status_code

    def get_footer_links(self, locale):
        """
        check footer links
        """
        headers = {
            # "Connection": "close",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
        }
        url = f"https://hdguest:MLP@2017@change-your-ride.proferochina.com/{locale}/home"
        s = requests.Session()
        s.mount('http://', HTTPAdapter(max_retries=5))  # 失败之后重试
        s.mount('https://', HTTPAdapter(max_retries=5))
        r = s.get(url, headers=headers, timeout=20)
        bs = BeautifulSoup(r.text, "html.parser")
        footer_links = bs.find(name="div", class_="footer_links-container").find_all("a")
        footer_li = []
        for item in footer_links:
            footer_li_child = []
            if len(item.get('href')):
                footer_li_child.append(item.get('href'))
                footer_li_child.append(item.get('target'))
                footer_li.append(footer_li_child)

        return footer_li

