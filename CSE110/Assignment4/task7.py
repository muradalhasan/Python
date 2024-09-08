str1=input()
new=""
for i in str1:
    if ord(i)==122:
        new+="a"
    else:
        new+=chr((ord(i))+1)
print(new)