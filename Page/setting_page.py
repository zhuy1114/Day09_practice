from Base.base import Base
from Page.element_page import ElementPage


class SettingPage(Base):
    def __init__(self):
        super().__init__()

    """点击搜索按钮"""

    # 点击搜索按钮
    def click_search_btn(self):
        self.click_btn(ElementPage.search_btn)
