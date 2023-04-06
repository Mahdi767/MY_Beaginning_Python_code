operator =input('Enter an operator :(+,-,/,*)')
num1 = float(input("Enter the 1st Number"))
num2 = float(input("Enter the 2nd Number"))
if operator == "+":
    result = num1 + num2
    print(f"The result is{result}")
elif operator == '-':
    result = num1 -num2
    print(f"The result is{result}")
elif operator == '/' :
    result = num1 / num2
    print(f"The result is{result}")
elif operator == "*":
    result = num1 * num2
    print(f"The result is{result}")
else:
    print('Operator is not valid operator')


