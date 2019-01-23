#coding=utf-8
import tornado.web
import config
import os
from views import index


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/index',index.IndaxHandler),
            (r'/home',index.HomeHandler),
            (r"/helloworld", index.MainHandler),

            # 反向解析，根据name的值匹配路由
            tornado.web.url(r"/yongsheng", index.yongshengHandler, {"word3": "handsome", "word4": "cool"},name="kaigegood"),
            # 提取特定uri
            (r"/liuyifei/(\w+)/(\w+)/(\w+)", index.LiuyifeiHandler),
            # 用get方法
            (r"/zhangmanyu", index.ZhangmanyuHandler),
           # 用post方法
            (r"/zhangmanyu", index.ZhangmanyuHandler),
            # request对象的使用
            (r"/zhuyin", index.ZhuyinHandler),
            # 上传文件
            (r"/upfile", index.UpfileHandler),
            # 重定向
            (r"/index", index.RedirectHandler),
            # 错误处理
            # iserror=flag=2
            (r"/iserror", index.ErrorHandler),



            #     自定义函数
            (r"/function", index.FunctionHandler),

            # 转义
            (r"/transferred", index.TransferredHandler),

            # 继承
            (r"/cart", index.CartHandler),
            
            # 设置普通cookie
            (r"/pcookie", index.PCookieHandler),
            # 获取普通cookie
            (r"/getpcookie", index.GetPCookieHandler),
            # 清除cookie
            (r"/clearpcookie", index.ClearPCookieHandler),

            # 设置安全cookie
            (r"/scookie", index.SCookieHandler),
            # 获取安全cookie
            (r"/getscookie", index.GetSCookieHandler),

            #cookie 计数
            (r"/cookienum", index.CookieNumHandler),
            # 用post才计数
            (r"/postfile", index.PostFileHandler),

            # 用户验证  逻辑是：如果用户未登录跳转到登录页面，登录了
            (r"/login", index.LoginHandler),
            (r"/lhome", index.LHomeHandler),
            (r"/gwc", index.GwcHandler),


            # StaticFileHandler    ,注意：要放在所有路由的最下面 ,写法和使用如下
            (r"/(.*)$", tornado.web.StaticFileHandler, {"path":os.path.join(config.BASE_DIRS,"static/html"), "default_filename":"index.html"})

        ]
        super(Application, self).__init__(handlers,**config.settings)