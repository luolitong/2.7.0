import sys
sys.path.append("..")
from pages import product_prelogin
import unittest,time


class TestJumpLogin(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        driver =product_prelogin.ProductDetail()
        self.driver = driver


    def test_from_msg_button(self):
        # 通知消息按钮跳转登录
        self.driver.from_msg_button()
        self.driver.close_login_page()

    def test_from_service_button(self):
        # 首页客服按钮跳转登录
        self.driver.from_service_button()
        self.driver.close_login_page()

    def test_from_use_car_button(self):
        #首页立即用车按钮跳转登录
        self.driver.from_usecar_button()
        self.driver.close_login_page()

    def test_from_slider_head_pic(self):
        #侧边栏头像跳转登录
        self.driver.from_slider_head_pic()
        self.driver.close_login_page()
        self.driver.clost_slider_page()

    def test_from_slider_fastlogin(self):
        #侧边栏快速登录按钮跳转登录
        self.driver.from_slider_fastlogin()
        self.driver.close_login_page()
        self.driver.clost_slider_page()

    def test_from_slider_bamboo_garden(self):
        # 侧边栏竹园按钮跳转登录
        self.driver.from_slider_bamboo_garden()
        self.driver.close_login_page()
        self.driver.clost_slider_page()

    def test_from_slider_travel(self):
        #侧边栏行程按钮跳转登录
        self.driver.from_slider_travel()
        self.driver.close_login_page()
        self.driver.clost_slider_page()

    def test_from_slider_wallet(self):
        #侧边栏钱包按钮跳转登录
        self.driver.from_slider_wallet()
        self.driver.close_login_page()
        self.driver.clost_slider_page()

    def test_from_slider_peccancy(self):
        #侧边栏违章按钮跳转登录
        self.driver.from_slider_peccancy()
        self.driver.close_login_page()
        self.driver.clost_slider_page()

    def test_from_slider_service(self):
        #侧边栏客服按钮跳转登录
        self.driver.from_slider_service()
        self.driver.close_login_page()
        self.driver.clost_slider_page()

    def test_from_slider_reward(self):
        #侧边栏奖励按钮跳转登录
        self.driver.from_slider_reward()
        self.driver.close_login_page()
        self.driver.clost_slider_page()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
