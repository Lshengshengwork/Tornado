#coding=utf-8
import time


#handler获取耗时操作
def longIo():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")
    return "sunck is a good man"


# 一个客户端的请求
def reqA():
    print("开始处理reqA")
    res = longIo()
    print "接收到longIo的响应数据：",res
    print("结束处理reqA")

# 另一个客户端请求
def reqB():
    print("开始处理reqB")
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