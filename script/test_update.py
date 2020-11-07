from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
import pytest

class TestUpdate:
    """
    更新版本
    """
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def test_update(self):
        #没有登录先登录
        self.page.home.login_if_not(self.page)
        #我 -点击设置
        self.page.me.click_setting()
        self.page.setting.click_about()
        self.page.about.click_uptdate()
        assert self.page.about.is_toast_exist("当前已是最新版本")