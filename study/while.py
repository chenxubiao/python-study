#!/usr/bin/env python
#!coding=utf8
#Filename:while.py

number = 23
running = True

while running:
    guess = int(raw_input("Enter an integer:"))
    if guess == number:
        print("yes")
        running = False
    elif guess < number:
        print("no,<")
    else:
        print("no,>")
else:
    print("the while loop is over.")

print("done")


