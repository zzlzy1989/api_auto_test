#-*-coding:utf-8-*-
#@Time      :2019/5/3 0003 00:10
#@Author    :蓝天下的风
#@Email     :394845369@qq.com
#@File      :logger.py
#@Software  :PyCharm Community Edition

import logging
from Common import contants
from Common.config import config

"""
    对日志进行打印在console和日志文件中
"""

def get_logger(name):

    logger = logging.getLogger(name)
    logger.setLevel(config.get('log','level')) #读取配置文件中日志级别

    '''
    日志输入的格式
    '''
    fmt = "%(asctime)s -  %(name)s - %(levelname)s - %(message)s - [%(filename)s:%(lineno)d ]"
    formatter = logging.Formatter(fmt=fmt)  #格式化日志输出

    '''
    输出到控制台
    '''
    console_handler = logging.StreamHandler()  # 控制台
    # 把日志级别放到配置文件里面配置--优化
    console_handler.setLevel(config.get('log','level'))
    console_handler.setFormatter(formatter)

    '''
    输出到日志文件中 contants获取存放日志文件的路径以及存放日志的文件名
    '''
    file_handler = logging.FileHandler(contants.log_dir + '/case.log')
    # 把日志级别放到配置文件里面配置
    file_handler.setLevel(config.get('log','level'))
    file_handler.setFormatter(formatter)

    #加载日志到控制台
    logger.addHandler(console_handler)
    #加载日志到日志文件中
    logger.addHandler(file_handler)

    return logger


logger = get_logger('case')
logger.info('测试开始啦')
logger.error('测试报错')
logger.debug('测试数据')
logger.info('测试结束')