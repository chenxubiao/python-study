#!/usr/bin/env python
#!coding=utf8
#Filename:simple_class.py

class Person:
    def __init__(self):
        self.name = "unknow"

    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print 'Hi, my name is',self.name

p = Person()
p.sayHi()

p = Person("chenxb")
p.sayHi()



