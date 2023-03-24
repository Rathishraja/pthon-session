
try:   
    value = 10/0
    number = int(input("enter the number : "))
    print(number)
except ZeroDivisionError:
    print("divided by zero")

except ValueError:
    print("invalid input")