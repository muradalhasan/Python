num=int(input())
flag=False
for i in range(2,num):
    if num%i==0:
        flag=True
        break
if flag:
    print("Not a prime number")
else:
    print("prime number")