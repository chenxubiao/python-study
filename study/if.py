#!/usr/bin/env python
#!coding=utf8
#Filename:if.py

number = 23

guess = int(raw_input("Enter na integer:"))

if guess == number:
    print("yes")

elif guess < number:
    print("no <")
else:
    print("no >")

print("done")

