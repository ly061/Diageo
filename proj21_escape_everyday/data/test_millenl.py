import time,os
import requests
import unittest
from requests.adapters import HTTPAdapter
from bs4 import BeautifulSoup
import pytest

"""
The market matrix excel utils
Get some matrix data from excel file. "V2.xlsx"
"""

__author__ = "Michael.Tian"

import openpyxl

__matrix_file_name__ = "V2.xlsx"


def get_social_links(locale):
    """
    check footer links
    """
    headers = {
        "Connection": "keep-alive",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"
    }
    url = f"https://hdguest:MLP@2017@change-your-ride.proferochina.com/{locale}/home"
    s = requests.Session()
    s.mount('http://', HTTPAdapter(max_retries=5))  # 失败之后重试
    s.mount('https://', HTTPAdapter(max_retries=5))
    r = s.get(url, headers=headers, timeout=20)
    bs = BeautifulSoup(r.text, "html.parser")
    social_links_list = bs.find(name="div", class_="footer__share-container").find_all("a")
    social_li = []
    for item in social_links_list:
        if len(item.get('href')):
            social_li.append(item.get('href'))

    return social_li


def get_social_matrix():
    """
    Get all soical link matrix
    locale column B
    Facebook Url column W
    Instagram Url column X
    Twitter Url column Y
    :return:
    """
    wb = openpyxl.load_workbook(__matrix_file_name__)
    sheet = wb["Sheet1"]
    res = {}
    for index in range(14, 15):
        locale = sheet["C{}".format(index)].value
        facebook = sheet["BA{}".format(index)].value
        instagram = sheet["AZ{}".format(index)].value
        twitter = sheet["AY{}".format(index)].value
        Youtube = sheet["AX{}".format(index)].value
        res[locale] = [link for link in [facebook, instagram, twitter, Youtube] if link]

    wb.close()
    return res


def test_ryi_check_social_link():
    """
    MY20 RYI Homepage check social link
    :return:
    """
    res = []
    # get social link matrix
    social_link_matrix = get_social_matrix()
    all_locales = ["en_GB"]
    print("表格", get_social_matrix())
    for locale in all_locales:
        # get social link
        social_links = get_social_links(locale)
        print("footer", social_links)
        if not sorted(social_links) == sorted(social_link_matrix[locale]):
            res.append(f"locale: [{locale}] social links is not equal. \rpage social links: {sorted(social_links)}\
                \rmatrix social links:{sorted(social_link_matrix[locale])}")
    print(res)

    if len(res):
        assert 0, "Some locales social links are incorrect."

def get_social_links_michael(self):
    """
    Get HomePage Social Link
    :return:
    """

    social_links = self.find_elements(self.element.homepage_social_link)
    return [a.get_attribute("href") for a in social_links if a.get_attribute("href")]

