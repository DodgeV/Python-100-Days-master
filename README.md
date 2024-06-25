🌍我的python笔记

# 100天学习python笔记

### Day01~15 - [Python语言基础](./Day01-15)

#### Day01 - [初识Python](./Day01-15/01.初识Python.md)

- Python简介 - Python的历史 / Python的优缺点 / Python的应用领域
- 搭建编程环境 - Windows环境 / Linux环境 / MacOS环境
- 从终端运行Python程序 - Hello, world / print函数 / 运行程序
- 使用IDLE - 交互式环境(REPL) / 编写多行代码 / 运行程序 / 退出IDLE
- 注释 - 注释的作用 / 单行注释 / 多行注释

#### Day02 - [语言元素](./Day01-15/02.语言元素.md)

- 程序和进制 - 指令和程序 / 冯诺依曼机 / 二进制和十进制 / 八进制和十六进制
- 变量和类型 - 变量的命名 / 变量的使用 / input函数 / 检查变量类型 / 类型转换
- 数字和字符串 - 整数 / 浮点数 / 复数 / 字符串 / 字符串基本操作 / 字符编码
- 运算符 - 数学运算符 / 赋值运算符 / 比较运算符 / 逻辑运算符 / 身份运算符 / 运算符的优先级
- 应用案例 - 华氏温度转换成摄氏温度 / 输入圆的半径计算周长和面积 / 输入年份判断是否是闰年

#### Day03 - [分支结构](./Day01-15/03.分支结构.md)

- 分支结构的应用场景 - 条件 / 缩进 / 代码块 / 流程图
- if语句 - 简单的if / if-else结构 / if-elif-else结构 / 嵌套的if
- 应用案例 - 用户身份验证 / 英制单位与公制单位互换 / 掷骰子决定做什么 / 百分制成绩转等级制 / 分段函数求值 / 输入三条边的长度如果能构成三角形就计算周长和面积

#### Day04 - [循环结构](./Day01-15/04.循环结构.md)

- 循环结构的应用场景 - 条件 / 缩进 / 代码块 / 流程图
- while循环 - 基本结构 / break语句 / continue语句
- for循环 - 基本结构 / range类型 / 循环中的分支结构 / 嵌套的循环 / 提前结束程序 
- 应用案例 - 1~100求和 / 判断素数 / 猜数字游戏 / 打印九九表 / 打印三角形图案 / 猴子吃桃 / 百钱百鸡

#### Day05 - [构造程序逻辑](./Day01-15/05.构造程序逻辑.md)

- 经典案例：水仙花数 / 百钱百鸡 / Craps赌博游戏
- 练习题目：斐波那契数列 / 完美数 / 素数

#### Day06 - [函数和模块的使用](./Day01-15/06.函数和模块的使用.md)

- 函数的作用 - 代码的坏味道 / 用函数封装功能模块
- 定义函数 - def语句 / 函数名 / 参数列表 / return语句 / 调用自定义函数
- 调用函数 - Python内置函数 /  导入模块和函数
- 函数的参数 - 默认参数 / 可变参数 / 关键字参数 / 命名关键字参数
- 函数的返回值 - 没有返回值  / 返回单个值 / 返回多个值
- 作用域问题 - 局部作用域 / 嵌套作用域 / 全局作用域 / 内置作用域 / 和作用域相关的关键字
- 用模块管理函数 - 模块的概念 / 用自定义模块管理函数 / 命名冲突的时候会怎样（同一个模块和不同的模块）

#### Day07 - [字符串和常用数据结构](./Day01-15/07.字符串和常用数据结构.md)

- 字符串的使用 - 计算长度 / 下标运算 / 切片 / 常用方法
- 列表基本用法 - 定义列表 / 用下表访问元素 / 下标越界 / 添加元素 / 删除元素 / 修改元素 / 切片 / 循环遍历
- 列表常用操作 - 连接 / 复制(复制元素和复制数组) / 长度 / 排序 / 倒转 / 查找
- 生成列表 - 使用range创建数字列表 / 生成表达式 / 生成器
- 元组的使用 - 定义元组 / 使用元组中的值 / 修改元组变量 / 元组和列表转换
- 集合基本用法 - 集合和列表的区别 /  创建集合 / 添加元素 / 删除元素 /  清空
- 集合常用操作 - 交集 / 并集 / 差集 / 对称差 / 子集 / 超集
- 字典的基本用法 - 字典的特点 / 创建字典 / 添加元素 / 删除元素 / 取值 / 清空
- 字典常用操作 - keys()方法 / values()方法 / items()方法 / setdefault()方法
- 基础练习 - 跑马灯效果 / 列表找最大元素 / 统计考试成绩的平均分 / Fibonacci数列 / 杨辉三角
- 综合案例 - 双色球选号 / 井字棋

#### Day08 - [面向对象编程基础](./Day01-15/08.面向对象编程基础.md)

