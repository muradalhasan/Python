sum=0
num=int(input())
for i in range(1,num):
    if num%i==0:
        sum+=i
if sum==num:
    print("PErfect!")
else:
    print("Not perfect!!")