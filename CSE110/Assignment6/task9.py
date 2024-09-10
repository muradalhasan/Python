exam_marks = {'Cierra Vega': 175, 'Alden Cantrell': 200, 'Kierra Gentry': 165, 'Pierre Cox': 190}
num=int(input())
dic={}
for j,k in exam_marks.items():
    if k>num:
        dic[j]=k
print(dic)