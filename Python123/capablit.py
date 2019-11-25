#!/usr/bin/python
#-*-coding:utf8-*-
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
# driver.find_element_by_xpath('//android.widget.EditText[@text="请输入用户名"]').send_keys('L13173348702')


# driver.find_element_by_xpath('//com.tal.kaoyan:id/login_password_edittext').send_keys('L123456')
# driver.find_element_by_xpath('//android.widget.Button[@text="登录"]').click()






# from rand2.weeb import driver
# from time import *
# # driver.find_element_by_class_name('android.widget.EditText').send_keys('L13173348702')
# # driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('L123456')
# # driver.find_element_by_class_name('android.widget.Button').click()
# def zhu_ce():
#     driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
#     sleep(3)
#     aa=driver.find_elements_by_id('com.tal.kaoyan:id/check')
#     aa[1].click()
#     driver.find_element_by_id('com.tal.kaoyan:id/picture_tv_ok').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/menu_crop').click()
#
#
# def deng_lu():
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys('Liuehduijpfy')
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys('AA123434689')
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys('2630835427@qq.com')
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
# def zi_liao():
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_time').click()
#     driver.find_element_by_id('android:id/text1').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/major_subject_title').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/major_search_item_name').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_school').click()
# #     #driver.tap([(),()],100)#100ms点一次
# zhu_ce()
# deng_lu()
# zi_liao()


#
# from rand2.weeb import driver
# from time import *
# driver.find_element_by_class_name('android.widget.EditText').send_keys('L13173348702')
# driver.find_element_by_id('com.tal.kaoyan:id/login_password_edittext').send_keys('L123456')
# driver.find_element_by_class_name('android.widget.Button').click()

# def zhu_ce():
#     driver.find_element_by_id('com.tal.kaoyan:id/login_register_text').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_userheader').click()
#     sleep(3)
#     aa=driver.find_elements_by_id('com.tal.kaoyan:ideck')
#     aa[1].click()
#     driver.find_element_by_id('com.tal.kaoyan:id/picture_tv_ok').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/menu_crop').click()
#
#
# def deng_lu():
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_username_edittext').send_keys('Liudglkijfy')
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_password_edittext').send_keys('AA12345689')
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_email_edittext').send_keys('2630845427@qq.com')
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_register_register_btn').click()
# def zi_liao():
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_time').click()
#     driver.find_element_by_id('android:id/text1').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_major').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/major_subject_title').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/major_search_item_name').click()
#     driver.find_element_by_id('com.tal.kaoyan:id/activity_perfectinfomation_school').click()
# zhu_ce()
# deng_lu()
# zi_liao()










#unittest
# import unittest
# class Study(unittest.TestCase):    #这个是一个基本类 所有的用例都继承他
#
#     @classmethod  #装饰符
#     def setUpClass(cls):  #所有的用例执行之前且只执行一次（先执行他）
#         print('第一')
#
#     @classmethod
#     def tearDownClass(cls):   #所有的用例执行之后且只执行一次（先执行他）
#         print('最后')
#
#     def test01(self):
#         print('我执行了test01')
#
#     def test02(self):
#         print('我执行了test02')
#
# if __name__== '__main__':  #
#     unittest.main()    #





#
# import unittest
# class Study(unittest.TestCase):    #这个是一个基本类 所有的用例都继承他
#     def setUp(self):  #每条用例执行之前执行一次
#         print('assddd11')
#
#     def tearDown(self):  #每条用例执行之后执行一次
#         print('sdfgh13')
#     @unittest.skip  #跳过这个用例不执行他
#
#     def test01(self):
#         print('我执行了test01')
#
#     def test02(self):
#         print('我执行了test02')
#
# if __name__== '__main__':  #
#     unittest.main()    #
