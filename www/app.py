#!/home/python/.virtualenv/spider_py2/bin/python2
# -*- coding:utf-8 -*-

# 配置日志文件
import logging
logging.basicConfig(level=logging.INFO)

# 导入异步模块asynico
import asyncio,os,json,time
from datetime import datetime

# Web框架使用了基于asyncio的aiohttp
from aiohttp import web
def index(request):
    # 返回页面,调用web.Response方法,参数为body(响应体),content_type指定为text/html文本类型,页面才能渲染出来
    return web.Response(body='<h1>Awesome</h1>',content_type='text/html')


# 装饰协程程序,初始化app应用程序
@asyncio.coroutine
def init(loop):
    # 创建app对象
    app = web.Application(loop=loop)
    # 给app对象添加路由
    app.router.add_route('GET','/',index)
    #　用协程创建监听服务，并使用aiohttp中的HTTP协议簇
    # 其中loop为传入函数的协程，调用其类方法创建一个监听服务
    # yield from 返回一个创建好的，绑定IP、端口、HTTP协议簇的监听服务的协程。yield from的作用是使srv的行为模式和 loop.create_server()一致
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server start at http://127.0.0.1:9000')
    return srv


# 创建协程，初始化协程，返回监听服务，进入协程执行
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()