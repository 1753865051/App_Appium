from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
class GoodsDetallPage(BaseAction):
    add_shop_cart_button=By.ID, "com.yunmall.lc:id/btn_add_to_shopping_cart"
    commit_button=By.XPATH, "//*[@text='确认']"
    goods_title_text_view=By.ID, "com.yunmall.lc:id/tv_product_title"
    shop_cart_button=By.ID, "com.yunmall.lc:id/btn_shopping_cart"
    @allure.step('商品详情 点击 添加购物车')
    def click_add_shop_cart(self):
        self.click(self.add_shop_cart_button)

    @allure.step('商品详情 点击 确认')
    def click_commit(self):
        self.click(self.commit_button)

    @allure.step('商品详情 点击 点击第一个规格')
    def get_choose_spec(self, text):
        return text.split(" ")[1]

    @allure.step('商品详情 选择规格')
    def click_spec(self):
        while True:
            self.click_commit()
            if self.is_toast_exist("请选择"):
                spec_name=self.get_choose_spec(self.get_toast_text("请选择"))
                spec_feature=By.XPATH,"//*[@text='%s']/../*[2]/*[1]" % spec_name
                self.click(spec_feature)
            else:
                break

    @allure.step('商品详情 获取商品标题')
    def get_goods_title_text(self):
        return self.get_text(self.goods_title_text_view)

    @allure.step('商品详情 点击 购物车')
    def click_shop_cart(self):
        self.click(self.shop_cart_button)

    @allure.step('商品详情 判断 商品是否存在')
    def is_goods_titles_exit(self,title):
        title_xpath=By.XPATH,"//*[@text='%s']" % title
        return self.is_feature_exit(title_xpath)