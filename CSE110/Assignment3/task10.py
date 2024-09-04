num=input("enter the number")
for i in range(len(num)):
    res=int(num)%10
    num=int(num)//10
    print(res,end=" ")