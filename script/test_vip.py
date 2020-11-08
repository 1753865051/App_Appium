import time

from base.base_driver import init_driver
from page.page import Page

class TestVip:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(1)
        self.driver.quit()
    # def test_vip(self):
    #     self.page.home.login_if_not(self.page)
    #     self.page.me.click_be_vip()
    #     print(self.driver.contexts)
    #     #切换web环境
    #     self.driver.switch_to.context("WEBVIEW_com.yunmall.lc")
    #     self.page.vip.input_invite("test")
    #     self.page.vip.click_be_vip()
    #     self.driver.switch_to.context("NATIVE_APP")

