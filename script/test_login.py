import time

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
import pytest
class TestLogin:
    """
    登录没的可说的
    """
    def setup(self):
        self.driver=init_driver(no_reset=False)
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(2)
        self.driver.quit()
    # def test_hello(self):
    #     self.page.home.login_if_not(self.page)
    @pytest.mark.parametrize("args",analyze_file("login_data.yaml","test_login"))
    def test_login(self,args):
        username = args["username"]
        password = args["password"]
        toast = args["toast"]
        # self.page.img.click_img()
        self.page.home.click_me()
        self.page.register.click_login()
        self.page.login.input_username(username)
        self.page.login.input_password(password)
        self.page.login.click_login()
        if toast is None:
            assert self.page.me.get_nick_name_text() == username ,"登录的和输入的不一致"
        else:
            self.page.login.is_toast_exist(toast)
