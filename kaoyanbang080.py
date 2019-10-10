# 安装客户端包 Appium-Python-Client (pip3 install)
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Applogin(object):

    def __init__(self):
        cap = {
            "platformName": "Android",
            "platformVersion": "4.4.2",
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.tal.kaoyan",
            "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
            "noReset": True
        }

        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)  # 链接appium-->控制模拟器

    def app_login(self):
        try:
            # 是否有跳过
            if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']")):
                self.driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_skip']").click()
        except:
            pass
        try:
            if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")):
                # 定位用户名
                login_name = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_email_edittext']")
                login_name.send_keys("kaoyanbang080")  # 输入用户名
                # 定位密码
                login_pwd = self.driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/login_password_edittext']")
                login_pwd.send_keys("kaoyanbang080")  # 输入密码
                time.sleep(0.5)
                # 定位登陆按钮
                sign = self.driver.find_element_by_xpath("//android.widget.Button[@resource-id='com.tal.kaoyan:id/login_login_btn']")
                sign.click()  # 点击登陆按钮
        except:
            pass

        # 定位 <研讯> 标签
        if WebDriverWait(self.driver, 3).until(lambda x: x.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")):
            yanxun = self.driver.find_element_by_xpath("//android.support.v7.widget.RecyclerView[@resource-id='com.tal.kaoyan:id/date_fix']/android.widget.RelativeLayout[3]/android.widget.LinearLayout[1]/android.widget.ImageView[1]")
            yanxun.click()  # 点击 研讯

        time.sleep(1)
        l = self.get_size()
        # 定位鼠标位置
        x1 = int(l[0] * 0.5)  # 宽度--放在哪
        y1 = int(l[1] * 0.75)  # 高度--从哪里开始滑动
        y2 = int(l[1] * 0.25)  # 高度--滑动到哪个位置
        # 循环滑动
        while True:
            self.driver.swipe(x1, y1, x1, y2)  # 放在哪，从哪开始滑动，沿着什么方向，滑动到呢
            time.sleep(1)

    def get_size(self):  
        x = self.driver.get_window_size()['width']  # 获取宽
        y = self.driver.get_window_size()['height']  # 获取高
        return (x,y)


if __name__ == '__main__':
    app = Applogin()
    app.app_login()




