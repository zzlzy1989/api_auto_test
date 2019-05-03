#-*-coding:utf-8-*-
#@Time      :2019/4/9 0009 20:39
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :study_requests.py
#@Software  :PyCharm Community Edition3

import requests

'''
1、构造请求：请求方式，请求地址，请求参数
2、发起请求
3、返回响应
4、判断响应码，响应体
'''

#注册接口
params= {"mobilephone":"18888889999","pwd":"123456"}
#resp是response对象
resp = requests.get("http://test.lemonban.com/futureloan/mvc/api/member/register",params=params)

# print(resp)
print("响应码:",resp.request)
print("响应头:",resp.headers)
print("响应码:",resp.status_code)
print("响应文本:",resp.text)
print("响应cookies:",resp.cookies)
print("响应cookies:",resp.request._cookies)


#登录接口
params= {"mobilephone":"18888889999","pwd":"123456"}
#resp是response对象
resp = requests.post("http://test.lemonban.com/futureloan/mvc/api/member/login",data=params)
# print(resp)
print("响应码:",resp.status_code)
print("响应文本:",resp.text)
print("响应cookies:",resp.cookies)
print("响应cookies:",resp.request._cookies)
cookies = {"cookie1":"123","cookie1":"123123 "}

print("*"*40)
#登录接口
params= {"mobilephone":"18888889999","amount":"400"}
#resp是response对象
resp = requests.post("http://test.lemonban.com/futureloan/mvc/api/member/recharge",
                     data=params,cookies=resp.cookies)
print("响应码:",resp.status_code)
print("响应文本:",resp.text)
print("响应cookies:",resp.cookies)
print("响应cookies:",resp.request._cookies)