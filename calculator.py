print("=====SIMPLECALCULATOR=====")

num1 = (float(input("Enter a first number: ")))
num2 = (float(input("Enter a second number: ")))

print("\nChoose an operation:\n")
print("+ Addition")
print("_ Subtraction")
print("* Multiplication")
print("/ Division")

operation = input("Enter an operation: ")
if operation == "+":
    print("Result:",num1 + num2)

elif operation == "-":
    print("Result:",num1 - num2)

elif operation == "*":
    print("Result:",num1 * num2)

elif operation == "/":
    if num2 != 0:
        print("Result:",num1 / num2)
    else:
        print("Error: Cannot divide by zero")

else:
    print("Invalid operation")