
# Simple calculator program

# Ask the user to input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask the user to choose an operation
operation = input("Choose an operation (+, -, *, /): ")

# Perform the operation and print the result
if operation == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please choose +, -, *, or /.")