- 类和对象 - 什么是类 / 什么是对象 / 面向对象其他相关概念
- 定义类 - 基本结构 / 属性和方法 / 构造器 / 析构器 / `__str__`方法
- 使用对象 - 创建对象 / 给对象发消息
- 面向对象的四大支柱 - 抽象 / 封装 / 继承 / 多态
- 基础练习 - 定义学生类 / 定义时钟类 / 定义图形类 / 定义汽车类

#### Day09 - [面向对象进阶](./Day01-15/09.面向对象进阶.md)

- 属性 - 类属性 / 实例属性 / 属性访问器 / 属性修改器 / 属性删除器 / 使用__slots__
- 类中的方法 - 实例方法 / 类方法 / 静态方法
- 运算符重载 - __add__ / __sub__ / __or__ /__getitem__ / __setitem__ / __len__ / __repr__ / __gt__ / __lt__ / __le__ / __ge__ / __eq__ / __ne__ / __contains__ 
- 类(的对象)之间的关系 - 关联 / 继承 / 依赖
- 继承和多态 - 什么是继承 / 继承的语法 / 调用父类方法 / 方法重写 / 类型判定 / 多重继承 / 菱形继承(钻石继承)和C3算法
- 综合案例 - 工资结算系统 / 图书自动折扣系统 / 自定义分数类

#### Day10 - [图形用户界面和游戏开发](./Day01-15/10.图形用户界面和游戏开发.md)

- 使用tkinter开发GUI程序
- 使用pygame三方库开发游戏应用
- “大球吃小球”游戏

#### Day11 - [文件和异常](./Day01-15/11.文件和异常.md)

- 读文件 - 读取整个文件 / 逐行读取 / 文件路径
- 写文件 - 覆盖写入 / 追加写入 / 文本文件 / 二进制文件
- 异常处理 - 异常机制的重要性 / try-except代码块 / else代码块 / finally代码块 / 内置异常类型 / 异常栈 / raise语句
- 数据持久化 - CSV文件概述 / csv模块的应用 / JSON数据格式 / json模块的应用

#### Day12 - [字符串和正则表达式](./Day01-15/12.字符串和正则表达式.md)

- 字符串高级操作 - 转义字符 / 原始字符串 / 多行字符串 / in和 not in运算符 / is开头的方法 / join和split方法 / strip相关方法 / pyperclip模块 / 不变字符串和可变字符串 / StringIO的使用
- 正则表达式入门 - 正则表达式的作用 / 元字符 / 转义 / 量词 / 分组 / 零宽断言 /贪婪匹配与惰性匹配懒惰 / 使用re模块实现正则表达式操作（匹配、搜索、替换、捕获）
- 使用正则表达式 - re模块 / compile函数 / group和groups方法 / match方法 / search方法 / findall和finditer方法 / sub和subn方法 / split方法
- 应用案例 - 使用正则表达式验证输入的字符串

#### Day13 - [进程和线程](./Day01-15/13.进程和线程.md)

- 进程和线程的概念 - 什么是进程 / 什么是线程 / 多线程的应用场景
- 使用进程 - fork函数 / multiprocessing模块 / 进程池 / 进程间通信
- 使用线程 - thread模块 / threading模块 / Thread类 / Lock类 / Condition类 / 线程池

#### Day14 - [网络编程入门和网络应用开发](./Day01-15/14.网络编程入门和网络应用开发.md)

- 计算机网络基础 - 计算机网络发展史 / “TCP-IP”模型 / IP地址 / 端口 / 协议 / 其他相关概念
- 网络应用模式 - “客户端-服务器”模式 / “浏览器-服务器”模式
- 基于HTTP协议访问网络资源 - 网络API概述 / 访问URL / requests模块 / 解析JSON格式数据
- Python网络编程 - 套接字的概念 / socket模块 /  socket函数 / 创建TCP服务器 / 创建TCP客户端 / 创建UDP服务器 / 创建UDP客户端 / SocketServer模块
- 电子邮件 - SMTP协议 / POP3协议 / IMAP协议 / smtplib模块 / poplib模块 / imaplib模块
- 短信服务 - 调用短信服务网关

#### Day15 - [图像和文档处理](./Day01-15/15.图像和办公文档处理.md)

- 用Pillow处理图片 - 图片读写 / 图片合成 / 几何变换 / 色彩转换 / 滤镜效果
- 读写Word文档 - 文本内容的处理 / 段落 / 页眉和页脚 / 样式的处理
- 读写Excel文件 - xlrd模块 / xlwt模块
- 生成PDF文件 - pypdf2模块 / reportlab模块

### Day16~Day20 - [Python语言进阶](./Day16-20/16-20.Python语言进阶.md)

