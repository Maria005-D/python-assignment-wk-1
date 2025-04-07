
num1 = input("Enter the first number: ")
operator = input("Enter an operator (+, -, *, /): ")
num2 = input("Enter the second number: ")


expression = num1 + operator + num2
result = eval(expression)


print(f"{expression} = {result}")

