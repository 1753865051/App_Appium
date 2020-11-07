from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class HomePage(BaseAction):
    me_button=By.ID, "com.yunmall.lc:id/tab_me"
    def click_me(self):
        self.click(self.me_button)

    def login_if_not(self, page):
        # page.img.click_img()
        self.click_me()
        if self.driver.current_activity !="com.yunmall.ymctoc.ui.activity.LogonActivity":
            return
        page.register.click_login()
        page.login.input_username("itheima_test")
        page.login.input_password("itheima")
        page.login.click_login()