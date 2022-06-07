# -*- coding: utf-8 -*-
# @Time : 2022/6/6 10:01 下午
# @Author : chenxiangan
# @File : 1.py
# @Software: PyCharm
# from twisted.internet import selectreactor,epollreactor,pollreactor
# 如果想使用其他的事件循环管理器，则必须在引入reactor之前，先引入并通过install来安装覆盖。
# epollreactor.install()
from twisted.internet import reactor


def main(message):
    print(message)
    reactor.stop()  # 停止运行


if __name__ == '__main__':
    reactor.callWhenRunning(main, "Hello World")
    reactor.run()  # 运行
