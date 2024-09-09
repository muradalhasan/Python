lst=input().split(", ")
new=[]
if len(lst)<=3:
    print("Not Possible!!")
else:
    new=lst[2:((len(lst)-2))]
    print(new)