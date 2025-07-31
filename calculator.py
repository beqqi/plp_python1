num1 = float(input("Enter first number: "))
operation = input("Choose operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    # Handle division by zero!
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Can't divide by zero!"
else:
    result = "Invalid operation!"

print(f"Result: {result}")