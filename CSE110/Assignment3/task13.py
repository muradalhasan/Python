cout=0
num=int(input())
for i in range(1,num+1):
    if num%i==0:
        cout+=1
print(cout)