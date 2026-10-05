# Simple Calculator in Python

print("===== Simple Calculator =====")

num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

<<<<<<< HEAD
elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Cannot divide by zero!"

=======
>>>>>>> b6ecaa6ff96b5d1fc68576950d4708ae104d25f4
else:
    result = "Invalid operator!"

print("Result:", result)
