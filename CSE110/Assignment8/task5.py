def marks(a):
    lst = [ ["Alan", 95, 87, 91], ["Turing", 92, 90, 83], ["Elon", 87, 92, 80], ["Musk", 85, 94, 90] ]
    dic=[]
    for i in lst:
        if a=="MAT110":
            dic.append(((i[0]),i[3]))
        if a=="PHY111":
            dic.append(((i[0]),i[2]))
        if a=="CSE110":
            dic.append(((i[0]),i[1]))
         
    n = len(dic)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if dic[j][1] < dic[j+1][1]:
                dic[j], dic[j+1] = dic[j+1], dic[j]
    for s in dic:
        print(s[0])
marks((input("Enter the course name: ")))