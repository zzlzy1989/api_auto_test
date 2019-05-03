#-*-coding:utf-8-*-
#@Time      :2019/5/2 0002 00:50
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :config.py
#@Software  :PyCharm Community Edition

import configparser
from Common import contants

"""
    1、完成配置文件的读取,ConfigParser 是用来读取配置文件的包。配置文件的格式如下：中括号“[ ]”内包含的为section。
        section 下面为类似于key-value 的配置内容。
    2、ConfigParser 初始化对象，ConfigParser 首选需要初始化实例，并读取配置文件
    3、ConfigParser 常用方法
        1,获取所用的section节点:config.sections()
        2,获取指定section 的options。即将配置文件某个section 内key 读取到列表中:config.options("db")
        3,获取指点section下指点option的值:config.get("db", "db_host")
        4,获取指点section的所用配置信息:config.items("db")
        5,修改某个option的值，如果不存在则会出创建:
            config.set("db", "db_port", "69")  #修改db_port的值为69
            config.write(open("ini", "w"))
        6,检查section或option是否存在，bool值:
            config.has_section("section") #是否存在该section
            config.has_option("section", "option")  #是否存在该option
        7,添加section 和 option:
            if not config.has_section("default"):  # 检查是否存在section
                config.add_section("default")
            if not config.has_option("default", "db_host"):  # 检查是否存在该option
                config.set("default", "db_host", "1.1.1.1")
            config.write(open("ini", "w"))
        8,删除section 和 option
            config.remove_section("default") #整个section下的所有内容都将删除
            config.write(open("ini", "w"))
        9,写入文件  写回文件的方式如下：（使用configparser的write方法）
            config.write(open("ini", "w"))
"""
class ReadConfig:
    #读取配置文件
    def __init__(self):
        #配置文件的第三方库
        self.config = configparser.ConfigParser()
        self.config.read(contants.global_file,encoding='utf8')  #先加载global里面的开关
        #取配置文件中的值
        switch = self.config.getboolean('switch','on')
        if switch:#开关打开的时候，使用online的配置
            self.config.read(contants.online_file,encoding='utf8')
        else:#开关关闭的时候，使用test的配置
            self.config.read(contants.test_file,encoding='utf8')

    '''
        获取指点section下指点option的值
    '''
    def get(self,section,option):
        return self.config.get(section,option)

#实例化，可在其他类直接引用
config=ReadConfig()

# if __name__ == '__main__':
#     config = ReadConfig()
#     print(config.get('api','pre_url'))