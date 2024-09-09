str1=input()
ls=[]
tmp=""
for i in str1:
    if i !=" ":
        tmp+=i
    else:
        if tmp!="":
            ls.append(int(tmp))
            tmp=''
print(ls)