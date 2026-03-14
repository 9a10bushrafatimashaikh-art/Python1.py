file=open("sample.txt","r")
content=file.read()
print(content)
file.close()

file=open("sample.txt","w")
content=file.write("rcoe")
print(content)
file.close()

file=open("sample.txt","a")
content=file.write(" AIDS  BRANCH")
print(content)

file.close()

file=open("sample.txt","r")
content=file.read()
print(content)
file.close()