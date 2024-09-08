str1=input()
if len(str1)>3:
    if str1[-2:]=="er":
        new=str1[:-2]+"est"
    elif str1[-3:]=="est":
        new=str1
    else:
        new=str1+"er"
else:
    if str1[-2:]=="er":
        new=str1[:-2]+"est"
    else:
      new=str1
print(new)