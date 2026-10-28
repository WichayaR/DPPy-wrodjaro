#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

#List comprehension
new_array = [num + 2 for num in original_array]
print(f"Original array: {original_array}")
print(f"New array: {new_array}")
