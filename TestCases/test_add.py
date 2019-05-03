#-*-coding:utf-8-*-
#@Time      :2019/5/1 0001 23:19
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :test_login.py
#@Software  :PyCharm Community Edition

import unittest

from ddt import ddt, data
from Common import contants
from Common import do_excel
from Common.http_request import HttpRequestSession
from Common.config import config
from Common import context

"""
加投标，使用unittest
"""
@ddt
class AddTest(unittest.TestCase):
    # contants为文件路径，获取文件的路径，login为excel的sheet
    excel = do_excel.DoExcel(contants.case_file, 'add')
    cases = excel.get_cases()

    #使用DDT的时候不能使用setUP,需要使用@classmethod
    @classmethod
    def setUpClass(cls):
        cls.http_request = HttpRequestSession()

    #data可接受字典，元祖，列表等等
    @data(*cases)
    def test_add(self,case):
        # case.data = eval(case.data)
        # '''
        # 判断参数是否在测试用例中，然后根据配置文件进行赋值，比较低级，需要重复的进行判断
        # '''
        # print(type(case.data),case.data)
        # if  case.data.__contains__('mobilephone') and case.data['mobilephone']=='normal_user':
        #     case.data['mobilephone'] =  config.get('data', 'normal_user')
        # if case.data.__contains__('pwd') and case.data['pwd']=='normal_pwd':
        #     case.data['pwd'] =  config.get('data', 'normal_pwd')
        # if case.data.__contains__('memberId') and case.data['memberId'] == 'loan_member_id':
        #     case.data['memberId'] =  int(config.get('data', 'loan_member_id'))
        #     print(case.data['memberId'])


        #请求之前替换参数化的值
        case.data = context.replace(case.data)

        resp = self.http_request.request(case.method, case.url, case.data)
        # 调用json方法，转成json串，拿到json【字典】中的key:code
        actual_code = resp.json()['code']
        try:
            self.assertEqual(str(case.expected),actual_code)
            self.excel.write_result(case.case_id + 1,resp.text,'PASS')
        except AssertionError as e:
            self.excel.write_result(case.case_id + 1,resp.text,'FAILED')
            raise e


    @classmethod
    def tearDownClass(cls):
        cls.http_request.close()
