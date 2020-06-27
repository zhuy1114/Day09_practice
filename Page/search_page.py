from Base.base import Base
from Page.element_page import ElementPage


class SearchPage(Base):
    def __init__(self):
        super().__init__()

    # 输入内容
    def input_search_text(self, text):
        self.send_text(ElementPage.edit_text, text)

    # 获取结果
    def get_search_results(self):
        results = self.find_elts(ElementPage.edit_text_results)
        return [i.text for i in results]



