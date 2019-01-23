# coding=utf-8
import tornado.web
from tornado.web import RequestHandler

import tornado.websocket
import socket
import struct
import config
import os

def get_ip_address(ifname):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,  # SIOCGIFADDR
            struct.pack('256s', ifname[:15])
        )[20:24])
    except Exception as e:
        return '127.0.0.1'

current_ip = get_ip_address('eth1')


class IndaxHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello! world ")


class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("home")



class EchoWebSocket(tornado.websocket.WebSocketHandler):

    def open(self):
        self.write_message("WebSocket opened,%s" % current_ip)

    def on_message(self, message):
        self.write_message(message)

    def on_close(self):
        print("WebSocket closed")

    def check_origin(self, origin):
        return True


class WsTestHandler(RequestHandler):

    def get(self):
        self.render("wstest.html")


class MainHandler(RequestHandler):

    def get(self):
        self.write(self.request.remote_ip)
        self.write(current_ip)


class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("sunck is a good man,\n")
        self.write("sunck is a nice man,\n")
        self.write("sunck is a handsome man.\n")
        #刷新缓冲区，关闭当次请求通道
        #在finish()下边就不要在write
        # self.finish()
        # self.write("sunck is a cool man")

#json
import json
class Json1Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "sunck",
            "age": 18,
            "height":178,
            "weight": 70,
        }
        # 将字典转换成json字符串
        jsonStr = json.dumps(per)
        self.set_header("Content-Type","application/json; charset=UTF-8")
        self.set_header("sunck","good")
        self.write(jsonStr)

class Json2Handler(RequestHandler):
    def get(self, *args, **kwargs):
        per = {
            "name": "kaige",
            "age": 18,
            "height":178,
            "weight": 70,
        }
        self.write(per)


#在进入HTTP相应处理方法之前被调用，可以重写该方法来预先设置默认的headers
# 注意：在HTTP处理方法中使用self.set_header设置的字段会覆盖set_default_headers()里设置默认字段的值
class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type","text/html; charset=UTF-8")

    def get(self, *args, **kwargs):
        self.write("*********************")
        pass

    def post(self, *args, **kwargs):
        pass



class StatusCodeHandler(RequestHandler):
    def get(self, *args, **kwargs):

        self.set_status(999,"我是谁，我在哪")
        self.write("*************")



class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")

class PoemPageHandler(RequestHandler):
    def post(self, *args, **kwargs):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                difference=noun3)

