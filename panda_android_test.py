# -*- coding:utf-8 -*-

import unittest
import HTMLTestRunner
import time


from testcase.test_login import Test_panda_login


if __name__ == '__main__':



#添加一个测试集合，并添加Case


    suiteTest = unittest.TestSuite()
    #begin
    suiteTest.addTest(Test_panda_login('test_begin'))
    #不输入手机号登录
    suiteTest.addTest(Test_panda_login('test_loginph'))
    #不输入验证码登录
    suiteTest.addTest(Test_panda_login('test_logincode'))
    #不勾选用户协议登录
    suiteTest.addTest(Test_panda_login('test_loginag'))
    #输入手机号码过短
    suiteTest.addTest(Test_panda_login('test_loginshort'))
    #输入非手机号
    suiteTest.addTest(Test_panda_login('test_loginerr'))
    #输入正确手机号
    suiteTest.addTest(Test_panda_login('test_login'))
    
    
    
    
    


    

    
    path = './test_Result/Test_Reports/'
    filename = '-result.html'
    now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    
   # fp = open(path + now + filename, 'wb')
    #runner = HTMLTestRunner.HTMLTestRunner(fp, title=u'My tests', description=u'This is a report test')
    #runner.run(suiteTest)


    with open(path + now + filename, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f,
                                title='Pand Android Test Report',
                                description='V2.4.2 state',
                                verbosity=2
                                )
        runner.run(suiteTest)

