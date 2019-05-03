#-*-coding:utf-8-*-
#@Time      :2019/4/12 0012 20:27
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :http_request.py
#@Software  :PyCharm Community Edition


import requests

from Common.config import config
from Common import logger

logger = logger.get_logger(__name__)


class HttpRequest():
    """
    使用这类的request方法去完成不同的http请求，并且返回响应结果
    """
    def request(self,method,url,data=None,json=None,cookies = None):
        method = method.upper() #强制转换成大写  upper大写，lower 小写

        #判断数据类型  Str 转成字典
        if type(data) == str:
            data = eval(data)

        #拼接URL
        url = config.get('api','pre_url')+url

        logger.debug('请求url ',url)
        logger.debug('请求data ',data)
        #判断调用接口的方式
        if method == "GET":
            resp = requests.get(url,params=data,cookies=cookies) #reso是request对象
        elif method == "POST":
            if json:
                resp = requests.post(url,json=json,cookies=cookies)
            else:
                resp = requests.post(url,data=data,cookies=cookies)
        else:
            resp = None
            logger.debug("UN-support method")

        return resp


class HttpRequestSession():
    """
    使用这类的request方法完成不同的HTTP请求，并返回响应结果
    """
    def __init__(self):
    #打开一个session
        self.session= requests.sessions.session()

    def request(self, method, url, data=None, json=None):

        method = method.upper()  #将method强制转换成大写
        # 判断数据类型
        if type(data) == str:
            data = eval(data)

        # 拼接URL
        url = config.get('api', 'pre_url') + url
        logger.debug('请求url ',url)
        logger.debug('请求data ',data)

        # 判断调用接口的方式
        if method == "GET":
            resp = self.session.request(method= method,url=url, params=data)  # reso是request对象
        elif method == "POST":
            if json:
                resp = self.session.request(method=method,url=url, json=json)
            else:
                resp = self.session.request(method=method,url=url, data=data)
        else:
            resp=None
            logger.debug("http_request,未找到请求的方法！---60行")

        print('http_request类，请求response ', resp.text)
        return resp

    def close(self):
        self.session.close()

# if __name__ == '__main__':
#     http_request = HttpRequest()
#     # 登录
#     params = {"mobilephone": "18888889999", "pwd": "123456"}
#     resp = http_request.request('post','http://test.lemonban.com/futureloan/mvc/api/member/login',params)
#     print(resp.status_code)
#     print(resp.text)
#     print(resp.cookies)
#     # 充值
#     params = {"mobilephone": "18888889999", "amount": "100"}
#     resp = http_request.request('post','http://test.lemonban.com/futureloan/mvc/api/member/recharge',params,cookies=resp.cookies)
#     print(resp.status_code)
#     print(resp.text)
#     print(resp.cookies)
#
#
#     HttpRequestSession=HttpRequestSession()
#     # 登录
#     params = {"mobilephone": "18888889999", "pwd": "123456"}
#     resp = HttpRequestSession.session.request('post',url='http://test.lemonban.com/futureloan/mvc/api/member/login',data=params)
#     print(resp.status_code)
#     print(resp.text)
#     print(resp.cookies)
#     # 充值
#     params = {"mobilephone": "18888889999", "amount": "100"}
#     resp = HttpRequestSession.session.request('post',url="http://test.lemonban.com/futureloan/mvc/api/member/recharge",data=params)
#     print(resp.status_code)
#     print(resp.text)
#     print(resp.cookies)
#     HttpRequestSession.close()  # 关闭session

