from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from selenium import webdriver
import requests

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
    footer_links = bs.find(name="div", class_="footer_links-container").find_all("a")
    footer_li = []
    for item in footer_links:
        footer_li_child = []
        if len(item.get('href')):
            footer_li_child.append(item.get('href'))
            footer_li_child.append(item.get('target'))
            footer_li.append(footer_li_child)

    return footer_li

print(get_social_links("en_GB"))