# -*- coding: utf-8 -*-
# @Time : 2022/6/7 11:11 上午
# @Author : chenxiangan
# @File : 3.py
# @Software: PyCharm
from twisted.internet import defer


def main(num):
    defered = defer.Deferred()
    defered.callback(num)
    defered.addCallback(cb1).addCallback(cb2).addErrback(eb2).addCallback(cb3)
    return defered


def cb1(num):
    print("cb1 called with num =", num)
    raise ValueError(123)


def cb2(num):
    print("cb2 called with num =", num)
    return num + 3


def cb3(num):
    print("cb3 called with num =", num)


def eb2(failure):
    print(failure)
    print("cb1出错了，才进入到这里")
    return -1


if __name__ == '__main__':
    main(5)
