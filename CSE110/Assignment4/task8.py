str1=input()
new=""
for i in range(len(str1)):
    if i%2==1:
        new+=chr((ord(str1[i]))-32)
print(new)
