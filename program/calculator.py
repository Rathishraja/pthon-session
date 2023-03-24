num1 = float(input("enter the first number :"))
op = input("enter the operator :")
num2 = float(input("enter the second number"))

if op == '+' :
    result = num1 + num2
elif op == '-' :
    result = num1 - num2
elif op == '*' :
    result = num1 * num2
elif op == '/' :
    result = num1/num2
elif op == '%' :
    result = num1 % num2
else :
    result = "invalid input"
print(result)