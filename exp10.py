print("251A019" ,"10/02/26")
n=int(input("enter num:" ))

if n<=1:
    print("neither prime nor composite")
else:
     flag=True
     for i in range(2,n):
         if n%i==0:
             flag=True
             break
         else:
            flag=False
     if flag==True:
          print("not prime")
     else:
            print("prime")
 




