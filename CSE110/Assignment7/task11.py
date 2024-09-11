def rem_duplicate(a):
    lst1=[]
    for i in a:
        if i not in lst1:
            lst1.append(i)
    print(tuple(lst1))
rem_duplicate((1,1,1,2,3,4,5,6,6,6,6,4,0,0,0))