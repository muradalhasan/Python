def make_sqare(a):
    dic={}
    for i in range(a[0],(a[1]+1)):
        dic[i]=i**2
    print(dic)
make_sqare((5,9))