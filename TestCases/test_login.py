#-*-coding:utf-8-*-
#@Time      :2019/5/1 0001 23:19
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :test_login.py
#@Software  :PyCharm Community Edition

import unittest
from Common.http_request import HttpRequestSession
from Common import do_excel
from Common import contants
from ddt import ddt,data
from Common import do_mysql
from Common import logger

logger = logger.get_logger(__name__)

"""
登录测试用例，使用unittest
cases.xlsx文件中login
"""
@ddt
class LoginTest(unittest.TestCase):
    # contants为文件路径，获取文件的路径，login为excel的sheet
    excel = do_excel.DoExcel(contants.case_file, 'login')
    cases = excel.get_cases()

    #使用DDT的时候不能使用setUP,需要使用@classmethod
    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置:test_recharge')
        cls.http_request = HttpRequestSession()
        cls.mysql = do_mysql.DoMysql()

    #data可接受字典，元祖，列表等等
    @data(*cases)
    def test_login(self,case):
        logger.info('开始测试:{}'.format(case.title))
        logger.info('测试用例入参:{}'.format(case.data))
        print('开始测试:{}'.format(case.title))
        print('测试用例入参:{}'.format(case.data))

        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id + 1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAILED')
            logger.error('ERROR:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
        cls.mysql.close()
