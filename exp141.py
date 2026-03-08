try:
    num1 = int(input("Enter first value: "))
    num2 = int(input("Enter second value: "))

    division = num1 / num2
    print("Division:", division)

except ZeroDivisionError:
    print("Number cannot be divided by zero.")