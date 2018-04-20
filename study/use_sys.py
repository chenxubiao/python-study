#!/usr/bin/env python
#!coding=utf8
#Filename:use_sys.py

'''This is use sys temp
    使用sys模块

    $ python use_sys.py we are arguments

    当Python执行import sys语句的时候，它在sys.path变量中所列目录中寻找sys.py模块。
    如果找到 了这个文件，这个模块的主块中的语句将被运行，然后这个模块将能够被你 使用 。
    注意，初始化过程仅在我们 第一次 输入模块的时候进行。另外，“sys”是“system”的缩写。

    记住，脚本的名称总是sys.argv列表的第一个参数。
    所以，在这里，'using_sys.py'是sys.argv [0]、'we'是sys.argv[1]、'are'是sys.argv[2]以及'arguments'是sys.argv[3]。
    注意，Python从0开始计 数，而非从1开始。
'''

import sys


print 'The command line argumentts are'

for i in sys.argv:
    print(i)

print '\n\nThe  PYTHON PATH is', sys.path, '\n'