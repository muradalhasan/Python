num=int(input("ENter the number: "))
for i in range(len(str(num))):
    div=10**(len(str(num))-1)
    res=num//div
    num=num%div
    print(res,end=" ")