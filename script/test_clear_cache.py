import time
import allure
from base.base_driver import init_driver
from page.page import Page

class TestClearCache:
    """
    缓存清理
    """
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(1)
        self.driver.quit()
    def test_clear_cache(self):
        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_cleat_cache()
        assert self.page.about.is_toast_exist("清理成功")