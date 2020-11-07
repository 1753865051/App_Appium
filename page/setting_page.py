from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class SettingPage(BaseAction):
    about_button=By.XPATH, "//*[@text='关于百年奥莱']"

    cleat_cache_button=By.XPATH, "//*[@text='清理缓存']"
    address_list_button=By.XPATH, "//*[@text='地址管理']"
    def click_about(self):
        self.find_element_with_scroll(self.about_button).click()


    def click_cleat_cache(self):
        self.find_element_with_scroll(self.cleat_cache_button).click()

    def click_address_list(self):
        self.find_element_with_scroll(self.address_list_button).click()