- 常用数据结构
- 函数的高级用法 - “一等公民” / 高阶函数 / Lambda函数 / 作用域和闭包 / 装饰器
- 面向对象高级知识 - “三大支柱” / 类与类之间的关系 / 垃圾回收 / 魔术属性和方法 / 混入 / 元类 / 面向对象设计原则 / GoF设计模式
- 迭代器和生成器 - 相关魔术方法 / 创建生成器的两种方式 / 
- 并发和异步编程 - 多线程 / 多进程 / 异步IO / async和await

### Day21~30 - [Web前端入门](./Day21-30/21-30.Web前端概述.md)

- 用HTML标签承载页面内容
- 用CSS渲染页面
- 用JavaScript处理交互式行为
- jQuery入门和提高
- Vue.js入门
- Element的使用
- Bootstrap的使用

### Day31~35 - [玩转Linux操作系统](./Day31-35/31-35.玩转Linux操作系统.md)

- 操作系统发展史和Linux概述
- Linux基础命令
- Linux中的实用程序
- Linux的文件系统
- Vim编辑器的应用
- 环境变量和Shell编程
- 软件的安装和服务的配置
- 网络访问和管理
- 其他相关内容

### Day36~40 - [数据库基础和进阶](./Day36-40)

- [关系型数据库MySQL](./Day36-40/36-38.关系型数据库MySQL.md)
  - 关系型数据库概述
  - MySQL的安装和使用
  - SQL的使用
    - DDL - 数据定义语言 - create / drop / alter
    - DML - 数据操作语言 - insert / delete / update / select
    - DCL - 数据控制语言 - grant / revoke
  - 相关知识
    - 范式理论 - 设计二维表的指导思想
    - 数据完整性
    - 数据一致性
  - 在Python中操作MySQL
- [NoSQL入门](./Day36-40/39-40.NoSQL入门.md)
  - NoSQL概述
  - Redis概述
  - Mongo概述

### Day41~55 - [实战Django](./Day41-55)

#### Day41 - [Django快速上手](./Day41-55/41.Django快速上手.md)

- Web应用工作机制
- HTTP请求和响应
- Django框架概述
- 5分钟快速上手

#### Day42 - [深入模型](./Day41-55/42.深入模型.md)

- 关系型数据库配置
- 使用ORM完成对模型的CRUD操作
- 管理后台的使用
- Django模型最佳实践
- 模型定义参考

#### Day43 - [静态资源和Ajax请求](./Day41-55/43.静态资源和Ajax请求.md)

- 加载静态资源
- Ajax概述
- 用Ajax实现投票功能

#### Day44 - [Cookie和Session](./Day41-55/44.Cookie和Session.md)

- 实现用户跟踪
- cookie和session的关系
- Django框架对session的支持
- 视图函数中的cookie读写操作

#### Day45 - [报表和日志](./Day41-55/45.制作报表.md)

- 通过HttpResponse修改响应头
- 使用StreamingHttpResponse处理大文件
- 使用xlwt生成Excel报表
- 使用reportlab生成PDF报表
- 使用ECharts生成前端图表

#### Day46 - [日志和调试工具栏](./Day41-55/46.日志和调试工具栏.md)

- 配置日志
- 配置Django-Debug-Toolbar
- 优化ORM代码

#### Day47 - [中间件的应用](./Day41-55/47.中间件的应用.md)

- 什么是中间件
- Django框架内置的中间件
- 自定义中间件及其应用场景

#### Day48 - [前后端分离开发入门](./Day41-55/48.前后端分离开发入门.md)

- 返回JSON格式的数据
- 用Vue.js渲染页面

#### Day49 - [RESTful架构和DRF入门](./Day41-55/49.RESTful架构和DRF入门.md)

#### Day50 - [RESTful架构和DRF进阶](./Day41-55/50.RESTful架构和DRF进阶.md)

#### Day51 - [使用缓存](./Day41-55/51.使用缓存.md)

- 网站优化第一定律

- 在Django项目中使用Redis提供缓存服务
- 在视图函数中读写缓存
- 使用装饰器实现页面缓存
- 为数据接口提供缓存服务

#### Day52 - [文件上传](./Day41-55/52.文件上传.md)

- 文件上传表单控件和图片文件预览
- 服务器端如何处理上传的文件

#### Day53 - [异步任务和定时任务](./Day41-55/53.异步任务和定时任务.md)

- 网站优化第二定律
- 配置消息队列服务
- 在项目中使用celery实现任务异步化
- 在项目中使用celery实现定时任务

#### Day54 - [单元测试](./Day41-55/54.单元测试.md)

#### Day55 - [项目上线](./Day41-55/55.项目上线.md)

- Python中的单元测试
- Django框架对单元测试的支持
- 使用版本控制系统
- 配置和使用uWSGI
- 动静分离和Nginx配置
- 配置HTTPS
- 配置域名解析


### Day56~60 - [实战Flask](./Day56-65)

#### Day56 - [Flask入门](./Day56-60/56.Flask入门.md)

#### Day57 - [模板的使用](./Day56-60/57.模板的使用.md)

#### Day58 - [表单的处理](./Day56-60/58.表单的处理.md)

