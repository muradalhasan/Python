def calc(sign,a,b):
    if sign=="+":
        print(a+b)
    elif sign=="-":
        print(a-b)
    elif sign=="*":
        print(a*b)
    else:
        print(a/b)
calc((input()),(int(input())),(int(input())))