lst=input().split(",")
lsg_num=0
lsg_idx=0
print(lst)
for i in range(len(lst)):
    c=lst[i]
    if int(c)>lsg_num:
        lsg_num=int(c)
        lsg_idx=i
print(f"My list: {lst}\nLargest number in the list is {lsg_num} which was found at index {lsg_idx}.")