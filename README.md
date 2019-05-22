一、项目描述：

        api_auto_test 接口自动化测试框架（简易版）
引言
        
        部署环境时，首先执行requirements.txt，命令如下:
        导出环境中的第三方库：pip freeze > requirements.txt
        新的服务器导入第三方库：pip -r install requirements.txt
    
二、各个模块简介

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
        
三、git常用命令

    git clone 拷贝副本到本地
    git status 查看未被追踪的文件
    git add 追踪文件F
    git commit -m "注释" 提交文件
    git push 推到远程
    git branch 查看本地所有的分支
    git branch -a 查看所有的远程分支
    git checkout -b branch1 创建分支
    git checkout master 切换分支
    git push --set-upstream origin branch1 将分支推送到远程
    
四、pycharm操作git

    1、安装完成git以后，在setting中设置git.exe文件，在安装目录中找到git.exe文件，然后就可以在pycharm中操作git了
    2、在右下角有git的分支结构，local branchs代表本地分支结构，remot branchs远程分支结构
    3、在开发新的代码时，首先创建一个分支，或者是用本地分支
    4、在使用本地分支时，查看本地和远程分支是否一致，如果不一致，将本地分支提交或marge远程分支结构到本地，然后进行编写代码！
    5、New Branch,创建一个新的分支，以当前获取的分支代码为基准！
    6、修改代码并进行提交，右键Git>Commit Files，查看修改记录，点击commit and push进行提交；提交完成后就可以在GitHub网站中进行合并分支

五、Jenkins持续集成

    1、安装jenkins，方式1：官网下载jenkins.war，java -jar jenkins.war，命令行停掉，服务会停掉 --httpPort=8888修改端口号
    2、下载jenkins.war包，加到tomcat中，进行控制，启动tomcat时，jenkins自动启动 --server.xml修改端口号
    3、windows中，安装pgk，jenkins.msi文件，安装完成后，自动加入服务中，服务中加入jenkins服务，自动启动（修改端口号：文件找到jenkins
        ，修改httpPort=8888）
    4、默认安装目录为D:\Jenkins
    5、持续集成工具还有hudson，jenkins
    6、jenkins主要做，拿到开发的最新代码部署到服务器上
    7、系统设置--全局工具配置（配置git地址，安装版本）--插件管理（enkins安装插件：HTML Publisher/git/Email Extension）
    8、mater-slave主从构建，分布式构建，web ui。修改jenkins配置，可以使用grouvy
    9、在jenkin配置中，添加：构建》执行Windows批处理命令》
        命令：pip install -r requirements.txt --user
        python TestCases/run.py
        添加：构建后操作 Publis HTML Reports： HTML directory to archive（文件路径）Index page[s]（页面地址）Report title（标题）
        添加：Editable Extended Email Publisher 》》》 Attachments（附件）Reports/report.html,
            Attach Build Log配置Do Not Attach Build Log
    10、点击构建，即可进行自动构建项目！

六、部分类和方法的说明
    1、用TestCase类来实现一个测试
        1）我们将通过集成TestCase类并且 在测试类中为每一个测试添加测试方法来创建单个测试或者一组测试；
            测试用例使用excel维护，并且进行参数化，通过自定义context上下文管理的类，来操作excel，对excel中的参数进行匹配和替换；
        2）TestCase中的常用的assert方法，最主要的任务是：
            调用assertEqual()来校验结果；
            assertTrue()来验证条件；
            assertRaises来验证预期的异常；
            通过使用第三方库pymysql（Mysql）查询SQL，和TestCase的返回值，进行匹配校验；
            操作过程中重要的返回结果将通过调用logger来进行记录，以便快速定位问题；
        3）除了添加测试，还可以添加测试夹具，setUp()方法和tearDown()方法；
        4）一个测试用例是从setUp()方法开始执行，因此可以在每个测试开始前执行一些初始化的任务；此方法无参数，也无返回值；
        5）接着编写test方法，这些测试方法命名为test开头，这种命名约定通知test runner哪个方法代表测试方法；
        6）值得注意的是：test runner能找到的每个测试方法，都会在执行测试方法之前先执行setUp()方法，
            这样有助于确保每个测试方法都能够依赖于相同的环境；
        7）tearDown()方法会在测试执行完成之后调用，用来清理所有的初始值；
        8）最后就是运行测试：为了能通过命令行测试，我们可以在测试中添加对main方法的调用；
        9) 优化：为了能让各个测试方法共用一个实例，我们可以创建类级别的setUp()和tearDown()方法：
            1）通过setUpClass()方法和tearDownClass()方法及@classmethod标识来实现；
            2）这两个方法使在类级别初始化数据，替代了方法级别的初始化；
    2、学习unittest提供的不同类型的assert方法
        断言：unittest的TestCase类提供了很多实用的方法来校验预期结果和实际结果是否一致；以下为常用的集中断言方式：
        assertEqual(a, b [, msg]);
        assertNotEqual(a, b [, msg]);
        assertTrue(x [, msg]); assertFalse(x [, msg]);
        assertIsNot(a, b [, msg]);
        assertRaises(exc, fun, *args, **kwds);
    3、为一组测试创建TestSuite
        应用unittest的TestSuites特性，可以将不同的测试组成一个逻辑组，然后设置统一的测试套件，并通过一个命令来执行；
        具体通过TestSuites、TestLoader和TestRunner类来实现的；
        我们使用TestSuites类来定义和执行测试套件，将多可测试加到一个测试套件中；
        还用TestLoader和TextTestRunner创建和运行测试套件；
    4、使用unittest扩展来生成HTML格式的测试报告