import time
import sys
sys.path.append("..")
from common import getconfig
from common import util
from androidbase.base import base
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class ProductPersonInfo(base):

    def __init__(self):
        self.con = getconfig.GetCof()
        self.driver = base()

    def tap_complete_choose_btn(self):
        #点击完成选择头像
        util.Util.tap_coordinate(810,2004)

    def tap_cancel_change_btn(self):
        #取消选择头像
        util.Util.tap_coordinate(269,2004)

    def back_to_homepage(self,page_class):
        #正常情况
        if page_class==1:
            self.driver.click_time('button','返回',20)
        elif page_class==2:
            self.driver.click_time('button','返回',20)
            self.driver.click_time('button','返回',20)



    def change_head_pic(self,test_kind):
        #更换头像
        self.driver.click_time(self.con.getbutton('button','用户中心'),20)
        self.driver.click_time(self.con.getbutton('button','登录头像'),20)
        self.driver.click_time(self.con.getbutton('button', '登录头像'), 20)
        self.driver.click_time(self.con.getbutton('button', '拍照'), 20)
        try:
            self.driver.driver.find_elements_by_class_name('GLButton')[5].click()
        except:
            self.driver.driver.find_elements_by_class_name('GLButton')[5].click()
        self.driver.click_time(self.con.getbutton('button','相机确定'),20)
        if test_kind=='complete':
            self.tap_complete_choose_btn()
        elif test_kind=='cancel':
            self.tap_cancel_change_btn()

    def change_nick_name(self,name,name_type):
        self.driver.click_time(self.con.getbutton('button', '用户中心'), 20)
        self.driver.click_time(self.con.getbutton('button', '登录头像'), 20)
        self.driver.click_time(self.con.getbutton('button','昵称'),20)
        self.driver.send(self.con.getbutton('button','昵称文本框'),5,name)
        self.driver.click_time(self.con.getbutton('button', '保存昵称'),20)
        nickname=self.driver.get_text(self.con.getbutton('button','昵称展示'),5)
        if name_type:
            if nickname==name:
                print('更换昵称成功\n')
        else:
            if self.driver.driver.page_source.find("保存")!=-1:
                print('昵称含有非法字符，未保存成功\n')

    def change_email_address(self,address,address_type):
        self.driver.click_time(self.con.getbutton('button', '用户中心'), 20)
        self.driver.click_time(self.con.getbutton('button', '登录头像'), 20)
        self.driver.click_time(self.con.getbutton('button', '邮箱'), 20)
        self.driver.send(self.con.getbutton('button', '昵称文本框'), 5, address)  #邮箱与昵称文本框公用id
        self.driver.click_time(self.con.getbutton('button', '保存昵称'), 20)      #id公用
        if address_type:
            email=self.driver.get_text(self.con.getbutton('button','邮箱展示'),5)
            if email==address:
                print('更换邮箱地址成功\n')
        else:
            # e1=WebDriverWait(self.driver,20,0.01).until(EC.presence_of_element_located((By.XPATH,'.//*[contains(@text,"请输入正确的邮箱格式")]'))) #获取toast位置
            # print(e1.text)
            if self.driver.driver.page_source.find("保存")!=-1:
                print('邮箱地址含有非法字符，未保存成功\n')



    def auth_process(self):
        self.driver.click_time(self.con.getbutton('button', '用户中心'), 20)
        self.driver.click_time(self.con.getbutton('button', '登录头像'), 20)
        auth_status=self.driver.get_text(self.con.getbutton('button','认证状态'),5)
        #print(auth_status)
        if auth_status=='未认证':
            self.driver.click_time(self.con.getbutton('button','认证'),5)
            time.sleep(2)
            self.driver.driver.find_element_by_xpath(
                "//*[@class='android.widget.ImageView' and @index='1'] ").click() #身份证正面
            #self.driver.click_time(self.con.getbutton('button','身份证背面'),20)
            #self.driver.click_time(self.con.getbutton('button','身份证拍照'),20)
            self.driver.driver.find_element_by_xpath(
                "//*[@class='android.widget.Button' and @index='0']").click()   #身份证拍照
            self.driver.click_time(self.con.getbutton('button','使用照片'),20)
            print('拍摄身份证正面成功\n')
            self.driver.driver.find_element_by_xpath(
                "//*[@class='android.widget.ImageView' and @index='3'] ").click() #身份证背面
            self.driver.driver.find_element_by_xpath(
                "//*[@class='android.widget.Button' and @index='0']").click()     #身份证拍照
            self.driver.click_time(self.con.getbutton('button', '使用照片'), 20)
            print('拍摄身份证背面成功\n')
            self.driver.click_time(self.con.getbutton('button','身份证下一步'),20)
            time.sleep(2)
            self.driver.driver.find_element_by_xpath(
                "//*[@class='android.widget.ImageView' and @index='2']").click()   #驾驶证首页
            self.driver.driver.find_element_by_xpath(
                "//*[@class='android.widget.Button' and @index='0']").click()     #驾驶证拍照
            self.driver.click_time(self.con.getbutton('button', '使用照片'), 20)
            print('拍摄驾驶证首页成功\n')
            self.driver.driver.find_element_by_xpath(
                "//*[@class='android.widget.ImageView' and @index='4']").click()   #驾驶证副页
            self.driver.driver.find_element_by_xpath(
                "//*[@class='android.widget.Button' and @index='0']").click()  # 驾驶证拍照
            self.driver.click_time(self.con.getbutton('button', '使用照片'), 20)
            print('拍摄驾驶证副页成功\n')
            self.driver.click_time(self.con.getbutton('button','提交认证'),20)
            print('完成认证流程\n')
        elif auth_status=='已认证':
            print('该用户已认证\n')