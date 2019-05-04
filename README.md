# api_auto_test
部署环境时，首先执行requirements.txt，命令如下:
    导出环境中的第三方库：pip freeze > requirements.txt
    新的服务器导入第三方库：pip -r install requirements.txt


1、Common封装的常用的方法
    contants 方法为定义路径方法，获取文件路径和其他参数的路径
    do_excel 操作excel方法
    http_request  HTTP_REQUEST方法，操作接口，其中封装了get和post方法（注：后期维护put，delete，file等方法）
    context 上下文处理，正则的通用类，调用replace进行替换，目前主要用于操作excel，对excel中的参数进行匹配和替换
    config 完成配置文件的读取
    do_mysql 操作数据库，完成与MySQL数据库的交互
    http_request 使用这类的request方法去完成不同的http请求，并且返回响应结果
    HTMLTestRunnerNew 生成测试报告模板
    logger 日志处理

2、Config    配置文件
    global.conf 全局变量，控制使用线上还是test的环境开关
    online.conf 线上环境的配置  包含接口地址，数据库地址和HTMLTestRunnerNew的配置信息
    test.conf   测试环境配置

3、Log
    存放日志文件
4、Reports
    report.html 生成的测试报告文件
5、TestCases
    run.py  使用unittest，调用defaultTestLoader方法，加载discover，用来查询某个文件夹下以test_开头的.py结尾的文件，用来执行所有的测试用例，并生成测试报告
    test_add 加标测试用例
    test_invest 投标测试用例
    test_login 登录测试用例
    test_recharge 充值测试用例
    test_register 注册测试用例
6、TestDatas
    cases.xlsx 维护测试用例


git常用命令
    git clone 拷贝副本到本地
    git status 查看未被追踪的文件
    git add 追踪文件
    git commit -m "注释" 提交文件
    git push 推到远程
    git branch 查看本地所有的分支
    git branch -a 查看所有的远程分支
    git checkout -b branch1 创建分支
    git checkout master 切换分支
    git push --set-upstream origin branch1 将分支推送到远程
