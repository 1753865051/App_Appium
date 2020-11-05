from page.home_page import HomePage
from page.img_page import ImgPage
from page.login_pge import LoginPage
from page.me_page import MePage
from page.register_page import RegistePage


class Page:
    def __init__(self,driver):
        self.driver=driver

    @property
    def home(self):
        return HomePage(self.driver)
    @property
    def img(self):
        return ImgPage(self.driver)
    @property
    def login(self):
        return LoginPage(self.driver)
    @property
    def registe(self):
        return RegistePage(self.driver)
    @property
    def me(self):
        return MePage(self.driver)