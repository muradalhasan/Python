dic={'sci fi': 12, 'mystery': 15, 'horror': 8, 'mythology': 10, 'young_adult': 4, 'adventure':14}
book=""
val=0
for i,j in dic.items():
    if j>val:
        book=i
        val=j
print(f"The highest selling book genre is {book} and the number of books sold are {val}.")