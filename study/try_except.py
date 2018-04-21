#!/usr/bin/env python
#!coding=utf8
#Filename:try_except.py

import sys

try:
    s = raw_input('enter something->')
except EOFError:
    print '\nwhy did you do an EOF on me?'
    sys.exit()  # exit the program
except:
    print '\nsome error /exception occurred.'
    # here, we are not exiting the program
print 'done'
