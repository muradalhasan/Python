lst1=[1, 3, 5, 7, 9, 10]

lst2=[2, 4, 6, 8]

lst=[]
for i in range(len(lst1)):
    if i==len(lst1)-1:
        for j in lst2:
            lst.append(j)
    else:
        lst.append(lst1[i])
print(lst)