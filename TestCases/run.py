#-*-coding:utf-8-*-
#@Time      :2019/5/3 0003 00:46
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :run.py
#@Software  :PyCharm Community Edition

import sys
sys.path.append('./') #project跟目录地址
print(sys.path)

import unittest
# from TestCases import test_login
from Common import HTMLTestRunnerNew
from Common import contants
from Common.config import config
from datetime import date

'''
    为一组测试创建TestSuite
    应用unittest的TestSuites特性，可以将不同的测试组成一个逻辑组，然后设置统一的测试套件，并通过一个命令来执行；
    具体通过TestSuites、TestLoader和TestRunner类来实现的；
    我们使用TestSuites类来定义和执行测试套件，将多可测试加到一个测试套件中；
    还用TestLoader和TextTestRunner创建和运行测试套件；
'''
# suite = unittest.TestSuite()
# loader = unittest.TestLoader()
# suite.addTest(loader.loadTestsFromModule(test_login))


now = date.today()
datestr = now.strftime('%m-%d-%y')

class HTMLTestRunner():

    def html_test(self):
        # 使用unittest，调用defaultTestLoader方法，加载discover，用来查询某个文件夹下以test_开头的.py结尾的文件。
        discover = unittest.defaultTestLoader.discover(contants.case_dir,"test_*.py")

        with open(contants.report_dir+'/report{}.html'.format(datestr),'wb+') as file:
            runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                                      title=config.get('HTMLTest','title'),
                                                      description=config.get('HTMLTest','description'),
                                                      tester=config.get('HTMLTest','tester'))
            runner.run(discover)


if __name__ == '__main__':
    htmltestrunner = HTMLTestRunner()
    htmltestrunner.html_test()
