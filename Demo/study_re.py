#-*-coding:utf-8-*-
#@Time      :2019/5/2 0002 16:52
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :study_re.py
#@Software  :PyCharm Community Edition

import re
from Common.config import config

#原本字符，元字符
data = '{"mobilephone":"#normal_user#","pwd":"#normal_pwd#"}'
p = '#(.*?)#' #正则表达式

# m = re.search(p,data) #查找 ： 在data中，查找p 从任意位置开始找，找到第一个就返回Match object，如果么有就返回None
# print(m.group(0))   #返回表达式 和 组里面的内容
# print(m.group(1))   #只返回 指定组 的内容
# ms = re.findall(p,data) #查找全部，返回列表
# # print(ms)
# g = m.group(1)  #拿到参数化的key
# v = config.get('data',g)    #根据Key取配置文件里面的值
# print(v)
# data_new = re.sub(p,v,data,count=1)    #sub,查找并替换，pattern  count有多少替换多少
# print(data_new)

#如果要匹配多次，替換多次，使用循环来解决
while re.search(p,data):
    print('替换之前的data ',data)
    m = re.search(p, data)#查找 ： 在data中，查找p 从任意位置开始找，找到第一个就返回Match object，如果么有就返回None
    g = m.group(1)  # 拿到参数化的key
    print(g)
    v = config.get('data', g)  # 根据Key取配置文件里面的值
    # print(v)
    # 替换后的内容，继续用data接收
    data = re.sub(p, v, data, count=1)  # sub,查找并替换，pattern  count有多少替换多少

print('替换之后的data ',data)