#### Day59 - [数据库操作](./Day56-60/59.数据库操作.md)

#### Day60 - [项目实战](./Day56-60/60.项目实战.md)

### Day61~65 - [实战Tornado](./Day61-65)

#### Day61 - [预备知识](./Day61-65/61.预备知识.md)

- 并发编程
- I/O模式和事件驱动

#### Day62 - [Tornado入门](./Day61-65/62.Tornado入门.md)

- Tornado概述
- 5分钟上手Tornado
- 路由解析
- 请求处理器

#### Day63 - [异步化](./Day61-65/63.异步化.md)

- aiomysql和aioredis的使用

#### Day64 - [WebSocket的应用](./Day61-65/64.WebSocket的应用.md)

- WebSocket简介
- WebSocket服务器端编程
- WebSocket客户端编程
- 项目：Web聊天室

#### Day65 - [项目实战](./Day61-65/65.项目实战.md)

- 前后端分离开发和接口文档的撰写
- 使用Vue.js实现前端渲染
- 使用ECharts实现报表功能
- 使用WebSocket实现推送服务

### Day66~75 - [爬虫开发](./Day66-75)

#### Day66 - [网络爬虫和相关工具](./Day66-75/66.网络爬虫和相关工具.md)

- 网络爬虫的概念及其应用领域
- 网络爬虫的合法性探讨
- 开发网络爬虫的相关工具
- 一个爬虫程序的构成

#### Day67 - [数据采集和解析](./Day66-75/67.数据采集和解析.md)

- 数据采集的标准和三方库
- 页面解析的三种方式：正则表达式解析 / XPath解析 / CSS选择器解析

#### Day68 - [存储数据](./Day66-75/68.存储数据.md)

- 如何存储海量数据
- 实现数据的缓存

#### Day69 - [并发下载](./Day66-75/69.并发下载.md)

- 多线程和多进程
- 异步I/O和协程
- async和await关键字的使用
- 三方库aiohttp的应用

#### Day70 - [解析动态内容](./Day66-75/70.解析动态内容.md)

- JavaScript逆向工程
- 使用Selenium获取动态内容

#### Day71 - [表单交互和验证码处理](./Day66-75/71.表单交互和验证码处理.md)

- 自动提交表单
- Cookie池的应用
- 验证码处理

#### Day72 - [Scrapy入门](./Day66-75/72.Scrapy入门.md)

- Scrapy爬虫框架概述
- 安装和使用Scrapy

#### Day73 - [Scrapy高级应用](./Day66-75/73.Scrapy高级应用.md)

- Spider的用法
- 中间件的应用：下载中间件 / 蜘蛛中间件
- Scrapy对接Selenium抓取动态内容
- Scrapy部署到Docker

#### Day74 - [Scrapy分布式实现](./Day66-75/74.Scrapy分布式实现.md)

- 分布式爬虫的原理
- Scrapy分布式实现
- 使用Scrapyd实现分布式部署

#### Day75 - [爬虫项目实战](./Day66-75/75.爬虫项目实战.md)

- 爬取招聘网站数据
- 爬取房地产行业数据
- 爬取二手车交易平台数据

### Day76~90 - [数据分析和机器学习](./Day76-90)

> **温馨提示**：数据分析和机器学习的内容在code文件夹中，是用jupyter notebook书写的代码和笔记，需要先启动jupyter notebook再打开对应的文件进行学习。2020年会持续补充相关文档，希望大家持续关注。

#### Day76 - [机器学习基础](./Day76-90/76.机器学习基础.md)

#### Day77 - [Pandas的应用](./Day76-90/77.Pandas的应用.md)

#### Day78 - [NumPy和SciPy的应用](./Day76-90/78.NumPy和SciPy的应用)

#### Day79 - [Matplotlib和数据可视化](./Day76-90/79.Matplotlib和数据可视化)

#### Day80 - [k最近邻(KNN)分类](./Day76-90/80.k最近邻分类.md)

#### Day81 - [决策树](./Day76-90/81.决策树.md)

#### Day82 - [贝叶斯分类](./Day76-90/82.贝叶斯分类.md)

#### Day83 - [支持向量机(SVM)](./Day76-90/83.支持向量机.md)

#### Day84 - [K-均值聚类](./Day76-90/84.K-均值聚类.md)

#### Day85 - [回归分析](./Day76-90/85.回归分析.md)

#### Day86 - [大数据分析入门](./Day76-90/86.大数据分析入门.md)

#### Day87 - [大数据分析进阶](./Day76-90/87.大数据分析进阶.md)

#### Day88 - [Tensorflow入门](./Day76-90/88.Tensorflow入门.md)

#### Day89 - [Tensorflow实战](./Day76-90/89.Tensorflow实战.md)

#### Day90 - [推荐系统实战](./Day76-90/90.推荐系统实战.md)

### Day91~100 - [团队项目开发](./Day91-100)

