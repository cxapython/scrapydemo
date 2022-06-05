# -*- coding: utf-8 -*-
# @Time : 2022/6/5 5:07 下午
# @Author : chenxiangan
# @File : experment.py
# @Software: PyCharm
from twisted.internet import defer


def status(*ds):
    return [(getattr(d, 'result', "N/A"), len(d.callbacks)) for d in ds]


def b_callback(arg):
    print("b_callback called with arg =", arg)
    return b


def on_done(arg):
    print("on_done called with arg =", arg)
    return arg

if __name__ == '__main__':
    a = defer.Deferred()
    b = defer.Deferred()
    a.addCallback(b_callback).addCallback(on_done)
    status(a, b)
    b.callback(4)
    status(a, b)
    a.callback(3)
    status(a, b)