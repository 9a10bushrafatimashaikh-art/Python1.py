print("251A019","09/02/26")
student={ }
n=int(input("enter no of students: " ))
for i in range (1,n+1):  
 name=input("enter name: ")
 attendance=int(input("enter attendance :")) 
 student[i]={"name" : name , "attendance" : attendance}
print(student)
