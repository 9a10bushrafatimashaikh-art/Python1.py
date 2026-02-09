print("251A019", "09-03-26")
i= []
a=int(input("enter your value of a:"))
r=int(input("enter your value of r:"))
n=int(input("enter your value of n:"))
for x in range(n):
   i.append(a * (r** x))
print(i)

print("251A019", "09-02-26")
l=[]
for x in range(1, 10):
   s=x**2
   if s> 50:
      l.append(s)
print(l)
