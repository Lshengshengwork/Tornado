#coding=utf-8
import tornado.web
import config
from views import index


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/',index.IndaxHandler),
            (r'/home',index.HomeHandler),
            (r"/helloworld", index.MainHandler),
            (r"/echows", index.EchoWebSocket),
            (r"/wstest", index.WsTestHandler),

            #write
            (r"/write",index.WriteHandler),
            #json
            (r"/json1",index.Json1Handler),
            (r"/json2",index.Json2Handler),

            #header
            (r"/header", index.HeaderHandler),
            #status_code
            (r"/status", index.StatusCodeHandler),

            (r"/index", index.IndexHandler),
            (r"/poem", index.PoemPageHandler),

        ]
        super(Application, self).__init__(handlers,**config.settings)