num1 =int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /):")

result = 0

if operation == '/':
    if num2 != 0: result = num1 / num2
    else: print("Cannot divide by zero.")
if operation == '+':
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    result = num1 / num2
    
print("The result is", result, end='.')
