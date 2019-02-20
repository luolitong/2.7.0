import sys
import time
sys.path.append("..")
from common import getconfig
from androidbase.base import base


class ProductDetail(base):

    def __init__(self):
        self.con = getconfig.GetCof()
        self.driver = base()

    def from_homepage(self,button_name):
        #从主页跳转
        self.driver.jump()
        self.driver.click_time(self.con.getbutton('button',button_name),20)
        if self.driver.get_text(self.con.getbutton('button','主页快速登录'),20):
            print('跳转成功')
        else:
            print('跳转失败')

    def from_slider_bar(self,button_name):
        #从侧边栏跳转
        self.driver.jump()
        self.driver.click_time(self.con.getbutton('button','用户中心'),20)
        self.driver.click_time(self.con.getbutton('button',button_name),20)
        if self.driver.get_text(self.con.getbutton('button','主页快速登录'),20):
            print('跳转成功')
        else:
            print('跳转失败')

    def close_login_page(self):
        #关闭登录页面
        self.driver.click_time(self.con.getbutton('button','关闭登录'),20)

    def clost_slider_page(self):
        #关闭侧边栏
        #time.sleep(1)
        x_ratio=953/1080
        y_ratio=173/2076
        screen_size=self.driver.driver.get_window_size()
        width=screen_size.get('width')
        height=screen_size.get('height')
        self.driver.driver.tap([(round(width*x_ratio),round(height*y_ratio))],100)

    def from_msg_button(self):
        #通知消息按钮跳转登录
        ProductDetail.from_homepage(self,'通知消息')

    def from_service_button(self):
        #首页客服按钮跳转登录
        ProductDetail.from_homepage(self,'首页客服')

    def from_usecar_button(self):
        #首页立即用车按钮跳转登录
        ProductDetail.from_homepage(self,'立即用车')

    def from_slider_head_pic(self):
        #侧边栏头像按钮跳转登录
        ProductDetail.from_slider_bar(self,'登录头像')

    def from_slider_fastlogin(self):
        #侧边栏快速登录按钮跳转登录
        ProductDetail.from_slider_bar(self,'侧边栏快速登录')

    def from_slider_bamboo_garden(self):
        #侧边栏竹园按钮跳转登录
        ProductDetail.from_slider_bar(self,'盼达竹园')

    def from_slider_travel(self):
        #侧边栏行程按钮跳转登录
        ProductDetail.from_slider_bar(self,'行程')

    def from_slider_wallet(self):
        #侧边栏钱包按钮跳转登录
        ProductDetail.from_slider_bar(self,'钱包')

    def from_slider_peccancy(self):
        #侧边栏违章按钮跳转登录
        ProductDetail.from_slider_bar(self,'违章')

    def from_slider_service(self):
        #侧边栏客服按钮跳转登录
        ProductDetail.from_slider_bar(self,'客服')

    def from_slider_reward(self):
        #侧边栏奖励按钮跳转登录
        ProductDetail.from_slider_bar(self,'奖励')

