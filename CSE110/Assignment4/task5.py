str1=input()
for i in range(len(str1)):
    for k in range(i+1):
        print(str1[k],end="")
    print()