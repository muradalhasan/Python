lst=input().split(", ")
lst1=[]
for i in lst:
    c=int(i)
    if i not in lst1:
        lst1.append(i)
print(lst1)