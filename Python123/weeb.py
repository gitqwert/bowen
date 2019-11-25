#!/usr/bin/python
#-*-coding:utf8-*-
import logging
import logging.config
logging.config.fileConfig(r'E:\PYTHOO\rand2\log.conf')

logging.getLogger()


from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
desired_cap={'platformName':'Android',
             'platformVersion':'5.1.1',
             'deviceName':'192.168.10.108:62001',
             'appPackage':'com.tal.kaoyan',
             'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
             'noReset':False}
logging.info('start-app')
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)#驱动这个服务器的路径来识别
driver.implicitly_wait(3)#他叫隐形等待ick()（他是针对全局的）
# #这个是ID
logging.info('skip')
driver.find_element_by_id('com.tal.kaoyan:id/tv_skip').click()#.click()是点击
logging.warning('agree')
driver.find_element_by_id('com.tal.kaoyan:id/tip_commit').click()

#这个是XPath
#driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView').click()
#driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]').click()
# def liu():
#     try:
#         aa=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
#     except:
#         print('no aa')
#     else:
#         aa.click()
# liu()
# def jiao():
#     try:
#         cc=driver.find_element_by_id('com.tal.kaoyan:id/tip_commit')
#     except:
#         print('no cc')
#     else:
#         cc.click()
# jiao()

#xpath
# def lj():
#     try:
#         dd=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')
#     except:
#         print('no dd')
#     else:
#         dd.click()
# lj()
# def jl():
#     try:
#         ee=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]')
#     except:
#         print('no ee')
#     else:
#         ee.click()
# jl()



# from selenium.webdriver.support.ui import WebDriverWait
# from appium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# desired_cap={'platformName':'Android',
#              'platformVersion':'5.1.1',
#              'deviceName':'192.168.10.108:62001',
#              'appPackage':'com.tal.kaoyan',
#              'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
#              'noReset':False,
#              'unicodeKeyboard':True,
#              'resetKeyboard':True}
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)#驱动这个服务器的路径来识别
# WebDriverWait(driver,5).until(lambda x:x.find_element_by_id('com.tal.kaoyan:id/tv_skip')).click()
# WebDriverWait(driver,6).until(lambda x:x.find_element_by_id('com.tal.kaoyan:id/tip_commit')).click()

# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView').click()
# driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]').click()
# def lj():
#     try:
#         dd=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.TextView')
#     except:
#         print('no dd')
#     else:
#         dd.click()
# lj()
# def jl():
#     try:
#         ee=driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.TextView[2]')
#     except:
#         print('no ee')
#     else:f
#         ee.click()
# jl()



# from selenium.webdriver.support.ui import WebDriverWait
# from appium import webdriver
# from selenium.common.exceptions import NoSuchElementException
# desired_cap={'platformName':'Android',
#              'platformVersion':'5.1.1',
#              'deviceName':'192.168.10.108:62001',
#              'appPackage':'com.tal.kaoyan',
#              'appActivity':'com.tal.kaoyan.ui.activity.SplashActivity',
#              'noReset':False,
#              'unicodeKeyboard':True,
#              'resetKeyboard':True}
# driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_cap)#驱动这个服务器的路径来识别
# driver.implicitly_wait(3)#他叫隐形等待ick()（他是针对全局的）
# def liu():
#     try:
#         aa=driver.find_element_by_id('com.tal.kaoyan:id/tv_skip')
#     except:
#         pass
#     else:
#         aa.click()
#
# def jiao():
#     try:
#         cc=driver.find_element_by_id('com.tal.kaoyan:id/tip_commit')
#     except:
#         pass
#     else:
#         cc.click()
# liu()
# jiao()

# #Name 定位
# #from find_element.capability import driver
#driver.find_element_by_class_name('android.widget.EditText').clean()
# driver.find_element_by_class_name('android.widget.EditText').send_keys('L13173348702')
# driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('L123456')
# driver.find_element_by_class_name('android.widget.Button').click()




#例子
# def ff():
#     driver.find_element_by_android_uiautomator('new UiSelector().className("android.widget.EditText")').send_keys('L13173348702')
#     driver.find_element_by_android_uiautomator('new UiSelector().id("com.tal.kaoyan:id/activity_register_password_edittext")').send_keys('L123456')
#     driver.find_element_by_android_uiautomator('')


# from appium import webdriver
# import yaml
# from selenium.common.exceptions import NoSuchElementException
# import logging


from  selenium import webdriver