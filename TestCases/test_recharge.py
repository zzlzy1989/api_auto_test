#-*-coding:utf-8-*-
#@Time      :2019/5/2 0002 00:15
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :test_recharge.py
#@Software  :PyCharm Community Edition

import unittest
from Common.http_request import HttpRequestSession
from Common import do_excel
from Common import contants
from ddt import ddt,data
from Common import do_mysql
from Common import logger


logger= logger.get_logger(__name__)

"""
    充值测试用例，使用unittest
"""
@ddt
class RechargeTest(unittest.TestCase):

    # contants为文件路径，获取文件的路径，recharge为excel的sheet
    excel = do_excel.DoExcel(contants.case_file, 'recharge')
    cases = excel.get_cases()

    '''
        #使用DDT的时候不能使用setUP,需要使用@classmethod
        #使用classmethod是为了在setUpClass开一次
    '''
    @classmethod
    def setUpClass(cls):
        logger.info('准备测试前置:test_recharge')
        cls.http_request = HttpRequestSession()
        cls.mysql = do_mysql.DoMysql()

    '''
    #data可接受字典，元祖，列表等等
    '''
    @data(*cases)
    def test_recharge(self,case):

        logger.info("开始测试:{}".format(case.title))
        logger.info("测试入参 ",case.data)
        print("测试用例标题 ",case.title)
        print("测试入参 ",case.data)

        '''
        请求之前，判断是否需要执行SQL
        '''
        if case.sql is not None:
            sql = eval(case.sql)['sql1'] #转换成字典，使用eval
            logger.info(sql)
            member = self.mysql.fetch_one(sql)   #返回一个元祖
            print("执行sql返回一个字典:{}".format(member))
            print("充值前金额:{}",member['LeaveAmount'])
            before = member['LeaveAmount']

        #调用http_request中的request方法，返回结果保存在resp中
        resp = self.http_request.request(case.method, case.url, case.data)
        #调用json方法，转成json串，拿到json【字典】中的key:code
        actual_code = resp.json()['code']
        try:
            #调用asserEqual，进行断言，判断case中expected和获取的json中code的值是否一致
            self.assertEqual(str(case.expected),actual_code)

            #调用excel中的write_result方法，写入数据
            self.excel.write_result(case.case_id+1,resp.text,'PASS')

            if case.sql is not None:
                sql = eval(case.sql)['sql1']
                logger.info(sql)
                member = self.mysql.fetch_one(sql)  # 返回一个元祖
                print("充值后金额:{}".format(member['LeaveAmount']))
                after = member['LeaveAmount']
                recharge_amount = int(eval(case.data)['amount'])  # 充值金额
                self.assertEqual(before+recharge_amount,after)

        except AssertionError as e: #
            self.excel.write_result(case.case_id+1,resp.text,'FAILED')
            logger.error('ERROR:{}'.format(e))
            raise e
        logger.info('结束测试:{}'.format(case.title))

    @classmethod
    def tearDownClass(cls):
        logger.info('测试后置处理')
        cls.http_request.close()
        cls.mysql.close()