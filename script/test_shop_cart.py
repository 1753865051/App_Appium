import time

from base.base_driver import init_driver
from page.page import Page

class TestShopCart:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(1)
        self.driver.quit()
    def test_add_shop_cart(self):
        self.page.home.login_if_not(self.page)
        self.page.home.click_category()
        self.page.categort.click_goods_list()
        self.page.goods_list.click_goods()
        goods_title=self.page.goods_detall.get_goods_title_text()
        self.page.goods_detall.click_add_shop_cart()
        self.page.goods_detall.click_spec()
        self.page.goods_detall.click_shop_cart()
        assert self.page.goods_detall.is_goods_titles_exit(goods_title)

    def test_shop_cart_price(self):
        self.page.home.login_if_not(self.page)
        self.page.home.click_shop_cart()
        self.page.shop_cart.click_select_all()
        all_price = self.page.shop_cart.get_all_price()
        self.page.shop_cart.click_edit()
        self.page.shop_cart.click_add()
        self.page.shop_cart.click_cummit()
        assert self.page.shop_cart.get_all_price() == all_price + self.page.shop_cart.get_price()

    def test_del_shop_cart(self):
        self.page.home.login_if_not(self.page)
        self.page.home.click_shop_cart()
        if self.page.shop_cart.is_shop_cart_empty():
            self.page.home.click_category()
            self.page.categort.click_goods_list()
            self.page.goods_list.click_goods()
            goods_title = self.page.goods_detall.get_goods_title_text()
            self.page.goods_detall.click_add_shop_cart()
            self.page.goods_detall.click_spec()
            self.page.goods_detall.press_back()
            time.sleep(2)
            self.page.goods_detall.press_back()
            self.page.home.click_shop_cart()

        self.page.shop_cart.click_select_all()
        self.page.shop_cart.click_edit()
        self.page.shop_cart.click_delete()
        self.page.shop_cart.click_yes()
        assert self.page.shop_cart.is_toast_exist("删除成功")
        assert self.page.shop_cart.is_shop_cart_empty()