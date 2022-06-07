# -*- coding: utf-8 -*-
# @Time : 2022/6/7 11:41 上午
# @Author : chenxiangan
# @File : 4.py
# @Software: PyCharm
from twisted.internet import defer
from twisted.internet.defer import gatherResults


def cb1(result):
    print("cb1 called with result =", result)
    return result


def cb2(result):
    print("cb2 called with result =", result)
    return result


def cb3(result):
    print("cb3 called with result =", result)
    return result


def get_result(result):
    print("get_result called with result =", result)
    return result


if __name__ == '__main__':
    d1 = defer.Deferred()
    d1.addCallback(cb1)
    d2 = defer.Deferred()
    d2.addCallback(cb2)
    d3 = defer.Deferred()
    d3.addCallback(cb3)
    # 只有所有的回调对象都callback了才会调用get_result。
    # 如果中间有一个错误不会影响其他的回调。
    # dl = DeferredList([d1, d2, d3])
    # dl.addCallback(get_result)

    # 相比DeferredList，gatherResults只要有一个任务没有完成成功回调或者没有回调结果都不会返回挥结果
    #参数consumeErrors=True,可以捕获整个回调链中的异常，否则会抛出异常.
    g = gatherResults([d1, d2, d3],consumeErrors=True)
    g.addCallback(get_result).addErrback(get_result)
    #d1.errback(1)  # 触发错误回调
    d1.errback(Exception(123))
    d2.callback(2)
    d3.callback(3)
