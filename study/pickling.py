#!/usr/bin/env python
#!coding=utf8
#Filename:pickling.py

import cPickle as p
# import pickle as p

shopListFile = 'shoplist.data'
# the name of the file where we will store the object|

shopList = ['apple', 'mango', 'carrot']

# write to the file
f = file(shopListFile, 'w')
p.dump(shopList, f)     # dump the object to a file
f.close()

del shopList        # remove the shopList

# read back form the storage
f = file(shopListFile)
storedList = p.load(f)
print storedList



