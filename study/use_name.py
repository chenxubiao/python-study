#!/usr/bin/env python
#!coding=utf8
#Filename:use_name.py

'''
模块的 __name__

每个模块都有一个名称，在模块中可以通过语句来找出模块的名称。
这在一个场合特别有用 ——就如前面所提到的，当一个模块被第一次输入的时候，这个模块的主块将被运行。
假如我 们只想在程序本身被使用的时候运行主块，而在它被别的模块输入的时候不运行主块，我们该 怎么做呢?
这可以通过模块的__name__属性完成。

$ python using_name.py

$ python
 \>>> import using_name
'''

if __name__ == '__main__':
    print('The program is being run by itself')
else:
    print('I am being imported from another module')
