from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class RegistePage(BaseAction):
    login_button=By.ID, "com.yunmall.lc:id/textView1"
    def click_login(self):
        self.click(self.login_button)