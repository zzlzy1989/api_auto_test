#-*-coding:utf-8-*-
#@Time      :2019/5/3 0003 00:46
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :run.py
#@Software  :PyCharm Community Edition


import unittest
# from TestCases import test_login
import HTMLTestRunnerNew
from Common import contants
from Common.config import config

# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_login))

class HTMLTestRunner():
#使用unittest，调用defaultTestLoader方法，加载discover，用来查询某个文件夹下以test_开头的.py结尾的文件。
    def html_test(self):
        discover = unittest.defaultTestLoader.discover(contants.case_dir,"test_*.py")


        with open(contants.report_dir+'/report.html','wb+') as file:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                      title=config.get('HTMLTest','title'),
                                                      description=config.get('HTMLTest','description'),
                                                      tester=config.get('HTMLTest','tester'))
            runner.run(discover)


if __name__ == '__main__':
    htmltestrunner = HTMLTestRunner()
    htmltestrunner.html_test()
