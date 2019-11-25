#!/usr/bin/python
#-*-coding:utf8-*-
# import yaml
# aa={'name':'liu','age':21}
# cc=['yo','tt']
# print(yaml.dump(aa))
# print(yaml.dump(cc))






# import os
# import time
# import unittest
# from rand.HTMLTestRunner import HTMLTestRunner
#
# #测试用例的路径
# case_path=r'E:\PYTHOO\rand2'
# #discover测试集
# discover=unittest.defaultTestLoader.discover(case_path,pattern='capab*.py')
#
# if __name__== '__main__':
#     #获取现在时间
#     now=time.strftime('%Y %m %d %H %M %S')
#     #放报告的路径
#     report=r'E:\PYTHOO\eport1'
#     report_name=os.path.join(report,'%s.html'%(now))
#     with open(report_name,'wb') as file:
#         runner=HTMLTestRunner(stream=file,title=u'测试报告',
#                               description=u'用例执行情况如下：',
#                               tester=u'皮皮',verbosity=2)  #0是不显示报告，1显示的不详细，2显示的最详细
#         run=HTMLTestRunner()
#         runner.run(discover)
