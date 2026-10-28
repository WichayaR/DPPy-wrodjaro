#!/usr/bin/env python3
# cell03/ex03/advanced_mult.py

import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        print(f"table de {i}:", end="")

        j = 0
        while j <= 10:
            print(f"{i * j}", end="")
            if j < 10:
                print(", ", end="")
            j += 1
        print()
        i += 1
