"""统一管理实例化页面"""
from Page.search_page import SearchPage
from Page.setting_page import SettingPage


class Page:
    @classmethod
    def get_setting_page(cls):
        return SettingPage()

    @classmethod
    def get_search_page(cls):
        return SearchPage()
