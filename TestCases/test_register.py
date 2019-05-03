#-*-coding:utf-8-*-
#@Time      :2019/5/1 0001 23:50
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :test_registe.py
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
注册，使用unittest
"""
@ddt
class RegisterTest(unittest.TestCase):
    # contants为文件路径，获取文件的路径，login为excel的sheet
    excel = do_excel.DoExcel(contants.case_file, 'register')
    cases = excel.get_cases()

    #使用DDT的时候不能使用setUP,需要使用@classmethod
    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置:test_recharge')
        cls.http_request = HttpRequestSession()
        cls.mysql = do_mysql.DoMysql()

    #data可接受字典，元祖，列表等等
    @data(*cases)
    def test_register(self,case):

        #加入日志
        logger.info('开始测试:{}'.format(case.title))
        logger.info('测试用例入参:{}'.format(case.data))
        print('开始测试:{}'.format(case.title))
        print('测试用例入参:{}'.format(case.data))

        #判断register_mobile是否存在在case.data中
        if case.data.find('register_mobile') > -1:
            # sql = 'SELECT max(MobilePhone) from future.member'  # 查询最大手机号
            sql = eval(case.sql)['sql1']  # 转换成字典，使用eval
            logger.info("注册查询当前最大的手机号:{}".format(sql))
            max_phone = self.mysql.fetch_one(sql)['MobilePhone']
            # 最大手机号+1
            max_phone = int(max_phone) + 1
            print('最大手机号码 ',max_phone)
            #replace方法是替换之后，重新返回新的字符串，重新赋值
            case.data = case.data.replace('register_mobile', str(max_phone))  # 替换参数值

        # 判断是否需要进行数据库数据验证
        if case.sql is not None:
            # 从case中获取sql，转化成字典，并根据key值获取sql内容
            sql = eval(case.sql)['sql1']  # 转换成字典，使用eval
            logger.info("注册查询当前最大的手机号:{}".format(sql))
            member = self.mysql.fetch_one(sql)  # 返回一个元祖
            print("注册前手机号为:{}".format(member['MobilePhone']))
            before = int(member['MobilePhone'])
            logger.info("注册前手机号为:{}".format(member['MobilePhone']))

        resp = self.http_request.request(case.method, case.url, case.data)
        try:
            self.assertEqual(case.expected,resp.text)
            self.excel.write_result(case.case_id + 1,resp.text,'PASS')

            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                logger.info("注册查询当前最大的手机号:{}".format(sql))
                member = self.mysql.fetch_one(sql)
                # print("注册成功后的手机号为:{}".format(member['MobilePhone']))
                after = int(member['MobilePhone'])
                self.assertEqual(before + 1, after)
                logger.info("注册成功后的手机号为:{}".format(member['MobilePhone']))

        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAILED')
            logger.info("ERROR:{}".format(e))
            raise e

        logger.info('结束测试:{}'.format(case.title))


    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
        cls.mysql.close()