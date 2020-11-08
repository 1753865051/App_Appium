import time

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page
import pytest

class TestSearch:
    def setup(self):
        self.driver=init_driver()
        self.page=Page(self.driver)
    def teardown(self):
        time.sleep(1)
        self.driver.quit()

    @pytest.mark.parametrize("args",analyze_file("seatch_data.yaml","test_search"))
    def test_search(self,args):
        ketword=args["keyword"]
        self.page.home.login_if_not(self.page)
        self.page.home.click_home()
        self.page.home.click_search()
        self.page.search.input_keyword(ketword)
        self.page.search.click_search()
        time.sleep(1)
        self.page.search.press_back()
        time.sleep(1)
        assert self.page.search.is_keyword_exist(ketword)
    def test_search_del(self):
        self.page.home.login_if_not(self.page)
        self.page.home.click_home()
        self.page.home.click_search()
        self.page.search.input_keyword()
        self.page.search.click_search()
        time.sleep(1)
        self.page.search.press_back()
        self.page.search.click_search_del()
        assert self.page.search.is_search_record_empty()