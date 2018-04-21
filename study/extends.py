#!/usr/bin/env python
#!coding=utf8
#Filename:extends.py

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized School Member:%s)' % self.name

    def tell(self):
        print 'Nmae:"%s" Age:"%s"' % (self.name, self.age)

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self,name,age)
        self.salary = salary
        print '(Initialized Teacher:%s)' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary:"%d"' % self.salary

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self,name,age)
        self.marks = marks
        print '(Initialized Student:%s)' % self.name

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks:"%d"' % self.marks


t = Teacher("teacher", 32, 3200)
s = Student("chenxb", 18, 60)

print

members = [t,s]

for member in members:
    member.tell()
