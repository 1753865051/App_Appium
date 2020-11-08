from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
class SearchPage(BaseAction):
    keyword_edit_text=By.ID, "com.yunmall.lc:id/text_search_keyword"
    search_button=By.ID, "com.yunmall.lc:id/button_search"
    search_del_button =By.ID ,"com.yunmall.lc:id/search_del"
    @allure.step('搜索 输入 关键字')
    def input_keyword(self,text):
        self.input(self.keyword_edit_text,text)
    @allure.step('搜索 点击 搜索')
    def click_search(self):
        self.click(self.search_button)
    @allure.step('搜索 删除')
    def click_search_del(self):
        self.click(self.search_del_button)
    def is_keyword_exist(self,keyword):
        xpath=By.XPATH, "//*[@resource-id='com.yunmall.lc:id/keyayout']/*/*[@text='%s']" % keyword
        return self.is_feature_exit(xpath)

    def is_search_record_empty(self):
        festure =By.XPATH, "//*[@text='暂时无搜索历史']"
        self.is_feature_exit(festure)
