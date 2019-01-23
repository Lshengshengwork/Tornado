#coding=utf-8
import time
import threading


#handler获取耗时操作
def longIo(callback):
    def run(cb):
        print("开始耗时操作")
        time.sleep(5)
        print("结束耗时操作")
        cb('sunck is a good mann ')
    threading.Thread(target=run,args=(callback,)).start()


#回调函数
def finish(data):
    print "开始处理回调函数"
    print "接收到longIo的响应数据：",data
    print "结束处理回调函数"



# 一个客户端的请求
def reqA():
    print "开始处理reqA"
    longIo(finish)
    print "结束处理reqA"

# 另一个客户端请求
def reqB():
    print("开始处理reqB")
    time.sleep(2)
    print("结束处理reqB")

# tornado服务
def main():
    reqA()
    reqB()
    while 1:
        time.sleep(0.4)
        pass




if __name__ == '__main__':
    main()