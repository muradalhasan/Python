dict_1 = {'A': [1, 2, 3], 'b': ['1', '2'], "c": [4, 5, 6, 7]}
count=0
for i,j in dict_1.items():
    for k in j:
        count+=1
print(count)