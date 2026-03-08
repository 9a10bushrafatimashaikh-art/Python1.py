try:
    num1 = int(input("Enter first value : "))
    num2 = int(input("Enter second value : "))
    
    result = num1 / num2

except ZeroDivisionError:
    print("Number cannot be divided by zero.")

except ValueError:
    print("Invalid Input")

else:
    print("Division :", result)

finally:
    print("Thankyou.")