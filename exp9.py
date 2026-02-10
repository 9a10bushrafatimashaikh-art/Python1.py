print("251A019" ,"10/02/26")
n = int(input("Enter a number: "))
fact = 1

if n < 0:
    print("Factorial not defined for negative numbers")
else:
    for i in range(1, n + 1):
        fact = fact * i
    print("Factorial =", fact)
