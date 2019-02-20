# -*- coding: utf-8 -*-
from pages import producte
import unittest,time

class Test_panda_login(unittest.TestCase):

    def setUp(self):
        driver = producte.product_detail()
        self.driver=driver

    def test_start(self):
        time.sleep(10)
        self.driver.login()




'''class product_detail(base.base):
    def __init__(self):
        driver = base.base(desired_caps)
        self.driver = dirver

    def login(self, time):
        self.driver.click_time('id=com.panda.usecar:id/slide_bar',20)
        self.driver.click_time('com.panda.usecar:id/ll_way',20)'''

        
    
if __name__ == "__main__":
    unittest.main()
