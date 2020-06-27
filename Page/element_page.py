from selenium.webdriver.common.by import By


class ElementPage:
    """设置页面"""
    # 搜索按钮
    search_btn = (By.ID, "com.android.settings:id/search")

    """搜索页面"""
    # 输入框
    edit_text = (By.ID, "android:id/search_src_text")

    # 获取结果元素
    edit_text_results = (By.ID, "com.android.settings:id/title")
