from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from appium import webdriver
import time



class base(object):
    '''usually method'''
    #if __name__ == "__main__":
    #unittest.main(verbosity=2)
    #加入 --quiet 参数 等效于 verbosity=0
#加入--verbose参数等效于 verbosity=2
#什么都不加就是 verbosity=1
    #启动APPIUM
    #eg = base.base({
    #'platformName':'Android',
    #'deviceName':'d52ad83c',
    #'platformVersion':'5.0',
    #'appPackage':'com.panda.usecar',
    #'appActivity':'com.panda.usecar.mvp.ui.main.MainActivity'
    #})
    #eg.find_element(xxx)
    #eg.wait(xxx)
    #首页跳过com.panda.usecar:id/bt_jump
    #首页跳转com.panda.usecar:id/iv_spash
    #首次登录com.panda.usecar:id/iv
    #首页小广告com.panda.usecar:id/rv_ad
    #差掉小广告com.panda.usecar:id/iv_cancel
    #小广告返回com.panda.usecar:id/back
    #侧边条com.panda.usecar:id/tv_operation_before
    #com.panda.usecar:id/tv_operation_area
    #com.panda.usecar:id/iv_close_operation
    def __init__(self):
        '''创建实例'''
        #driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',{
            'platformName':'Android',
            'deviceName':'98895a314f4e505252',
            'platformVersion':8.0,
            'appPackage':'com.panda.usecar',
            'appActivity':'com.panda.usecar.mvp.ui.main.MainActivity',
            'automationName': 'Uiautomator2',
            'noReset':'True',
            'autoGrantPermissions':'True',
            'unicodeKeyboard': 'True'
            })
        self.driver=driver


    def find_element(self,element,time):
        '''超时等待'''
        '''WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(driver.find_element_by_id('com.panda.usecar:id/slide_bar')))'''
        
        try:
            if element:
                
                idx = element.index('=')
                by = element[:idx]
                value = element[idx + 1:]
                ele = WebDriverWait(self.driver,time).until(lambda driver:driver.find_element(by=by,value=value))
                return ele
            else:
                raise NameError('Please input element.')
        except Exception as e:
            print(e)

    
    def wait(self, seconds):
        """
        Implicitly wait.All elements on the page.
        :param seconds:
        :return:None
        Usage:
        driver.wait(5)
        """
        if seconds > 0:
            self.driver.implicitly_wait(seconds)
        else:
            raise NameError('Seconds must greater than 0.')

    def click(self, element):
        """driver.find_element_by_id(com.panda.usecar:id/tv_save).click()"""
        self.driver.find_element_by_id(element).click()


    def click_time(self, element, time):
        """
        :param element:
        :return:
        """
        self.find_element(element, time).click()

    def click_path(self, element):
        '''driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "111")]').click()  '''
        self.driver.find_element_by_xpath(element).click()

    def swipe3(self,x,y,xx,yy,ms):
        size=self.driver.get_window_size()
        wi=size.get('width')/1080
        he=size.get('height')/1920
        try:
            x1=int(x*wi)
            y1=int(y*he)
            xx1=int(xx*wi)
            yy1=int(yy*he)       
            self.driver.swipe(x1,y1,xx1,yy1,ms)
        except:
            print('坐标异常')

    def width(self):
        size=self.driver.get_window_size()
        wi=size.get('width')
        print(wi)
        return wi

    def swipe(self,x,y,xx,yy,ms):
        self.driver.swipe(x,y,xx,yy,ms)

    def swipe2(self,x,y,xx,yy,ms):
        self.driver.swipe(x,y,xx,yy,ms)

    def get_attribute(self,element,time,name):
        #tag = self.driver.find_element_by_id(ele).get_attribute(name)
        tag = self.find_element(element, time).get_attribute(name)
        return tag

    def get_text(self,element,time):
        tap = self.find_element(element, time).text
        return tap

    def get_text_xpath(self,ele):
        tap = self.driver.find_element_by_xpath(ele).text
        return tap

 

    def quit(self):
        """
        Quit the driver and close all the windows.
        :return:None
        """
        self.driver.quit()

    def send(self,element, time,key):
        '''driver.find_element_by_id('com.panda.usecar:id/et_phone').send_keys('13678025855')'''
        self.find_element(element, time).send_keys(key)


    def jump(self):
        '''跳过首页那些有的没的'''
        
        try:
            self.driver.find_element_by_id('com.panda.usecar:id/bt_jump').click()
        except:
            time.sleep(5)

        try:
            self.driver.find_element_by_id('com.panda.usecar:id/iv_cancel').click()
        except:
            pass

        try:
            self.driver.find_element_by_id('com.panda.usecar:id/iv_close').click()
        except:
            pass

    def location(self):
        try:
            self.driver.find_element_by_id('com.panda.usecar:id/location').click()
        except:
            print(',')

    def refresh(self):
        self.driver.find_element_by_id('com.panda.usecar:id/iv_refresh').click()

    def clear(self,ele):
        self.driver.find_element_by_id(ele).clear()

    def wLogging(self,log):    
        self.path = './test_Result/Test_logs/'
        self.now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
        self.filename = '-Tests_log.log'
        self.logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s wLog: %(levelname)s [** %(message)s **]',
            datefmt='%Y-%m-%d %H:%M:%S',
            filename=path + now + filename,
            filemode='w')
        self.logging.info(log)
        

    
        
