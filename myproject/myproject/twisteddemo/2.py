# -*- coding: utf-8 -*-
# @Time : 2022/6/6 10:52 下午
# @Author : chenxiangan
# @File : 2.py
# @Software: PyCharm
from twisted.internet import defer, reactor


#
# def func1(num):
#     defered = defer.Deferred()
#     defered.callback(num + 1)
#     print("func1 called with num =", num)
#     return defered
#
# def func2(num):
#     print("func2 called with num =", num)
#
# if __name__ == '__main__':
#     defered = func1(1)
#     print("func1 returned")
#     defered.addCallback(func2)
from twisted.python import failure


def func1(num):
    defered = defer.Deferred()
    if isinstance(num, str):
        # 四秒钟之后调用defered.callback，模拟耗时操作，参数为num+1。
        reactor.callLater(4, defered.callback, num + "1")
        print("func1 执行结束")
    else:
        reactor.callLater(4, defered.errback, ValueError("请输入字符串类型"))

    return defered # 只要是异步任务必须返回defer.Deferred对象。


def error(failure):
    print("异常回调", failure.type.__name__, #异常类型
          failure.value #异常信息
          )
    print(failure.getBriefTraceback()) #异常跟踪信息


def func2(num):
    print("func2得到值 ", num)
    reactor.stop()  # 如果不加它，程序就停不下下来

def callback(num):
    if isinstance(num,failure.Failure):
        print("异常回调")
    else:
        print("callback 得到值 ", num)

if __name__ == '__main__':
    defered = func1("1")
    # defered.addCallback(callback=func2).addErrback(errback=error)
    #defered.addCallbacks(func2,error)
    defered.addBoth(callback)
    print("准备run")
    reactor.run()
