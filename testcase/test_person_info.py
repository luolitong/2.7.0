import sys
sys.path.append("..")
from pages import product_person_info
import unittest,time


class TestPersonInfo(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        driver=product_person_info.ProductPersonInfo()
        self.driver=driver

    def test_change_head_pic(self):
        #更换头像
        self.driver.change_head_pic()
        self.driver.back_to_homepage(1)

    def test_change_nickname(self):
        #更换昵称（合法昵称）
        self.driver.change_nick_name("测试昵称",True)
        self.driver.back_to_homepage(1)

    def test_change_nickname_illegal(self):
         # 更换昵称（非法昵称）
        self.driver.change_nick_name("测试昵称$@#$@#.",False)
        self.driver.back_to_homepage(2)

    def test_change_email(self):
        #更换邮箱地址（合法）
        self.driver.change_email_address("12345@qq.com",True)
        self.driver.back_to_homepage(1)

    def test_change_email_illegal(self):
        #更换邮箱地址（非法）
        self.driver.change_email_address("12345@qq.￥@#￥@￥@com",False)
        self.driver.back_to_homepage(2)

    def test_auth_process_is_authorization(self):
        #用户已认证
        self.driver.auth_process()
        self.driver.back_to_homepage(1)

    def test_auth_process_not_authorization(self):
        #用户未认证
        self.driver.auth_process()
        #self.driver.back_to_homepage(1)
    @classmethod
    def tearDownClass(self):
        self.driver.quit()