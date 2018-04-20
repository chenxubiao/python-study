#!/usr/bin/env python
#!coding=utf8
#Filename:func_param.py


def printMax(a, b):
    if a > b:
        print a, "is max num"
    else:
        print b, "is max num"

printMax(2, 3)

def localParam(x):
    print 'x = ', x
    x = 23
    print 'changed x to', x

localParam('asdf')


def globalParam(a):
    global x
    print 'a =', a
    x = 20
    print 'change x to',x


x = 'sdf'
globalParam(12)
print 'x =',x


def say(message, times = 1, a = 2):
    print message*times*a


say('hello')
say('a', 3)

say(message='b', a=3)


def max_num(x,y):
    if x >= y:
        return x
    else:
        return y


print max_num(23, 2)
