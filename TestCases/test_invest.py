#-*-coding:utf-8-*-
#@Time      :2019年5月10日19:01:23
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
from Common import context
from Common import logger

logger = logger.get_logger(__name__)

"""
注册，使用unittest
"""
@ddt
class InvestTest(unittest.TestCase):
    # contants为文件路径，获取文件的路径，login为excel的sheet
    excel = do_excel.DoExcel(contants.case_file, 'invest')
    cases = excel.get_cases()

    #使用DDT的时候不能使用setUP,需要使用@classmethod
    @classmethod
    def setUpClass(cls):
        logger.info("TEST CASE START : InvestTest")
        cls.http_request = HttpRequestSession()
        cls.mysql = do_mysql.DoMysql()
    #data可接受字典，元祖，列表等等
    @data(*cases)
    def test_invest(self,case):
        logger.info(case.title)
        print("开始执行测试用例 ",case.title)

        #请求之前替换参数化的值--替换配置文件online中设置的data的值
        case.data = context.replace(case.data)
        print("替换配置文件完成后，data的值:{}".format(case.data))

        #判断是否投资人正常投资，sql是否存在
        if case.title == "投资人正常投资":
            if case.sql is not None:
                case.sql = context.replace(case.sql)
                logger.info("替换配置文件完成后，sql的值:{}".format(case.sql))
                print("替换配置文件完成后，sql的值:{}".format(case.sql))
                #sql1查询用户表，获取LeaveAmount
                sql1 = eval(case.sql)['sql1']
                logger.info(sql1)
                member = self.mysql.fetch_one(sql1)  # 返回一个元祖
                before_leave_amount = member['LeaveAmount']
                print('before_leave_amount:'.format(before_leave_amount))

        resp = self.http_request.request(case.method, case.url, case.data)
        # 调用json方法，转成json串，拿到json【字典】中的key:code
        actual_code = resp.json()['code']

        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id + 1,resp.text,'PASS')

            #判断加标成功后，查询数据库，取到loan_id
            if resp.json()['msg'] == "加标成功":
                if case.sql is not None:
                    case.sql = context.replace(case.sql)
                    logger.info("替换配置文件完成后，sql的值:{}".format(case.sql))
                    print("替换配置文件完成后，sql的值:{}".format(case.sql))
                    # sql = 'select id from future.loan where memberid = 199 order by id limit 1'
                    sql = eval(case.sql)['sql1']
                    loan_id = self.mysql.fetch_one(sql)['Id']
                    print("加标之后的标的ID ",loan_id)
                    #保存到类属性里面
                    setattr(context.Context,"loan_id",str(loan_id))

            # 判断是否投资人正常投资，sql是否存在
            if resp.json()['msg'] == "竞标成功":
                if case.sql is not None:
                    case.sql = context.replace(case.sql)
                    logger.info("替换配置文件完成后，sql的值:{}".format(case.sql))
                    print("替换配置文件完成后，sql的值:{}".format(case.sql))

                    # sql1查询用户表，获取LeaveAmount
                    sql1 = eval(case.sql)['sql1']
                    logger.info(sql1)
                    member = self.mysql.fetch_one(sql1)  # 返回一个元祖
                    after_leave_amount = member['LeaveAmount']
                    print('after_leave_amount:'.format(after_leave_amount))

                    # sql查询流水记录表 获取到加标ID：IncomeMemberId  加标金额：Amount
                    sql2 = eval(case.sql)['sql2']
                    logger.info(sql2)
                    member2 = self.mysql.fetch_one(sql2)
                    financelog_income_member_id = member2['IncomeMemberId']
                    financelog_amount = member2['Amount']
                    print('financelog_amount:'.format(financelog_amount))

                    #sql查询投资记录表invest 查询 MemberID  loanId  Amount
                    sql3 = eval(case.sql)['sql3']
                    logger.info(sql3)
                    member3 = self.mysql.fetch_one(sql3)
                    invest_member_id = member3['MemberID']
                    invest_loan_id = member3['LoanId']
                    invest_amount = member3['Amount']
                    print('invest_amount:'.format(invest_amount))

                    self.assertEqual(before_leave_amount - invest_amount, after_leave_amount)
                    self.assertEqual(before_leave_amount - financelog_amount, after_leave_amount)
                    # self.assertEqual(float(before_leave_amount) - float(invest_amount), float(after_leave_amount))
                    # self.assertEqual(float(before_leave_amount) - float(financelog_amount), float(after_leave_amount))
                    #self.assertEqual(financelog_income_member_id,invest_member_id)
                    #self.assertEqual(loan_id,invest_loan_id)

        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAILED')
            logger.debug("ERROR:{}".format(e))
            raise e


    @classmethod
    def tearDownClass(cls):
        logger.info("THE END")
        cls.http_request.close()
        cls.mysql.close()