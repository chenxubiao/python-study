#!/usr/bin/env python
#!coding=utf8
#Filename:simple_class.py

class Person:
    population = 0
    def __init__(self, name):
        self.name = name
        print '(adding a person %s)' % self.name
        Person.population += 1

    def __del__(self):
        print '%s says bye.' % self.name
        Person.population -= 1
        if Person.population == 0:
            print 'I am the last one.'
        else:
            print 'There are still %d people left.' % Person.population

    def sayHi(self):
        print 'Hi, my name is', self.name

    def howMany(self):
        if Person.population == 1:
            print 'I am the only person here'
        else:
            print 'We have %d persons here.' % Person.population


p = Person("p")
p.sayHi()
p.howMany()

d = Person("d")
d.sayHi()
d.howMany()

p.sayHi()
p.__del__()
d.howMany()


