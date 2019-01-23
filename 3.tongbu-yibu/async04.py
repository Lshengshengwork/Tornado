#coding=utf-8
import time
import threading





# 加一个装饰器
def genCoroutine(func):
    def wrapper(*args,**kwargs):
        gen1 = func()   # reqA的生成器
        gen2 = next(gen1) # longIo的生成器
        def run(g):
            res = next(g)
            try:
                gen1.send(res)  # 返回给reqA数据
            except StopIteration as e:
                pass
        threading.Thread(target=run,args=(gen2,)).start()
    return wrapper


# handler获取耗时操作
def longIo():
    print("开始耗时操作")
    time.sleep(5)
    print("结束耗时操作")
    # 返回数据
    yield "sunck is a good man"


# 一个客户端的请求
@genCoroutine
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
    reqA()

    reqB()
    while 1:
        time.sleep(0.4)
        pass




if __name__ == '__main__':
    main()