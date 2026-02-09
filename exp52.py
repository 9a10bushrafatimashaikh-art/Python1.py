print("251A019", "9-02-2026")
l=[]
name=[]
age=[]
section=[]
name_1=input("enter your name: ")
name_2=input("enter your friend's name: ")
age_1=int(input("enter age: "))
age_2=int(input("enter your friend's age: "))
section_1=input("enter your section: ")
section_2=input("enter your friends section: ")
l.extend([(name_1, age_1, section_1), (name_2, age_2, section_2)])
print(l)
