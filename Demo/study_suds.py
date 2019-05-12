# -*- coding:utf-8 -*-
# @Author   : GaoXu
# @Time     : 2019/5/12 13:36
# @File     : study_suds.py
# @Software : api_auto_test


from suds.client import Client
import suds

class send_webservice():

    #获取短信验证码接口
    def req_sendMCode(self):
        #要访问的Webservice地址
        url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
        #创建Webservice Client对象
        client = Client(url)
        #print(client)可以打印出Client对象所有的方法
        #print(client)
        data = {"client_ip":"192.168.1.1","tmpl_id":"1","mobile":"17792303803"}
        try:
            resp = client.service.sendMCode(data)
            print("返回码", resp.retCode)
            print("返回信息", resp.retInfo)
        except suds.WebFault as e:
            print(e.fault.faultstring)

    def req_userRegister(self):

        url = "http：//120.24.235.105:9010/finance-user_info-war-1.0/ws/financeUserInfoFacade.ws?wsdl"
        client = Client(url)
        data = {"verify_code": "111111", "user_id": "1", "channel_id": "1","pwd":"123456","mobile":"17792303803","ip":"192.168.1.1"}
        try:
            resp = client.service.userRegister(data)
            print("返回码", resp.retCode)
            print("返回信息", resp.retInfo)
        except suds.WebFault as e:
            print(e.fault.faultstring)


    def ws_request(self,url,data,method):
        client = Client(url)
        try:
            resp= eval("client.service.{0}({1})".format(method,data))
            msg=resp.retInfo
            print(resp.retCode)
            print(resp.retInfo)
        except suds.WebFault as e:
            print(e.fault.faultstring)
            msg = e.fault.faultstring
        return msg

if __name__ == '__main__':
    send_webservice = send_webservice()
    # send_webservice.req_sendMCode()
    # send_webservice.req_userRegister()
    url = "http://120.24.235.105:9010/sms-service-war-1.0/ws/smsFacade.ws?wsdl"
    data = {"client_ip": "192.168.1.1", "tmpl_id": "1", "mobile": "17792303803"}
    send_webservice.ws_request(url,data,"sendMCode")
