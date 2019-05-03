#-*-coding:utf-8-*-
#@Time      :2019/5/2 0002 18:08
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :context.py
#@Software  :PyCharm Community Edition

"""
上下文处理，正则的通用类，调用replace进行替换，目前主要用于操作excel，对excel中的参数进行匹配和替换
"""
import re
from Common.config import config
import configparser

class Context:

    loan_id = None

'''
match(p,target) 从字符串开头位置开始匹配
***  search() 对字符串的任意位置进行匹配
***  findall() 返回字符串中所有匹配的字符串组成的列表
finditer() 返回一个包含了所有的匹配对象的迭代器
'''
def replace(data):
    p = '#(.*?)#'  # 正则表达式
    while re.search(p, data):
        # print('context类：替换之前的data ', data)
        m = re.search(p, data)  # 查找在data中，查找p 从任意位置开始找，找到第一个就返回Match object，如果么有就返回None
        g = m.group(1)  # 拿到参数化的key
        try:
            v = config.get('data', g)  # 根据Key取配置文件里面的值
        except configparser.NoOptionError as e:
            if hasattr(Context,g):
                v =  getattr(Context,g)
            else:
                print("context 找不到参数化的值")
                raise e

        print('context.v:{}'.format(v))
        # 替换后的内容，继续用data接收
        data = re.sub(p, v, data, count=1)  # sub,查找并替换，pattern  count有多少替换多少

    return data
    # print('context类：替换之后的data ', data)