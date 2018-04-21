#!/usr/bin/env python
#!coding=utf8
#Filename:finally.py

import time

try:
    f = file('poem.txt')

    while True:
        line = f.readline()
        if len(line) == 0:
            break
        time.sleep(2)
        print line,
finally:
    f.close()
    print 'Clearing up... closed the file'
