# _*_ coding: utf-8 _*_

"""
@file: mylocker.py
@time: 2017/5/2 下午10:49
@author: pigbreeder
"""


class mylocker:
    def __init__(self):
        print("mylocker.__init__() called.")

    @staticmethod
    def acquire():
        print("mylocker.acquire() called.")

    @staticmethod
    def unlock():
        print("  mylocker.unlock() called.")


class lockerex(mylocker):
    @staticmethod
    def acquire():
        print("lockerex.acquire() called.")

    @staticmethod
    def unlock():
        print("  lockerex.unlock() called.")


def lockhelper(cls):
    '''''cls 必须实现acquire和release静态方法'''

    def _deco(func):
        def __deco(*args, **kwargs):
            print("before %s called." % func.__name__)
            cls.acquire()
            try:
                return func(*args, **kwargs)
            finally:
                cls.unlock()

        return __deco

    return _deco