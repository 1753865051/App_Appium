from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
class AboutPage(BaseAction):
    update_button = By.ID, "com.yunmall.lc:id/about_version_update"

    @allure.step('点击 更新版本')
    def click_uptdate(self):
        self.click(self.update_button)