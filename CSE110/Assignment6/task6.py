tup=(10, 20, 30, 40, 50, 60)

lst=list(tup)
for i in range((len(tup)//2)):
    temp=lst[i]
    lst[i]=lst[((len(lst)-1)-i)]
    lst[((len(lst)-1)-i)]=temp
print(tuple(lst))