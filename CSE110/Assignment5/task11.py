lst1=[1, 4, 3, 2, 5]

lst2=[8, 7, 6, 9]

flag=False
for i in lst1:
    if i in lst2:
        flag=True
        break
print(flag)