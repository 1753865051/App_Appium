import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page

class TestAddress:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    #地址管理
    @pytest.mark.parametrize("args",analyze_file("address_data.yaml","test_add_address"))
    def test_add_address(self,args):
        name=args["name"]
        phone=args["phone"]
        info=args["info"]
        post_code=args["post_code"]
        toast=args["toast"]
        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_address_list()
        self.page.address_list.click_add_address()
        self.page.edit_address.input_name(name)
        self.page.edit_address.input_phone(phone)
        self.page.edit_address.input_info(info)
        self.page.edit_address.input_post_code(post_code)
        self.page.edit_address.click_default_address()
        self.page.edit_address.choose_region()
        self.page.edit_address.click_save()
        if toast is None:
            assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % (name, phone),"保存成功"
        else:
            assert self.page.edit_address.is_toast_exist(toast),"保存失败"
        # assert self.page.address_list.get_default_receipt_name_text() == "%s  %s" % ("利亚东",12345678901)
    @pytest.mark.parametrize("args",analyze_file("address_data2.yaml","test_update_address"))
    def test_edit_address(self,args):
        name=args["name"]
        phone=args["phone"]
        info=args["info"]
        post_code=args["post_code"]
        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_address_list()
        if not self.page.address_list.is_default_feature_exit():
            self.page.address_list.click_add_address()
            self.page.edit_address.input_name(name)
            self.page.edit_address.input_phone(phone)
            self.page.edit_address.input_info(info)
            self.page.edit_address.input_post_code(post_code)
            self.page.edit_address.click_default_address()
            self.page.edit_address.choose_region()
            self.page.edit_address.click_save()
        self.page.address_list.click_default_address()
        self.page.edit_address.input_name(name)
        self.page.edit_address.input_phone(phone)
        self.page.edit_address.input_info(info)
        self.page.edit_address.input_post_code(post_code)
        self.page.edit_address.choose_region()
        self.page.edit_address.click_save()
        assert self.page.address_list.is_toast_exist("成功")

    def test_delete_address(self):
        self.page.home.login_if_not(self.page)
        self.page.me.click_setting()
        self.page.setting.click_address_list()
        assert self.page.address_list.is_default_feature_exit(), "没有地址可删除的"
        for i in range(10):
            self.page.address_list.click_edit()
            if not self.page.address_list.is_delete_exit():
                break
            self.page.address_list.click_delete()
            self.page.address_list.click_commit()

        self.page.address_list.click_edit()
        assert not self.page.address_list.is_delete_exit(), "还没删完"




