str1=input()
lst=str1.split(", ")
dic={}
for o in lst:
    new=o.split(":")
    dic[new[0]]=int(new[1])
count=0
for j,k in dic.items():
    count+=k
print(f"Average is {count/(len(lst))}")