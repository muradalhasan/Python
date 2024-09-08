var=input()
idx=int(input())
new=''
for i in range(idx,-1,-1):
    new+=var[i]
new+=var[idx+1:]
print(new)