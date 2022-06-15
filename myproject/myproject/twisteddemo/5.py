# # -*- coding: utf-8 -*-
# # @Time : 2022/6/7 9:27 下午
# # @Author : chenxiangan
# # @File : 5.py
# # @Software: PyCharm
# """
# 内联回调
# """
# from twisted.internet import reactor,defer
#
#
# def callback(num):
#     print("callback called with num =", num)
#     deferred = defer.Deferred()
#     #deferred.callback(num+1)
#     reactor.callLater(3,deferred.callback, num+1)
#     return deferred
#
#
# def callback2(num):
#     print("callback2 called with num =", num)
#     deferred = defer.Deferred()
#     deferred.callback(num+1)
#     return deferred
#
# def callback3(num):
#     print("callback3 called with num =", num)
#     deferred = defer.Deferred()
#     reactor.callLater(2,deferred.callback, num+1)
#     return deferred
# @defer.inlineCallbacks
# def main():
#     result = yield callback(5)
#     result2 = yield callback2(6)
#     result3 = yield callback2(7)
#     print(result)
#     print(result2)
#     print(result3)
#     reactor.stop()
#
# if __name__ == '__main__':
#     print("twisted开始运行")
#     reactor.callWhenRunning(main)
#     reactor.run()

#对于Python3可以使用async/await
import asyncio

from twisted.internet import reactor, defer
from twisted.internet.defer import Deferred


def callback(num):
    print("callback called with num =", num)
    deferred = defer.Deferred()
    # deferred.callback(num+1)
    reactor.callLater(3, deferred.callback, num + 1)
    return deferred


def callback2(num):
    print("callback2 called with num =", num)
    deferred = defer.Deferred()
    deferred.callback(num + 1)
    return deferred


def callback3(num):
    print("callback3 called with num =", num)
    deferred = defer.Deferred()
    reactor.callLater(2, deferred.callback, num + 1)
    return deferred


async def main():
    result = await callback(5)
    result2 = await callback2(6)
    result3 = await callback2(7)
    print(result)
    print(result2)
    print(result3)
    reactor.stop()


if __name__ == '__main__':
    print("twisted开始运行")
    defer.ensureDeferred(main())
    reactor.run()
