#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'测试模块'
_author_ = 'zhbo'
import sys


def test():
    args = sys.argv
    print(args)
    if len(args) == 1:
        print('Hello, world!')
    elif len(args) == 2:
        print('Hello,%s' % args[1])
    else:
        print('Too many arguments!')


# 使用命令行时会创建一个main
if __name__ == '__main__':
    test()

from TestImport import _testPrtitial

print(_testPrtitial(1, y=2))


class Student:
    height = 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printSelf(self):
        print('name:%s, age:%d' % (self.name, self.age))


stu = Student('xiaoxiao', 12)
stu.printSelf()
stu1 = Student('dada', 13)
stu1.printSelf()


class Worker:
    __slots__ = ('name', 'age')
    pass


worker = Worker()
worker.name = 'xiaoxiao'
worker.age = 13

print(worker, worker.age, worker.name)
worker1 = Worker()

print(type(worker))

print(isinstance(worker, Worker))

print(dir(worker))

print(dir(stu1))

print(Student.height)

# 绑定方法
from types import MethodType


def add2(self,i):
    return 2 + i


worker1.name1 = MethodType(add2, worker1)
print(worker1.name1(2))
