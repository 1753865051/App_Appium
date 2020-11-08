import random
import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class CategoryPage(BaseAction):
    goods_list_button=By.ID, "com.yunmall.lc:id/iv_img"

    @allure.step('分类 点击 商品列表')
    def click_goods_list(self):
        goods_lists=self.find_elements(self.goods_list_button)
        goods_list_count=len(goods_lists)
        goods_lists_index=random.randint(0,goods_list_count -1)
        goods_lists[goods_lists_index].click()