S=int(input())
L=0
if S<100:
    L=3000-125*(S*S)
else:
    L=12000/(4+((S*S)/14900))
print(L)