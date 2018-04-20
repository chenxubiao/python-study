#!/usr/bin/env python
#!coding=utf8
#Filename:break.py


while True:
    s = raw_input("Enter something:")

    if s == 'quit':
        break

    elif len(s) < 3:
        continue

    print 'word is', s, ',len = ', len(s)

print("done")
