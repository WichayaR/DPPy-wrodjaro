#!/usr/bin/env python3
print("What you gotta say?: ")
user_input = input()

while True:
    if user_input == "STOP":
        break
    user_input = input("I got that! Anything else? : ")

'''
print("What you gotta say?: ")
user_input = input()
while user_input != "STOP":
    user_input = input("I got that! Anything else? : ")
    if user_input == "STOP":
        break
'''