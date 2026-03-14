try:
    num1=int(input("enter first number :"))
    num2=int(input("enter second number :"))
    division=num1/num2
except ZeroDivisionError:
    print("division by zero is not possible")
    print("invalid input")
else:
    print("division:",division)
finally:
    print("thank you" )