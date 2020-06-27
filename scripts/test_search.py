import pytest

from Base.driver import Driver
from Base.page import Page
from Base.readData import GetData


def search_data():
    data_list = []
    data = GetData.get_yaml_data("search_data.yml")
    for i in data.values():
        data_list.append((i.get("input_data"), i.get("expect_data")))
    return data_list


class TestSearch:
    def teardown_class(self):
        Driver.quit_driver()

    # 只执行一次点击搜索按钮
    @pytest.fixture(scope='class', autouse=True)
    def click_search_button(self):
        Page.get_setting_page().click_search_btn()

    # 输入结果获取结果断言
    @pytest.mark.parametrize("input_data,expect_data", search_data())
    def test_search_text(self, input_data, expect_data):
        Page.get_search_page().input_search_text(input_data)
        assert expect_data in Page.get_search_page().get_search_results()
