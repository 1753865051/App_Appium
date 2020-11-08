from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
class HomePage(BaseAction):
    me_button = By.ID, "com.yunmall.lc:id/tab_me"
    category_button = By.ID, "com.yunmall.lc:id/tab_category"
    shop_cart_button=By.ID, "com.yunmall.lc:id/tab_shopping_cart"
    home_button = By.ID, "com.yunmall.lc:id/tab_home"
    search_button = By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    @allure.step('主页 点击 我')
    def click_me(self):
        self.click(self.me_button)

    @allure.step('主页 点击 分类')
    def click_category(self):
        self.click(self.category_button)
    @allure.step('主页 点击 购物车')
    def click_shop_cart(self):
        self.click(self.shop_cart_button)

    @allure.step('主页 登录(如果没有登录)')
    def login_if_not(self, page):
        # page.img.click_img()
        self.click_me()
        if self.driver.current_activity !="com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        page.register.click_login()
        page.login.input_username("itheima_test")
        page.login.input_password("itheima")
        page.login.click_login()
    @allure.step('主页 点击 放大镜')
    def click_search(self):
        self.click(self.search_button)
    @allure.step('主页 点击 首页')
    def click_home(self):
        self.click(self.home_button)