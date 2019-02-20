# -*- coding: utf-8 -*-
import os
import sys
#sys.path.append(os.path.abspath(os.path.dirname(__file__)+'/'+'..'))
sys.path.append("..")
from common import getconfig
from androidbase.base import base


class product_detail(base):
    def __init__(self):
        self.con = getconfig.GetCof()
        self.driver = base()
        

    def login(self):
        self.driver.click_time(self.con.getbutton('button','侧边栏'),20)
        try:
            self.driver.get_text(self.con.getbutton('button','快速登录'),20) == '快速登录'
            self.driver.click_time(self.con.getbutton('button','快速登录'),20)
            self.driver.click_time(self.con.getbutton('button','关闭登录'),20)
        except:
            print('请退出登录')

    def login_agreement(self):
        #查看用户协议
        self.driver.click_time(self.con.getbutton('button','快速登录'),20)
        try:
            self.driver.click_time(self.con.getbutton('button','查看用户协议'),20)
            self.driver.click_time(self.con.getbutton('button','返回'),20)
        except:
            print('查看用户协议失败')
        try:
            self.driver.click_time(self.con.getbutton('button','查看隐私政策'),20)
            self.driver.click_time(self.con.getbutton('button','返回'),20)
        except:
            print('查看隐私政策失败')
        self.driver.click_time(self.con.getbutton('button','关闭登录'),20)
        
    def login_ph(self):
        #不输入手机号登录
        self.driver.click_time(self.con.getbutton('button','快速登录'),20)
        if self.driver.get_text(self.con.getbutton('button','账号栏'),20) == '请输入手机号':
            pass
        else:
            self.driver.click_time(self.con.getbutton('button','清除账号'),20)
        #self.driver.send(self.con.getbutton('button','账号栏'),20,key)
        self.driver.send(self.con.getbutton('button','输入验证码'),20,1111)
        self.driver.click_time(self.con.getbutton('button','用户协议'),20)
        self.driver.click_time(self.con.getbutton('button','登录'),20)
        try:
            self.driver.click_time(self.con.getbutton('button','关闭登录'),20)
        except:
            print('不输入手机号登录')

    def login_code(self,key):
        #不输入验证码登录
        self.driver.click_time(self.con.getbutton('button','快速登录'),20)
        if self.driver.get_text(self.con.getbutton('button','账号栏'),20) == '请输入手机号':
            pass
        else:
            self.driver.click_time(self.con.getbutton('button','清除账号'),20)
        self.driver.send(self.con.getbutton('button','账号栏'),20,key)
        #self.driver.send(self.con.getbutton('button','输入验证码'),20,1111)
        self.driver.click_time(self.con.getbutton('button','用户协议'),20)
        self.driver.click_time(self.con.getbutton('button','登录'),20)
        try:
            self.driver.click_time(self.con.getbutton('button','关闭登录'),20)
        except:
            print('不输入验证码登录')

    def login_ag(self,key):
        #不勾选用户协议
        self.driver.click_time(self.con.getbutton('button','快速登录'),20)
        if self.driver.get_text(self.con.getbutton('button','账号栏'),20) == '请输入手机号':
            pass
        else:
            self.driver.click_time(self.con.getbutton('button','清除账号'),20)
        self.driver.send(self.con.getbutton('button','账号栏'),20,key)
        self.driver.send(self.con.getbutton('button','输入验证码'),20,1111)
        #self.driver.click_time(self.con.getbutton('button','用户协议'),20)
        self.driver.click_time(self.con.getbutton('button','登录'),20)
        try:
            self.driver.click_time(self.con.getbutton('button','关闭登录'),20)
        except:
            print('不勾选用户协议')

    def login_num(self,key):
        self.driver.click_time(self.con.getbutton('button','快速登录'),20)
        if self.driver.get_text(self.con.getbutton('button','账号栏'),20) == '请输入手机号':
            pass
        else:
            self.driver.click_time(self.con.getbutton('button','清除账号'),20)
        self.driver.send(self.con.getbutton('button','账号栏'),20,key)
        self.driver.send(self.con.getbutton('button','输入验证码'),20,1111)
        self.driver.click_time(self.con.getbutton('button','用户协议'),20)
        self.driver.click_time(self.con.getbutton('button','登录'),20)

    def login_ex(self):
        self.driver.click_time(self.con.getbutton('button','关闭登录'),20)

    def login_rg(self):
        self.driver.click_time(self.con.getbutton('button','侧边栏'),20)
        if self.driver.get_text(self.con.getbutton('button','快速登录'),20) == '快速登录':
            print('登录失败')
        else:
            print('登录成功')
        



