str1=input()
dic={}
for i in str1:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
print(dic)