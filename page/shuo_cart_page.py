from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
class ShopCartPage(BaseAction):
    select_all_button =By.ID, "com.yunmall.lc:id/iv_select_all"
    @allure.step("购物车 点击 全选")
    def click_select_all(self):
        self.click(self.select_all_button)

    edit_button =By.XPATH, "//*[@text='编辑']"
    @allure.step("购物车 点击 编辑")
    def click_edit(self):
        self.click(self.edit_button)

    cummit_button =By.XPATH, "//*[@text='完成']"
    @allure.step("购物车 点击 完成")
    def click_cummit(self):
        self.click(self.cummit_button)

    add_button =By.ID, "com.yunmall.lc:id/iv_add"
    @allure.step("购物车 点击 +")
    def click_add(self):
        self.click(self.add_button)

    price_feature=By.ID, "com.yunmall.lc:id/tv_price"

    all_price_feature = By.ID, "com.yunmall.lc:id/tv_count_money"
    def get_price(self):
        price_text=self.get_text(self.price_feature)
        return self.deal_with_price(price_text)
    def get_all_price(self):
        price_text=self.get_text(self.all_price_feature)
        return self.deal_with_price(price_text)
    def deal_with_price(self,price):
        return float(price[2:])
    delete_button =By.XPATH, "//*[@text='删除']"
    yes_button = By.XPATH, "//*[@text='确认']"
    def click_delete(self):
        self.click(self.delete_button)
    def click_yes(self):
        self.click(self.yes_button)
    def is_shop_cart_empty(self):
        xpath=By.XPATH, "//*[contains(@text,'购物车还是空的')]"
        return self.is_feature_exit(xpath)
