from selenium.webdriver.common.by import By
from base.base_action import BaseAction

class ImgPage(BaseAction):
    # //com.yunmall.lc:id/img_close 1
    img_close = By.ID, "com.yunmall.lc:id/img_close"
    def click_img(self):
        self.click(self.img_close)