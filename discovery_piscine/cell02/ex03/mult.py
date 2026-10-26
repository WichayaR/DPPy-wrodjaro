print("Enter the first number: ")
first_num = int(input())

print("Enter the second number")
second_num = int(input())

result = first_num * second_num

print(f"{first_num} x {second_num} = {result}")

if result > 0:
    print("The result is positive.")
elif result < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")

