#coding=utf-8
import time
import threading

gen = None

#handler获取耗时操作
def longIo():
    def run():
        print("开始耗时操作")
        time.sleep(5)
        try:
            global gen
            gen.send("sunck is a good man")
        except StopIteration as e:
            pass
        print("结束耗时操作")
    threading.Thread(target=run).start()



# 一个客户端的请求
def reqA():
    print "开始处理reqA"
    res = yield longIo()
    print "接收到longIo的响应数据：", res
    print "结束处理reqA"

# 另一个客户端请求
def reqB():
    print("开始处理reqB")
    time.sleep(2)
    print("结束处理reqB")

# tornado服务
def main():
    global gen
    gen = reqA()
    next(gen)

    reqB()
    while 1:
        time.sleep(0.4)
        pass




if __name__ == '__main__':
    main()