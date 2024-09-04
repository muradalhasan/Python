max=0
min=0
cout=0
for i in range(5):
    num=int(input())
    cout+=num
    if num>max:
        max=num
    if num<min:
        min=num
print(f"Max: {max}\nMin: {min}\nAgerage: {cout/5}")