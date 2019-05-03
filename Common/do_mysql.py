#-*-coding:utf-8-*-
#@Time      :2019/5/2 0002 14:23
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :do_mysql.py
#@Software  :PyCharm Community Edition

import pymysql
from Common.config import config

"""
操作数据库，完成与MySQL数据库的交互
"""
class DoMysql:

   '''
   连接，init实例化时，就已经建立好了连接
   '''
   def __init__(self):
       # 1、建立连接，数据库的连接信息
       # host = 'test.lemonban.com'
       # user = 'test'
       # password = 'test'
       # port = 3306
       '''
        调用config类中的config，使配置连接地址进行参数化。
       '''
       host = config.get('mysql','host')
       user = config.get('mysql', 'user')
       password = config.get('mysql','password')
       port = int(config.get('mysql', 'port'))
       # print(host,user,password,port)

       self.mysql = pymysql.connect(host=host, user=user, password=password, port=port,charset='utf8')
       # 2、新建一个查询页面
       # self.cursor = self.mysql.cursor()  # 新建一个游标对象，记录sql的作用 self实例属性，其他方法可以使用
       # 新建一个游标对象，记录sql的作用 self实例属性，其他方法可以使用
       # 创建一个字典类型的游标
       self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)

   def fetch_one(self, sql):
       self.cursor.execute(sql)
       self.mysql.commit()
       return self.cursor.fetchone()  # 返回一条数据，元组

   def fetch_all(self, sql):
       self.cursor.execute(sql)
       return self.cursor.fetchall()  # 返回多条数据的时候，元组里面套元组

   def close(self):
       self.cursor.close()  # 关闭游标
       self.mysql.close()  # 关闭连接

'''
if __name__ == '__main__':
   mysql=DoMysql()
   result1 = mysql.fetch_one('select max(mobilephone) from future.member')  # 返回一条数据，元组
   print(type(result1), result1)
   result2 = mysql.fetch_all('select * from future.member limit 10')  # 返回多条数据的时候，元组里面套元组
   print(type(result2), result2)
   mysql.close()
'''