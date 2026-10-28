#!/usr/bin/env python3
#while loop
print("Enter a number")
num = int(input())
i = 0
while i <= 9:
    result = num * i
    print(f"{i} x {num} = {result}")
    i += 1 


'''
#for loop
print("Enter a number")
num = int(input())

#range(10) will generate numbers from 0 to 9
for i in range(10):
    result = num * i
    print(f"{i} x {num} = {result}")
'''
