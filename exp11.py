print("-----menu-----")

print("1.addition")
print("2.substraction")
print("3.multiply")
print("4.modulus")
print("5.division")

def add(num1,num2):
    sum = num1 + num2
    print("addition", sum)

def sub(num1,num2):
    diff = num1 - num2
    print("substraction", diff)

def mul(num1,num2):
    mul = num1 * num2
    print("multiply", mul)

def mod(num1,num2):
    rem = num1 % num2
    print("modulus", rem)

def div(num1,num2):
    if num2 == 0:
        print("num2 value should be greater than zero")
    else:
        div = num1 / num2
        print("division", div)

value1 = int(input("enter value 1: "))
value2 = int(input("enter value 2: "))
choice = int(input("enter your choice: "))

if choice == 1:
    add(value1,value2)

elif choice == 2:
    sub(value1,value2)

elif choice == 3:
    mul(value1,value2)

elif choice == 4:
    mod(value1,value2)

elif choice == 5:
    div(value1,value2)

else:
    print("invalid choice")