#!/user/bin env python

import random

s = int(random.uniform(1,10))
# print(s)
m = int(input('input int:'))
while m!=s:
    if m > s:
        print('big')
        m= input('input int"')
    if m < s:
        print('small')
        m = input('input int')
    if m == s:
        print("ok")
        break
