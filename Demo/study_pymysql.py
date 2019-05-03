#-*-coding:utf-8-*-
#@Time      :2019/5/2 0002 14:00
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :study_pymysql.py
#@Software  :PyCharm Community Edition

import pymysql


#1、建立连接，数据库的连接信息
host = 'test.lemonban.com'
user = 'test'
password = 'test'
port = 3306
charset = 'UTF-8'
mysql = pymysql.connect(host=host,user=user,password=password,port=port)
#2、新建一个查询页面
cursor = mysql.cursor()#新建一个游标对象，记录sql的作用
#3、编写sql
sql = 'SELECT max(MobilePhone) from future.member'
# sql = 'SELECT * from future.member limit 10'
#4、执行sql
cursor.execute(sql)
#5、查看结果
result = cursor.fetchone() #获取查询结果集里面最近一条数据，保存在一个结果中
print(type(result),result) #返回结果类型为元祖，结果为最大的手机号

# 多条数据的话，也存放在元祖中，元祖中嵌套元祖，一条结果一条元祖
# result = cursor.fetchall() #获取全部结果集
#print(type(result),result[0])
#6、关闭查询
cursor.close()
#7、关闭数据库连接
mysql.close()
