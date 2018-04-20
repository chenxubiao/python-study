#!/usr/bin/env python
#!coding=utf8
#Filename:func_doc.py

def printMax(x,y):
    ''' pirnt the max num of two nums.

    The two values must be integers.'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x)
    else:
        print y

printMax(3,5)

print printMax.__doc__


