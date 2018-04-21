#!/usr/bin/env python
#!coding=utf8
#Filename:cat.py

import sys

def readfile(filename):
    '''print a file to the standard output.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()

# script starts from here
print sys.argv
if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    # fetch sys.argv[1] but without the first two characters
    if option == 'version':
        print 'Version 1.2'
    elif option == 'help':
        print '''\
        This program prints files to the standard output.
        Any number of files can be specified.
        Options include:
        --version:Prints the version number
        --help:Display this help'''
    else:
        print 'Unknown option.'

    sys.exit()
else:
    for filename in sys.argv[1:]:
        readfile(filename)


'''
$ python cat.py
No action specified.
$ python cat.py --help
This program prints files to the standard output.
Any number of files can be specified.
Options include:
--version : Prints the version number
--help : Display this help
$ python cat.py --version
Version 1.2
$ python cat.py --nonsense
Unknown option.
$ python cat.py poem.txt

$ python cat.py poem.txt cat.py

'''