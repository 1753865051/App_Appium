from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class LoginPage(BaseAction):
    username_edit_test=By.ID, "com.yunmall.lc:id/logon_account_textview"
    password_edit_test = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_button=By.ID, "com.yunmall.lc:id/logon_button"
    def input_username(self,test):
        self.input(self.username_edit_test,test)
    def input_password(self,test):
        self.input(self.password_edit_test,test)
    def click_login(self):
        self.click(self.login_button)