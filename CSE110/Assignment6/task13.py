list_1 = [("a", 1), ("b", 2), ("a", 3), ("b", 1), ("a", 2), ("c", 1)]
dic={}
for i in list_1:
    if i[0] not in dic:
        dic[i[0]]=[(i[1])]
    else:
        dic[i[0]].append(i[1])
print(dic)