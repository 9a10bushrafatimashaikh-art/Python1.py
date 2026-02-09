print("251A019", "9-02-2026")
l=[]
name=[]
age=[]
section=[]
name.extend((input("enter your name: "),input("enter your friends name: ")))
age.extend((input("enter your age: "),input("enter your f's age: ")))
section.extend((input("enter your section: "),input("enter your f's section: ")))
l.extend([(name[0], age[0], section[0]), (name[1], age[1], section[1])])
print(l)
