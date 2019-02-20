# -*- coding: utf-8 -*-
import sys
sys.path.append("..")
from pages import product_login
import unittest,time


class Test_panda_login(unittest.TestCase):
    
    @classmethod
    def setUpClass(self):
        driver = product_login.product_detail()
        self.driver=driver

    def test_begin(self):
        time.sleep(10)
        self.driver.login()

    def test_agreement(self):
        #查看用户协议
        self.driver.login_agreement()

    def test_loginph(self):
        #不输入手机号登录
        self.driver.login_ph()

    def test_logincode(self):
        #不输入验证码登录
        self.driver.login_code(13678025855)

    def test_loginag(self):
        #不勾选用户协议登录
        self.driver.login_ag(13678025855)

    def test_loginshort(self):
        #输入手机号码过短
        self.driver.login_num(136780)
        self.driver.login_ex()

    def test_loginerr(self):
        #输入非手机号
        self.driver.login_num(23678025855)
        self.driver.login_ex()

    def test_login(self):
        #输入正确手机号
        self.driver.login_num(13678025855)
        self.driver.login_rg()

    @classmethod
    def tearDownClass(self):
        self.driver.quit()

        
    
if __name__ == "__main__":
    unittest.main()
