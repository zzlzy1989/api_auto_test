# api_auto_test

部署环境时，首先执行requirements.txt，命令如下:
    导出环境中的第三方库：pip freeze > requirements.txt
    新的服务器导入第三方库：pip -r install requirements.txt


1、Common封装的常用的方法
    contants 方法为定义路径方法，获取文件路径和其他参数的路径
    do_excel 操作excel方法
    http_request  HTTP_REQUEST方法，操作接口，其中封装了get和post方法
        （注：后期维护put，delete，file等方法）
    context 上下文处理，正则的通用类，调用replace进行替换，目前主要用于操作excel，对excel中的参数进行匹配和替换
    config 完成配置文件的读取
    do_mysql 操作数据库，完成与MySQL数据库的交互
    http_request 使用这类的request方法去完成不同的http请求，并且返回响应结果

2、Config    配置文件
    config
    global.conf
    online.conf
    test.conf

3、Log

4、Reports

5、TestCases

6、TestDatas

