#!/usr/bin/env python
#!coding=utf8
#Filename:taising.py
class ShortInputException(Exception):
    ''' a user-defined exception class'''
    def __init__(self, length, atlease):
        Exception.__init__(self)
        self.length = length
        self.atleast = atlease

try:
    s = raw_input('enter something ->')
    if len(s) < 3:
        raise ShortInputException(len(s),3)
    # other work can continue as usual here
except EOFError:
    print '\nwhy did you do an EOF on me?'
except ShortInputException, x:
    print 'ShortInputException:The input was of length %d,\
was expecting at least %d' % (x.length, x.atleast)
else:
    print 'No exception wa raised.'
