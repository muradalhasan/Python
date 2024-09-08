str1=input()
new=""
for i in range(len(str1)):
    if i==len(str1)-2:
        if str1[i]!=str1[i+1]:
            new+=str1[i]
            new+=str1[i+1]

            break
    else:
        if str1[i]!=str1[i+1]:
            new+=str1[i]
print(new)
    