#### 第91天：[团队项目开发的问题和解决方案](./Day91-100/91.团队项目开发的问题和解决方案.md)

1. 软件过程模型
   - 经典过程模型（瀑布模型）
     - 可行性分析（研究做还是不做），输出《可行性分析报告》。
     - 需求分析（研究做什么），输出《需求规格说明书》和产品界面原型图。
     - 概要设计和详细设计，输出概念模型图（ER图）、物理模型图、类图、时序图等。
     - 编码 / 测试。
     - 上线 / 维护。

     瀑布模型最大的缺点是无法拥抱需求变化，整套流程结束后才能看到产品，团队士气低落。
   - 敏捷开发（Scrum）- 产品所有者、Scrum Master、研发人员 - Sprint
     - 产品的Backlog（用户故事、产品原型）。
     - 计划会议（评估和预算）。
     - 日常开发（站立会议、番茄工作法、结对编程、测试先行、代码重构……）。
     - 修复bug（问题描述、重现步骤、测试人员、被指派人）。
     - 发布版本。
     - 评审会议（Showcase，用户需要参与）。
     - 回顾会议（对当前迭代周期做一个总结）。

     > 补充：敏捷软件开发宣言
     >
     > - **个体和互动** 高于 流程和工具
     > - **工作的软件** 高于 详尽的文档
     > - **客户合作** 高于 合同谈判
     > - **响应变化** 高于 遵循计划

     ![](./res/agile-scrum-sprint-cycle.png)

     > 角色：产品所有者（决定做什么，能对需求拍板的人）、团队负责人（解决各种问题，专注如何更好的工作，屏蔽外部对开发团队的影响）、开发团队（项目执行人员，具体指开发人员和测试人员）。

     > 准备工作：商业案例和资金、合同、憧憬、初始产品需求、初始发布计划、入股、组建团队。

     >  敏捷团队通常人数为8-10人。

     >  工作量估算：将开发任务量化，包括原型、Logo设计、UI设计、前端开发等，尽量把每个工作分解到最小任务量，最小任务量标准为工作时间不能超过两天，然后估算总体项目时间。把每个任务都贴在看板上面，看板上分三部分：to do（待完成）、in progress（进行中）和done（已完成）。

2. 项目团队组建

   - 团队的构成和角色

     > 说明：谢谢**付祥英**女士帮助我绘制了下面这张精美的公司组织架构图。

     ![company_architecture](./res/company_architecture.png)

   - 编程规范和代码审查（flake8、pylint）

     ![](./res/pylint.png)

   - Python中的一些“惯例”（请参考[《Python惯例-如何编写Pythonic的代码》](Python惯例.md)）

   - 影响代码可读性的原因：

     - 代码注释太少或者没有注释
     - 代码破坏了语言的最佳实践
     - 反模式编程（意大利面代码、复制-黏贴编程、自负编程、……）

