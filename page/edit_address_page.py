import random
import time

from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class EditAddressPage(BaseAction):
    #收件人
    name_edit_text = By.ID, "com.yunmall.lc:id/address_receipt_name"
    #手机号
    phone_edit_text = By.ID, "com.yunmall.lc:id/address_add_phone"
    #详细地址
    info_edit_text = By.ID, "com.yunmall.lc:id/address_detail_addr_info"
    #邮编
    post_code_edit_text = By.ID, "com.yunmall.lc:id/address_post_code"
    # 设置默认地址
    default_address_button = By.ID, "com.yunmall.lc:id/address_default"
    #所在地区com.yunmall.lc:id/address_province
    region_button = By.ID, "com.yunmall.lc:id/address_province"
    #省市区
    area_featuer=By.ID, "com.yunmall.lc:id/area_title"
    save_button=By.XPATH, "//*[@text='保存']"
    def input_name(self, text):
        self.input(self.name_edit_text, text)
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)
    def input_info(self, text):
        self.input(self.info_edit_text, text)
    def input_post_code(self, text):
        self.input(self.post_code_edit_text, text)
    def click_default_address(self):
        self.click(self.default_address_button)
    def click_region(self):
        self.click(self.region_button)
    def choose_region(self):
        self.click_region()
        time.sleep(1)
        while True:
            if self.driver.current_activity != "com.yunmall.ymctoc.ui.activity.ProvinceActivity":
                return
            areas=self.find_elements(self.area_featuer)
            areas_count=len(areas)
            area_index=random.randint(0,areas_count-1)
            areas[area_index].click()
            time.sleep(1)
    def click_save(self):
        self.click(self.save_button)