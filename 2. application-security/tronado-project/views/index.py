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



class MainHandler(RequestHandler):

    def get(self):
        self.write(self.request.remote_ip)
        # self.write(self.request.headers)




class IndaxHandler(RequestHandler):
    def initialize(self):
        print "initialize"
    def prepare(self):
        print "prepare"
    def get(self, *args, **kwargs):
        self.send_error(500)
        self.write("hello! world ")
    def set_default_headers(self):
        print "set_default_headers"
    def write_error(self, status_code, **kwargs):
        self.write("服务器错误辣...")
        print "write_error"
    def on_finish(self):
        print "on_finish"
        


# 渲染
class HomeHandler(RequestHandler):
    def get(self, *args, **kwargs):
        num = 100
        per = {
            "name":"sunck",
            "age": 18,
        }
        
        flag = 0
        
        stus = [
            {
                "name":"hanmeimei",
                "age":19
            },
            {
              "name":"lilei",
              "age":24
            }
        ]
        self.render('home.html',num = num, per = per, flag = flag, stus = stus)
        
        
class yongshengHandler(RequestHandler):
    def initialize(self,word3,word4):
        self.word3 = word3
        self.word4 = word4
    def get(self, *args, **kwargs):
        print(self.word3,self.word4)
        print(self.request.remote_ip)
        self.write("道友的ip是:%s" % (self.request.remote_ip))
        self.render("laodi.html")




class LiuyifeiHandler(RequestHandler):
    def get(self,h1,h2,h3, *args, **kwargs):
        print(h1 + "--" + h2 + "--" +h3)
        self.write("liuyifei is a nice")


class ZhangmanyuHandler(RequestHandler):
    def get(self, *args, **kwargs):
        # 带s的是可以接收到相同的参数，比如a=1&a=2
        # a = self.get_query_arguments("a")
        a = self.get_query_argument("a")
        b = self.get_query_argument("b")
        c = self.get_query_argument("c",strip=False)
        print(a, b, "*"+ c + "*")
        self.write("zhang man yu .")


class ZhuyinHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.path)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.body)
        print(self.request.files)
        print(self.request.remote_ip)
        ip = self.request.remote_ip
        self.write(ip)

class UpfileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('upfile.html')
    def post(self, *args, **kwargs):
        filesDict = self.request.files
        for inputname in filesDict:
            fileArr = filesDict[inputname]
            for fileObj in fileArr:
        #         存储路径
                filePath = os.path.join(config.BASE_URL,"upfile/" + fileObj.filename)
                print(filePath)
                with open(filePath,"wb") as f:
                    f.write(fileObj.body)

        self.write("OK")



class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect("/")


# 错误处理
class ErrorHandler(RequestHandler):
    def write_error(self, status_code, **kwargs):
        if status_code == 500:
            self.set_status(500)
            self.write("服务器内部错误")
        elif status_code == 404:
            self.set_status(404)
            self.write("资源不存在")
        else:
            self.set_status(999,"what?")
            self.write("我也不知道啥错误")

    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        if flag =='0':
            self.send_error(404)
        else:
            self.write("you are right")













        
#  自定义函数  在模板里调用
class FunctionHandler(RequestHandler):    
    def get(self, *args, **kwargs):
        def mySum(n1, n2):
            return n1 + n2
        self.render('function.html',ms = mySum)
        

        
        
'''转义 --- 默认是自动转义，能防止网站受到恶意攻击
              关闭自动转义   1. raw  ， 示例： {% raw str %}    注意：只能关闭一行
                            2. 在页面模板中修改 ， 示例  ：{% autoescape None %}   注意： 关闭当前文档的自动转义
                            3. 在config配置中修改  ， "autoescape": None   注意：关闭当前项目的自动转义 
                            4. escape() 函数； 作用：在关闭自动转义后，可以使用该方法对特定的变量进行转义  ， 示例： {{ escape(str) }}
'''
class TransferredHandler(RequestHandler):
    def get(self, *args, **kwargs):
        str = "<h1> sunck is a good man </h1>"
        self.render('transferred.html',str = str)

        
        
'''
继承：  父模板挖坑 ，子模板填坑
'''       

class CartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('cart.html', Title = "Cart")




# 普通cookie
class PCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_cookie("sunck","good")
        self.write("ok")

# 获取普通cookie
class GetPCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pcookie = self.get_cookie("sunck",default="未登录")
        print "pcookie ",pcookie
        self.write("ok")


# 清除cookie
class ClearPCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie("zhangmanyu")
        self.write("OK")

# 设置安全cookie
class SCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_secure_cookie("zhangmanyu","nice")
        self.write("ok")

# 获取安全cookie
class GetSCookieHandler(RequestHandler):
    def get(self, *args, **kwargs):
        scookie = self.get_secure_cookie("zhangmanyu")
        print "scookie :", scookie
        self.write("ok")



# cookie 计数
class CookieNumHandler(RequestHandler):
    def get(self, *args, **kwargs):
        count = self.get_cookie("count",None    )
        if not count:
            count = 1
        self.render("cookienum.html", count = count)
        
class PostFileHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('postfile.html')
    def post(self, *args, **kwargs):
        count = self.get_cookie("count", None)
        if not count:
            count =1
        else:
            count = int(count)
            count += 1
        self.set_cookie("count", str(count))
        self.redirect("/cookienum")



#用户验证
class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        next = self.get_argument("next", "/")
        url = "/login?next="+next
        self.render('login.html',url = url)
    def post(self, *args, **kwargs):
        name = self.get_argument("username")
        passwd = self.get_argument("passwd")
        if name == '1' and passwd == '1':
            next = self.get_argument("next", "/")
            self.redirect(next+"?flag=logined")
        else:
            next = self.get_argument("next", "/")
            self.redirect("/login?next="+next)

class LHomeHandler(RequestHandler):
    def get_current_user(self):
        flag = self.get_argument("flag",None)
        return flag
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('lhome.html')


class GwcHandler(RequestHandler):
    def get_current_user(self):
        flag = self.get_argument("flag",None)
        return flag
    @tornado.web.authenticated
    def get(self, *args, **kwargs):
        self.render('gwc.html')
        
        
        
        
        
        
        
        
        