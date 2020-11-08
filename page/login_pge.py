from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
class LoginPage(BaseAction):
                              #com.yunmall.lc:id/logon_account_textview
    username_edit_test=By.ID, "com.yunmall.lc:id/logon_account_textview"
    password_edit_test = By.ID, "com.yunmall.lc:id/logon_password_textview"
    login_button=By.ID, "com.yunmall.lc:id/logon_button"

    @allure.step('登录 输入 用户名')
    def input_username(self,test):
        self.input(self.username_edit_test,test)

    @allure.step('注册 输入 密码')
    def input_password(self,test):
        self.input(self.password_edit_test,test)

    @allure.step('登录 点击 登录')
    def click_login(self):
        self.click(self.login_button)