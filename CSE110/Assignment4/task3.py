var=input()
flag=True
for i in var:
    if i!="1" and i!="0":
        flag=False
        break
if flag:
    print("Binary Number")
else:
    print("Not a binary Number!")