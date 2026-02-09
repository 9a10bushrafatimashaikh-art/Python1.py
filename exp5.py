print("251A019", "9-02-2026")
l=[]
name=[]
age=[]
section=[]
name.append(input("enter your name: "))
name.append(input("enter your friend's name: "))
age.append(int(input("enter your age: ")))
age.append(int(input("enter your friend's age: ")))
section.append(input("enter your section: "))
section.append(input("enter your friends section: "))
l.append((name[0],age[0],section[0]))
l.append((name[1],age[1],section[1]))
print(l)
