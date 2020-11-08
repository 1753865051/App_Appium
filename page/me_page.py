import time
import allure
from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class MePage(BaseAction):

    nick_name_text_view = By.ID, "com.yunmall.lc:id/tv_user_nikename"
    setting_button=By.ID, "com.yunmall.lc:id/ymtitlebar_left_btn_image"
    be_vip_button=By.XPATH, "//*[@text='加入超级VIP']"
    @allure.step('我 获取 昵称')
    def get_nick_name_text(self):
        return self.find_element(self.nick_name_text_view).text
    @allure.step('我 点击 设置')
    def click_setting(self):
        self.find_element_with_scroll(self.setting_button).click()
    @allure.step('我 点击 VIP')
    def click_be_vip(self):
        self.find_element_with_scroll(self.be_vip_button).click()
        time.sleep(5)
