#!/usr/bin/python

import sys

print ("%%%%% Finding biggest number of out three %%%%%%% ")
print (" ")

num1 = input("Enter the first number:  ")
num2 = input("Enter the second number:  ")
num3 = input("Enter the third number:  ")

if int(num1) > int(num2) and int(num1) > int(num3):
    print (num1 + " is biggest out of three")
elif int(num2) > int(num1) and int(num2) > int(num3):
    print (num2 + " is biggest out of three")
elif int(num3) > int(num1) and int(num3) > int(num2):
    print (num3 + " is biggest out of three")
else:
    print ("Two or all  numbers are same")
