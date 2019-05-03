#-*-coding:utf-8-*-
#@Time      :2019/4/12 0012 20:41
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :study_session_request.py
#@Software  :PyCharm Community Edition

import requests

session = requests.sessions.session()

#注册
params = {"mobilephone":"18888889999","pwd":"123456"}
resp= session.request('post',
                url='http://test.lemonban.com/futureloan/mvc/api/member/register',
                data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

#登录
params = {"mobilephone":"18888889999","pwd":"123456"}
resp= session.request('post',
                url='http://test.lemonban.com/futureloan/mvc/api/member/login',
                data=params)
print(resp.status_code)
print(resp.text)
print(resp.cookies)

#充值
params = {"mobilephone":"18888889999","amount":"123456"}
resp=session.request('post',
                url="http://test.lemonban.com/futureloan/mvc/api/member/recharge",
                data=params)

print(resp.status_code)
print(resp.text)
print(resp.cookies)

session.close()#关闭session
