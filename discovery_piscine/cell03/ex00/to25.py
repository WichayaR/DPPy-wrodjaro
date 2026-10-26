print("Enter a number less than 25")
numeric = int(input())

if numeric > 25:
    print("Error")
else:
    while numeric <= 25:
        print(f"Inside the loop, my variable is {numeric}")
        #numeric = numeric + 1
        numeric += 1