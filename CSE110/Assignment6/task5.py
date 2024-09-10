tup= (10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
num=int(input("Enter the number: "))
count=0
for i in tup:
    if i==num:
        count+=1
print(f"{num} appears {count} times in the tuple")