3. 团队开发工具介绍
   - 版本控制：Git、Mercury
   - 缺陷管理：[Gitlab](https://about.gitlab.com/)、[Redmine](http://www.redmine.org.cn/)
   - 敏捷闭环工具：[禅道](https://www.zentao.net/)、[JIRA](https://www.atlassian.com/software/jira/features)
   - 持续集成：[Jenkins](https://jenkins.io/)、[Travis-CI](https://travis-ci.org/)

   请参考[《团队项目开发的问题和解决方案》](Day91-100/91.团队项目开发的问题和解决方案.md)。

##### 项目选题和理解业务

1. 选题范围设定

   - CMS（用户端）：新闻聚合网站、问答/分享社区、影评/书评网站等。
   - MIS（用户端+管理端）：KMS、KPI考核系统、HRS、CRM系统、供应链系统、仓储管理系统等。

   - App后台（管理端+数据接口）：二手交易类、报刊杂志类、小众电商类、新闻资讯类、旅游类、社交类、阅读类等。
   - 其他类型：自身行业背景和工作经验、业务容易理解和把控。

2. 需求理解、模块划分和任务分配

   - 需求理解：头脑风暴和竞品分析。
   - 模块划分：画思维导图（XMind），每个模块是一个枝节点，每个具体的功能是一个叶节点（用动词表述），需要确保每个叶节点无法再生出新节点，确定每个叶子节点的重要性、优先级和工作量。
   - 任务分配：由项目负责人根据上面的指标为每个团队成员分配任务。

   ![](./res/requirements_by_xmind.png)

3. 制定项目进度表（每日更新）

   | 模块 | 功能     | 人员   | 状态     | 完成 | 工时 | 计划开始 | 实际开始 | 计划结束 | 实际结束 | 备注             |
   | ---- | -------- | ------ | -------- | ---- | ---- | -------- | -------- | -------- | -------- | ---------------- |
   | 评论 | 添加评论 | 王大锤 | 正在进行 | 50%  | 4    | 2018/8/7 |          | 2018/8/7 |          |                  |
   |      | 删除评论 | 王大锤 | 等待     | 0%   | 2    | 2018/8/7 |          | 2018/8/7 |          |                  |
   |      | 查看评论 | 白元芳 | 正在进行 | 20%  | 4    | 2018/8/7 |          | 2018/8/7 |          | 需要进行代码审查 |
   |      | 评论投票 | 白元芳 | 等待     | 0%   | 4    | 2018/8/8 |          | 2018/8/8 |          |                  |

4. OOAD和数据库设计

  - UML（统一建模语言）的类图

    ![uml](./res/uml-class-diagram.png)

  - 通过模型创建表（正向工程）

    ```Shell
    python manage.py makemigrations app
    python manage.py migrate
    ```

  - 使用PowerDesigner绘制物理模型图。

    ![](./res/power-designer-pdm.png)

  - 通过数据表创建模型（反向工程）

    ```Shell
    python manage.py inspectdb > app/models.py
    ```

#### 第92天：[Docker容器详解](./Day91-100/92.Docker容器详解.md)

1. Docker简介
2. 安装Docker
3. 使用Docker创建容器（Nginx、MySQL、Redis、Gitlab、Jenkins）
4. 构建Docker镜像（Dockerfile的编写和相关指令）
5. 容器编排（Docker-compose）
6. 集群管理（Kubernetes）

#### 第93天：[MySQL性能优化](./Day91-100/93.MySQL性能优化.md)

#### 第94天：[网络API接口设计](./Day91-100/94.网络API接口设计.md)

#### 第95天：[使用Django开发商业项目](./Day91-100/95.使用Django开发商业项	目.md)

##### 项目开发中的公共问题

1. 数据库的配置（多数据库、主从复制、数据库路由）
2. 缓存的配置（分区缓存、键设置、超时设置、主从复制、故障恢复（哨兵））
3. 日志的配置
4. 分析和调试（Django-Debug-ToolBar）
5. 好用的Python模块（日期计算、图像处理、数据加密、三方API）

##### REST API设计

1. RESTful架构
   - [理解RESTful架构](http://www.ruanyifeng.com/blog/2011/09/restful.html)
   - [RESTful API设计指南](http://www.ruanyifeng.com/blog/2014/05/restful_api.html)
   - [RESTful API最佳实践](http://www.ruanyifeng.com/blog/2018/10/restful-api-best-practices.html)
2. API接口文档的撰写
   - [RAP2](http://rap2.taobao.org/)
   - [YAPI](http://yapi.demo.qunar.com/)
3. [django-REST-framework](https://www.django-rest-framework.org/)的应用

##### 项目中的重点难点剖析

1. 使用缓存缓解数据库压力 - Redis
2. 使用消息队列做解耦合和削峰 - Celery + RabbitMQ

#### 第96天：[软件测试和自动化测试](Day91-100/96.软件测试和自动化测试.md)

##### 单元测试

1. 测试的种类
2. 编写单元测试（unittest、pytest、nose2、tox、ddt、……）
3. 测试覆盖率（coverage）

##### 项目部署

1. 部署前的准备工作
   - 关键设置（SECRET_KEY / DEBUG / ALLOWED_HOSTS / 缓存 / 数据库）
   - HTTPS / CSRF_COOKIE_SECUR  / SESSION_COOKIE_SECURE  
   - 日志相关配置
2. Linux常用命令回顾
3. Linux常用服务的安装和配置
4. uWSGI/Gunicorn和Nginx的使用
   - Gunicorn和uWSGI的比较
     - 对于不需要大量定制化的简单应用程序，Gunicorn是一个不错的选择，uWSGI的学习曲线比Gunicorn要陡峭得多，Gunicorn的默认参数就已经能够适应大多数应用程序。
     - uWSGI支持异构部署。
     - 由于Nginx本身支持uWSGI，在线上一般都将Nginx和uWSGI捆绑在一起部署，而且uWSGI属于功能齐全且高度定制的WSGI中间件。
     - 在性能上，Gunicorn和uWSGI其实表现相当。
5. 使用虚拟化技术（Docker）部署测试环境和生产环境

##### 性能测试

1. AB的使用
2. SQLslap的使用
3. sysbench的使用

##### 自动化测试

1. 使用Shell和Python进行自动化测试
2. 使用Selenium实现自动化测试
   - Selenium IDE
   - Selenium WebDriver
   - Selenium Remote Control
3. 测试工具Robot Framework介绍

#### 第97天：[电商网站技术要点剖析](./Day91-100/97.电商网站技术要点剖析.md)

#### 第98天：[项目部署上线和性能调优](./Day91-100/98.项目部署上线和性能调优.md)

1. MySQL数据库调优
2. Web服务器性能优化
   - Nginx负载均衡配置
   - Keepalived实现高可用
3. 代码性能调优
   - 多线程
   - 异步化
4. 静态资源访问优化
   - 云存储
   - CDN

#### 第99天：[面试中的公共问题](./Day91-100/99.面试中的公共问题.md)

#### 第100天：[Python面试题集](./Day91-100/100.Python面试题集.md)

### [番外篇](./extra)

1. Python面试题汇总
2. 使用Hexo搭建自己的博客
3. 用函数还是用复杂的表达式
4. 租房网项目接口文档
5. 那些年我们踩过的那些坑
6. 一个小例子助你彻底理解协程
7. 我为什么选择了Python
8. 知乎问题回答
9. 英语面试
10. PEP8风格指南
11. Python编程惯例
12. Python之禅
13. 玩转PyCharm
14. 常用库整理

# mypractice

+ [100 classic examples of python](./mypractice/python_100_classic_examples):尤其需要注意37/39/67/68/69/80/83/84/85
+ [The Big Book of Small Python Projects](https://inventwithpython.com/bigbookpython/)&[code](./mypractice/BigBookPythonResources)
+ [Python 练习册-每天一点小练习-25题](https://github.com/Yixiaohan/show-me-the-code)&[Reference](https://github.com/Show-Me-the-Code/python)&[mycode](./mypractice/Python_25_exercises)
+ [python百道面试题](https://github.com/kenwoodjw/python_interview_question)
+ [pythonchallenge](http://www.pythonchallenge.com/)

# sets

- [python-patterns](https://github.com/faif/python-patterns)
- [python-cheatsheet备忘录](https://github.com/gto76/python-cheatsheet)
- [Crossin的编程教室-学习资源+项目实战](https://crossincode.com/home/)
- [Crossin's python初学常见问题汇总 ](https://mp.weixin.qq.com/s/pC_r4VliHrn9WEVFEnVjSQ)
- [Python算法学习与机器学习算法资源汇总](https://mp.weixin.qq.com/s/nsOt-uLJBegehVkGigmuow)
- [倾心整理的Python量化资源大合集](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484656&idx=1&sn=7692a9c0f342e59e6c62c9ce3d003d94&chksm=f9e3c21ace944b0c784f3a1a7660b6cb2e0f9b31a9912869a03efc7a55ca0249d7bd27acd92d&scene=0&xtrack=1#rd)
- [Python量化从入门到精通 ](https://mp.weixin.qq.com/s?__biz=MzUyMDk1MDY2MQ==&mid=2247484258&idx=1&sn=5daf786c06cde32d6bbd0b0ffb50e871&chksm=f9e3c588ce944c9e763f9110f7c8fc0b800ab26d8ae8598c6310f0220b80767d1f58a1d78381&mpshare=1&scene=1&srcid=1028fiZEC6bx13VIT62D8GnB&sharer_sharetime=1679190241056&sharer_shareid=ccb3982f74463770fa13a7e792141680#rd)

# tutorials

- [微软官方教程c9-python-getting-started](https://github.com/microsoft/c9-python-getting-started)
- [List of Algorithms implemented in Python](https://github.com/TheAlgorithms/Python/blob/master/DIRECTORY.md)
- [pcc--Resources for Python Crash Course, from No Starch Press.](https://github.com/ehmatthes/pcc)
- [pycrumbs--Bits and bytes of Python from the Internet ](https://github.com/kirang89/pycrumbs)
- [pythondoc](http://www.pythondoc.com/)
- [DataSciencePython](https://github.com/ujjwalkarn/DataSciencePython)
- [python爬虫教程](https://github.com/Kr1s77/Python-crawler-tutorial-starts-from-zero)
- [python简单crawler教程](https://github.com/Kr1s77/awesome-python-login-model)
- [python爬虫教程系列](https://github.com/wistbean/learn_python3_spider)
- [web.py 0.3 教程](https://blog.csdn.net/c9cad/article/details/4089643)
- [【笔记】17 幅思维导图：Python 核心知识体系](https://woaielf.github.io/2018/04/10/python-basic/)
- [12个案例教你用Python玩转数据可视化](https://mp.weixin.qq.com/s/BqQoaWqprVlZf9y0IXJrdA)
- [python3.0的18张思维导图核心知识-数林觅风](./res/v3.0-ZOE-SLMF)

# books

- [参考书籍清单](./Python参考书籍)
- [free-programming-books-zh_CN for Python](https://github.com/justjavac/free-programming-books-zh_CN/blob/master/README.md#python)
- [Official doc](https://docs.python.org/3/)
- [用python进行科学计算](https://github.com/DodgeV/demo1/blob/master/package_DA/%E7%94%A8Python%E5%81%9A%E7%A7%91%E5%AD%A6%E8%AE%A1%E7%AE%97.pdf)
- [Python for Data Analysis](https://github.com/wesm/pydata-book)[视频](https://www.bilibili.com/video/av80675432)
- [菜鸟教程--python](https://www.runoob.com/python3/python3-stdlib.html)
- [廖雪峰python](https://www.liaoxuefeng.com/wiki/1016959663602400)
- [scrapy 白皮书](https://scrapy-cookbook.readthedocs.io/zh_CN/latest/scrapy-01.html#scrapy)

# videos

- [python就业形势](https://www.bilibili.com/video/BV1Y7411v7T1?p=87)&[对应ppt](https://github.com/DodgeV/learning-programming/blob/master/books/python/python%E5%B0%B1%E4%B8%9A%E5%BD%A2%E5%8A%BF.pptx)
- [Python3 入门与进阶](https://www.bilibili.com/video/BV1At4y1i76x)&[对应源码](https://github.com/DodgeV/learning-programming/tree/master/books/python/Python3%20%E5%85%A5%E9%97%A8%E4%B8%8E%E8%BF%9B%E9%98%B6)
- [python从入门到实践--bilibili](https://www.bilibili.com/video/BV1Y7411v7T1)
- [零基础入门学习Python(小甲鱼)](https://www.bilibili.com/video/BV1y7411d7rW)&[全套源码课件](https://github.com/DodgeV/learning-programming/tree/master/books/python/%E9%9B%B6%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%E5%AD%A6%E4%B9%A0Python(%E5%B0%8F%E7%94%B2%E9%B1%BC)%E5%85%A8%E5%A5%97%E6%BA%90%E7%A0%81%E8%AF%BE%E4%BB%B6)
- [千锋Python基础视频&对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/python/%E5%8D%83%E9%94%8BPython%E5%9F%BA%E7%A1%80%E8%A7%86%E9%A2%91)
- [全国计算机二级Python科目基础知识教程](https://www.bilibili.com/video/BV1ht41187Aa)&[真题操作题部分讲解](https://www.bilibili.com/video/BV1Vb411h7K8)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/%E4%BA%8C%E7%BA%A7)&[Python二级考试考纲笔记（2018全）](https://mubu.com/doc/1Bam_vCyQw)
- [python老男孩linux运维](https://www.bilibili.com/video/BV1k54y1m7BC)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/python/python%E8%80%81%E7%94%B7%E5%AD%A9linux%E8%BF%90%E7%BB%B4)
- [python网络程序开发-炼数成金-2012](https://www.bilibili.com/video/BV1D54y1U7dM)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/python/python%E7%BD%91%E7%BB%9C%E7%A8%8B%E5%BA%8F%E5%BC%80%E5%8F%91-%E7%82%BC%E6%95%B0%E6%88%90%E9%87%91-2012)
- [Python网络爬虫与信息提取--北理工](http://www.icourse163.org/learn/BIT-1001870001)
- [Python科学计算三维可视化--北理工](http://www.icourse163.org/learn/BIT-1001871001)
- [Python机器学习--北理工](http://www.icourse163.org/learn/BIT-1001872001)
- [用Python玩转数据--南京大学](http://www.icourse163.org/learn/NJU-1001571005)
- [零基础学习PythonCAP--北理工](http://www.icourse163.org/learn/BIT-1002058035)
- [python公开课](https://www.bilibili.com/video/BV11K4y1S7MM)&[对应资料](https://github.com/DodgeV/learning-programming/tree/master/books/python/python%E5%85%AC%E5%BC%80%E8%AF%BE)
- [传智播客day25网络爬虫](https://www.bilibili.com/video/av84404200?p=86)&[如果失效用这个](https://www.bilibili.com/video/av50730537)
- [传智播客python就业班](https://www.bilibili.com/video/BV1uJ411Y7uH?p=115) 或 [python2018就业班全集（前半部分）](https://www.bilibili.com/video/BV1b4411b74E?p=116)&[Python2018就业班（后半部分）](https://www.bilibili.com/video/av53525697/)

# demo

- [GitHub Top 45：新手入门 Python，值得推荐的优质资源！](https://mp.weixin.qq.com/s/fLZdDQE_trhKRLyQKoORzg)
- [You-are-Pythonista python projects](https://github.com/MiracleYoung/You-are-Pythonista)
- [Some interesting Python crawlers and data analysis project](https://github.com/Alfred1984/interesting-python)
- [five Practice Python Projects](https://github.com/learnbyexample/practice_python_projects)
- [Scrapy爬虫实战](https://github.com/Jaysong2012/tutorial)
- [大众点评评论文本挖掘项目](https://github.com/py-bin/dianping_textmining)
- [Super Mario Bros made with Python and Pygame](https://github.com/justinmeister/Mario-Level-1)
- [链家二手房租房在线数据，存量房交易服务平台数据，详细数据分析教程](https://github.com/XuefengHuang/lianjia-scrawler)
- [Zipline, a Pythonic Algorithmic Trading Library](https://github.com/quantopian/zipline)
- [阿布量化交易系统(股票，期权，期货，比特币，机器学习) 基于python的开源量化交易，量化投资架构](https://github.com/bbfamily/abu)
- [Flask 10天开发一个网站 - 知乎](https://zhuanlan.zhihu.com/p/33038507)
