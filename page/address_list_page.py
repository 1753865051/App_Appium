from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class AddressListPage(BaseAction):

    #地址新增
    add_address_button=By.ID, "com.yunmall.lc:id/address_add_new_btn"
    #默认姓名电话
    default_receipt_name_text_view=By.ID,"com.yunmall.lc:id/receipt_name"

    is_default_feature = By.ID, "com.yunmall.lc:id/address_is_default"
    edit_button=By.XPATH, "//*[@text='编辑']"
    delete_button = By.XPATH, "//*[@text='删除']"
    commit_button = By.XPATH, "//*[@text='确认']"
    def click_add_address(self):
        self.find_element_with_scroll(self.add_address_button).click()
    def get_default_receipt_name_text(self):
        return self.get_text(self.default_receipt_name_text_view)
    def is_default_feature_exit(self):
        return self.is_feature_exit(self.is_default_feature)
    def is_delete_exit(self):
        return self.is_feature_exit(self.delete_button)
    def click_default_address(self):
        self.click(self.is_default_feature)
    def click_edit(self):
        self.click(self.edit_button)
    def click_delete(self):
        self.click(self.delete_button)
    def click_commit(self):
        self.click(self.commit_button)