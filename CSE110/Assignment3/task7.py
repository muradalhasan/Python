sum=0
count=0
for i in range(10):
    n=int(input())
    if n%2!=0:
        sum +=n
        count+=1
print(f"Sum = {sum}\nAverage= {sum/count}")